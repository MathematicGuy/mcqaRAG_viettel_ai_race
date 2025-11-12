# ViettelAI Race - MCQ RAG System

**RAG-based Multiple Choice Question Answering System** for ViettelAI Race Challenge. This system extracts knowledge from Vietnamese PDF documents and answers multiple-choice questions with high accuracy using hybrid search and LLM verification.

## 🏆 Challenge Overview

This project is built for the **ViettelAI Race Challenge**, which requires:
- **Input**: PDF documents (Vietnamese technical documents)
- **Task**: Answer multiple-choice questions based on document content
- **Output**: Structured answer file with document extraction and MCQ answers

### Output Format (`data/answer.md`)

The system generates a single submission file with two sections:

#### 1. TASK EXTRACT
Full markdown extraction of all PDF documents:
```markdown
### TASK EXTRACT

# Public_427
<Full markdown content of Public_427.pdf>

# Public_428
<Full markdown content of Public_428.pdf>
...
```

#### 2. TASK QA
MCQ answers in CSV format:
```csv
### TASK QA
num_correct,answers
1,A
1,C
2,"B, D"
1,B
...
```

## 📊 System Architecture

### Overview
```
PDFs → Extract → Chunk → Embed → Index → Search → Answer → Submit
```

### 1️⃣ Extraction Pipeline (`run_extract.ipynb`)
```
data/pdf/*.pdf  →  [Docling Parser]  →  PostgreSQL (documents)
                                              ↓
                    [Section Chunker]  →  PostgreSQL (chunks)
                                              ↓
                 [Sentence Transformer]  →  Add embeddings
                                              ↓
                    [OpenSearch Index]  →  Ready for search
```
**What it does:** Converts PDFs to searchable chunks with vector embeddings
- Parse 57 PDFs to markdown with Docling
- Split into 600-word chunks (100 overlap)
- Generate 768D multilingual embeddings
- Index to OpenSearch with hybrid BM25+Vector search

### 2️⃣ Inference Pipeline (`run_mcq_system.py`)
```
question.csv  →  [Search API]  →  100 candidates
                       ↓
              [Filter by doc_id]  →  45 candidates
                       ↓
              [LLM Verification]  →  28 relevant
                       ↓
              [LLM Generation]  →  Answer (A/B/C/D)
                       ↓
              answers_mcq.csv
```
**What it does:** Answers MCQs using retrieved context + LLM reasoning
- Hybrid search retrieves 100 candidate chunks
- Filter by document ID (Public_XXX pattern)
- LLM verifies chunk relevance (batch 15)
- Generate answer with SmallThinker-3B model

### 3️⃣ Post-Processing
```
private_test_output/*.md  →  [write_answers.py]  →  TASK EXTRACT
answers_mcq.csv           →  [process_answer.py]  →  TASK QA
                                                         ↓
                                               data/answer.md
```
**What it does:** Combines outputs into ViettelAI Race submission format

## 🎯 Key Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **PDF Parser** | Docling | Extract structured markdown from PDFs |
| **Database** | PostgreSQL 16 | Store documents and chunks |
| **Search** | OpenSearch 2.11 | Hybrid BM25 + Vector search |
| **Embeddings** | Sentence Transformers | 768D multilingual vectors |
| **LLM Server** | llama.cpp (port 8080) | Local inference server |
| **LLM Model** | SmallThinker-3B-Preview | Answer generation |
| **API** | FastAPI (port 8000) | Search REST endpoints |

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- llama.cpp with SmallThinker-3B model
- 16GB+ RAM, 50GB+ disk space

### 1. Setup Services

```bash
# Install dependencies
pip install -r requirements.txt
# or:
uv sync # recommened 

# Start Docker services
docker compose up -d

# Wait for initialization
sleep 30
```

### 2. Start llama.cpp Server

```bash
# Run llama.cpp server
./server -m "path/to/SmallThinker-3B-Preview-Q4_K_M.gguf" \
  -c 16384 --port 8080 --host 127.0.0.1
```

### 3. Verify Services

```bash
curl http://localhost:8000/health          # FastAPI
curl http://localhost:9200/_cluster/health # OpenSearch
docker exec rag-mcq-postgres pg_isready    # PostgreSQL
```

## 📝 Complete Workflow

### Step 1: Extract & Index PDFs

Run `run_extract.ipynb` notebook:

```python
# Cell 1: Parse PDFs to markdown
extract_pdfs_debug(pdf_paths, max_workers=7)

# Cell 2: Create chunks (600 words, 100 overlap)
chunk_documents_from_markdown()

# Cell 3: Generate embeddings & index
await generate_embeddings_and_index(chunk_ids)
```

**Output:** 57 PDFs → ~1234 chunks → OpenSearch index

### Step 2: Answer Questions

```bash
python run_mcq_system.py
```

**Configuration:**
```python
API_BASE_URL = "http://localhost:8000"
LLAMACPP_HOST = "http://127.0.0.1:8080"
TOP_K = 7           # Final chunks for answer
USE_HYBRID = True   # BM25 + Vector search
TIMEOUT = 180       # LLM timeout (seconds)
```

**Process:** Reads `data/question.csv` → Retrieves chunks → LLM verifies → Generates answers → Saves to `data/answers_mcq.csv`

### Step 3: Generate Submission

```bash
python post_processing/write_answers.py  # TASK EXTRACT
python data/process_answer.py            # TASK QA
```

**Output:** `data/answer.md` ready for submission

## 🔍 API Reference

### Search Endpoint

```bash
curl -X POST "http://localhost:8000/api/v1/search/" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Mục đích của Logic Bomb?",
    "top_k": 100,
    "use_hybrid": true
  }'
```

**Response:**
```json
{
  "results": [
    {"chunk_id": "...", "text": "...", "score": 0.95}
  ],
  "total": 100
}
```

## 💾 Database Schema

**documents table:**
- `doc_id`: "Public_427" (unique)
- `full_text`: Complete markdown content
- `processing_status`: "completed"

**document_chunks table:**
- `chunk_id`: "Public_427_chunk_0001" (unique)
- `chunk_text`: Text with context header
- `embedding`: Array[768] (vector)
- `indexed_in_opensearch`: "completed"

## 🛠️ Development Commands

```bash
# Start all services
docker compose up -d

# Check service status
make health  # or: docker compose ps

# View logs
docker compose logs -f api
docker compose logs -f opensearch

# Stop services
docker compose down
```

## 📁 Project Structure

```
mcqaRAG_p4/
├── src/                    # Core application
│   ├── services/
│   │   ├── pdf_parser/     # Docling integration
│   │   ├── chunking/       # Section-aware chunker
│   │   ├── embeddings/     # Sentence Transformers
│   │   ├── opensearch/     # Search client
│   │   └── ollama/         # llama.cpp client
│   ├── routers/            # FastAPI endpoints
│   ├── models/             # PostgreSQL models
│   └── db/                 # Database session
├── data/
│   ├── pdf/                # Input PDFs
│   ├── question.csv        # MCQ questions
│   └── answers_mcq.csv     # Generated answers
├── private_test_output/    # Extracted markdown files
├── post_processing/        # Submission formatters
├── run_extract.ipynb       # Extraction pipeline
├── run_mcq_system.py       # Inference pipeline
└── docker-compose.yml      # Service orchestration
```

## ⚙️ Configuration Files

**Environment Variables** (`.env`):
```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
OPENSEARCH_HOST=http://localhost:9200
REDIS_HOST=localhost
```

**Docker Services** (`docker-compose.yml`):
- PostgreSQL (port 5432)
- OpenSearch (port 9200)
- Redis (port 6379)
- FastAPI (port 8000)

## 📝 Notes

- **LLM Server**: Must start llama.cpp separately (not in Docker)
- **Model Size**: SmallThinker-3B requires ~2GB RAM
- **Search**: Hybrid mode (BM25+Vector) gives best results
- **Chunking**: 600 words with 100 overlap preserves context
- **Embeddings**: 768D multilingual supports Vietnamese

---

**License:** MIT | **Challenge:** ViettelAI Race 2025
