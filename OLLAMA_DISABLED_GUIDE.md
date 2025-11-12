# Ollama Disabled - Migration Guide

## Summary of Changes

✅ **Ollama container commented out in docker-compose.yml**
✅ **Ollama dependency removed from API service**
✅ **Ollama data volume removed**

## Functions That Will NO LONGER WORK Without Ollama

### 1. **RAG API Endpoint** (Most Critical)
**File**: `src/routers/ask.py`
**Endpoint**: `POST /api/v1/ask`

```python
# This endpoint uses RAGPipeline which requires ollama_client
@router.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest, pipeline: RAGPipelineDep):
    result = await pipeline.answer_question(...)
    # ❌ Will fail because RAGPipeline uses self.ollama
```

**Status**: ❌ **BROKEN** - Needs fallback or removal

---

### 2. **RAG Pipeline** (Core Logic)
**File**: `src/services/rag/pipeline.py`

```python
class RAGPipeline:
    def __init__(self, ..., ollama_client, ...):
        self.ollama = ollama_client  # ❌ Required

    async def answer_question(self, question, options, ...):
        response = await self.ollama.generate_mcq_answer(
            question=question,
            options=options,
            context_chunks=chunks,  # ❌ Will fail without LLM
        )
```

**Status**: ❌ **BROKEN** - Requires LLM client

---

### 3. **OllamaClient Initialization**
**File**: `src/services/ollama/client.py`

```python
class OllamaClient:
    """Ollama LLM client for MCQ answer generation."""
    def __init__(self, host="http://localhost:11434", ...):
        # ❌ Assumes Ollama is running at http://localhost:11434
```

**Status**: ❌ **UNUSABLE** - Ollama not in Docker anymore

---

### 4. **Factory Function** (Currently Auto-Selects)
**File**: `src/services/factories.py`

```python
@lru_cache()
def make_ollama_client():
    # ✅ Currently checks for port 8080 (llama.cpp) vs 11434 (Ollama)
    if ":8080" in settings.ollama.host:
        return OllamaCppClient(...)  # ✅ Works - uses external llama.cpp
    else:
        return OllamaClient(...)  # ❌ Will fail - Docker Ollama disabled
```

**Status**: ⚠️ **WORKS IF** - Using external llama.cpp on port 8080

---

## What Still Works

### ✅ Retrieval Endpoints (No LLM needed)
- `POST /api/v1/search` - OpenSearch hybrid search
- `POST /api/v1/search/bm25` - BM25 search only
- `GET /health` - Health check

### ✅ Document Indexing
- `POST /api/v1/documents/index` - Index PDFs
- `POST /api/v1/documents/upload` - Upload new documents

### ✅ Notebook Inference (With External llama.cpp)
- `run_inference.ipynb` - ✅ Works if llama.cpp server on port 8080
- Direct `OllamaCppClient` usage - ✅ Works with external server

---

## How to Fix the RAG API

### Option 1: Use External Ollama (Recommended)
**Setup**:
```bash
# Install Ollama locally
# https://ollama.ai

# Run Ollama server
ollama serve

# Pull model in another terminal
ollama pull qwen3:1.7b
```

**Update docker-compose.yml environment**:
```yaml
environment:
  - OLLAMA_HOST=http://host.docker.internal:11434  # Windows/Mac
  # Or for Linux:
  - OLLAMA_HOST=http://127.0.0.1:11434
```

**Docker compose command**:
```bash
docker-compose up -d
```

---

### Option 2: Use External llama.cpp (What You're Doing)
**Setup**:
```bash
# Run llama.cpp server locally
./server -m model.gguf -c 4096 -ngl 33
```

**In factories.py, the auto-detection already handles this**:
- If `OLLAMA_HOST=http://127.0.0.1:8080` → Uses `OllamaCppClient`
- If `OLLAMA_HOST=http://host.docker.internal:11434` → Uses `OllamaClient`

**Status**: ✅ Already works! No changes needed.

---

### Option 3: Uncomment Ollama in docker-compose.yml
If you change your mind, simply uncomment:
```yaml
# In docker-compose.yml, uncomment:
ollama:
  image: ollama/ollama:0.11.2
  ...

# And re-add to depends_on:
depends_on:
  ollama:
    condition: service_healthy
```

Then rebuild:
```bash
docker-compose down -v
docker-compose up -d
```

---

## Environment Variable Configuration

### For External Ollama
```bash
# .env file
OLLAMA_HOST=http://host.docker.internal:11434  # Windows/Mac
# or
OLLAMA_HOST=http://127.0.0.1:11434  # Linux
```

### For External llama.cpp (Your Setup)
```bash
# .env file
OLLAMA_HOST=http://127.0.0.1:8080
```

The factory will automatically use `OllamaCppClient` for port 8080.

---

## Testing Your Setup

### Test 1: Check if llama.cpp is running
```bash
curl http://127.0.0.1:8080/health
```

### Test 2: Check if API can reach it
```bash
# From inside Docker API container
curl http://host.docker.internal:8080/health
# or
curl http://127.0.0.1:8080/health
```

### Test 3: Use the notebook
```python
# run_inference.ipynb
# This should work fine since it directly uses OllamaCppClient
```

### Test 4: Try the RAG API
```bash
curl -X POST http://localhost:8000/api/v1/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is AI?","options":{"A":"...","B":"...","C":"...","D":"..."}}'
```

If this fails → RAGPipeline is trying to use Docker Ollama (which is disabled)

---

## Summary Table

| Component | Status | Notes |
|-----------|--------|-------|
| Docker Ollama | ❌ DISABLED | Commented out in docker-compose.yml |
| RAG API `/ask` | ⚠️ PARTIAL | Works with external Ollama/llama.cpp |
| Notebook inference | ✅ WORKS | Uses external llama.cpp on port 8080 |
| Search endpoints | ✅ WORKS | No LLM needed |
| OllamaCppClient | ✅ WORKS | For llama.cpp server |
| OllamaClient | ⚠️ BROKEN | Docker Ollama not available |

---

## Next Steps

1. **If using external llama.cpp**: No action needed, your setup is correct
2. **If using external Ollama**: Update `docker-compose.yml` environment variable
3. **If you want Docker Ollama back**: Uncomment the service in `docker-compose.yml`
