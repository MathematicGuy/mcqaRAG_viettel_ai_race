# 🚀 RAG MCQ System - Hướng Dẫn Sử Dụng Đầy Đủ

## 📋 Mục lục
1. [Tổng quan hệ thống](#tổng-quan)
2. [Cài đặt và khởi động](#cài-đặt)
3. [Xử lý PDF](#xử-lý-pdf)
4. [Tìm kiếm tài liệu](#tìm-kiếm)
5. [Trả lời câu hỏi MCQ](#trả-lời-mcq)
6. [Sử dụng Python API](#python-api)
7. [Troubleshooting](#troubleshooting)

---

## 📊 Tổng quan

### Dự án đã HOÀN THÀNH với các tính năng:

✅ **Core Features**
- PDF parsing với Docling + GROBID
- Section-aware chunking (600 words, 100 overlap)
- Multilingual embeddings (768D Sentence Transformers)
- Hybrid search (BM25 + Vector + RRF fusion)
- Local LLM với Ollama
- Complete RAG pipeline
- Apache Airflow automation
- FastAPI REST endpoints

✅ **Production Ready**
- Docker Compose orchestration
- Health checks for all services
- Comprehensive logging
- Error handling & retries
- Configuration management
- Database migrations

⏳ **Optional (Structure Ready)**
- Redis caching
- Langfuse monitoring

### Kiến trúc

```
PDF Files → Docling Parser → PostgreSQL → Chunking → Embeddings
                                                          ↓
Question → FastAPI → OpenSearch (Hybrid) → Ollama LLM → Answer
                            ↓
                      Redis Cache
```

---

## 🔧 Cài đặt

### Yêu cầu hệ thống
- Docker Desktop (chạy Docker Compose)
- Python 3.11+
- UV package manager
- 8GB+ RAM (16GB khuyến nghị)
- 20GB+ disk space

### Bước 1: Cài đặt UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify
uv --version
```

### Bước 2: Setup dự án

```bash
# Navigate to project
cd test/rag_mcq_system

# Copy environment file
cp .env.example .env

# Install dependencies
uv sync

# Start all services
docker compose up -d

# Wait for services to start (30-60 seconds)
sleep 60
```

### Bước 3: Pull LLM model

```bash
# Llama 3.2 3B (khuyến nghị - nhanh, nhẹ)
docker exec rag-mcq-ollama ollama pull llama3.2:1b

# Hoặc Qwen 2.5 7B (chất lượng cao hơn)
docker exec rag-mcq-ollama ollama pull qwen2.5:7b

# List models
docker exec rag-mcq-ollama ollama list
```

### Bước 4: Initialize database

```bash
uv run python -c "from src.db.session import init_db; init_db()"
```

### Bước 5: Verify installation

```bash
# Check health
curl http://localhost:8000/health | python -m json.tool

# Expected output: All services "healthy" or "ready"
```

---

## 📄 Xử lý PDF

### Bước 1: Thêm PDF files

```bash
# Copy PDFs vào thư mục data
cp /path/to/your/pdfs/*.pdf ../data/pdf/

# Kiểm tra
ls -lh ../data/pdf/
```

### Bước 2: Trigger Airflow DAG

#### Option 1: Qua Airflow UI (Khuyến nghị)

1. Mở http://localhost:8080
2. Login: `admin` / `admin`
3. Tìm DAG: `pdf_ingestion_dag`
4. Click nút **Trigger DAG** (▶️)
5. Monitor progress trong DAG run

#### Option 2: Qua CLI

```bash
docker exec rag-mcq-airflow airflow dags trigger pdf_ingestion_dag
```

### Bước 3: Monitor progress

```bash
# View Airflow logs
docker compose logs -f airflow

# Check indexed documents
curl -u admin:admin -k http://localhost:9200/mcq-documents/_count
```

### Pipeline workflow

```
1. Scan PDF files từ ../data/pdf/
2. Parse với Docling +