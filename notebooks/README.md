# 📓 Notebooks - RAG MCQ System

Thư mục này chứa các notebook và scripts để sử dụng hệ thống RAG MCQ một cách dễ dàng.

## 📁 Files

### `run_mcq_system.py` - Script Chính ⭐
**Script Python đơn giản để xử lý end-to-end:**

- ✅ Input: Folder PDF + file CSV câu hỏi
- ✅ Output: File CSV kết quả với đáp án + reasoning
- ✅ Tự động hóa toàn bộ quy trình

**Sử dụng:**
```bash
cd rag_mcq_system
python run_mcq_system.py
```

## 🚀 Quick Start

### 1. Chuẩn bị dữ liệu

```bash
# Copy PDF vào folder
cp /path/to/*.pdf ../data/pdf/

# Đảm bảo có file questions
ls ../data/question.csv
```

### 2. Khởi động hệ thống

```bash
# Start services
docker compose up -d

# Pull LLM model (lần đầu)
docker exec rag-mcq-ollama ollama pull llama3.2:3b
```

### 3. Chạy script

```bash
python run_mcq_system.py
```

Script sẽ:
1. Kiểm tra health của hệ thống
2. Kiểm tra PDF files
3. Hướng dẫn trigger Airflow để xử lý PDF
4. Đọc câu hỏi từ CSV
5. Trả lời tất cả câu hỏi
6. Lưu kết quả ra `../data/answers_output.csv`

## 📝 Format Dữ Liệu

### Input: `../data/question.csv`

```csv
Question,A,B,C,D,source_folder
"Câu hỏi 1?","Đáp án A","Đáp án B","Đáp án C","Đáp án D",train_fix
"Câu hỏi 2?","Đáp án A","Đáp án B","Đáp án C","Đáp án D",train_fix
```

### Output: `../data/answers_output.csv`

```csv
question_number,question,option_A,option_B,option_C,option_D,predicted_answer,confidence,reasoning,processing_time_seconds
1,"Câu hỏi 1?","A","B","C","D","B","high","Dựa vào tài liệu...",4.5
2,"Câu hỏi 2?","A","B","C","D","A","medium","Theo phân tích...",3.2
```

## ⚙️ Cấu Hình

### Thay đổi trong script

Edit `run_mcq_system.py`:

```python
# Dòng 29-31
TOP_K = 5              # Số documents để retrieve (3-10)
USE_HYBRID = True      # Hybrid search: BM25 + Vector
TIMEOUT = 60           # Timeout cho mỗi câu hỏi (seconds)
```

### Thay đổi LLM model

```bash
# Edit .env
OLLAMA_MODEL=qwen2.5:7b

# Pull model
docker exec rag-mcq-ollama ollama pull qwen2.5:7b

# Restart API
docker compose restart api
```

## 🔄 Workflow

```
┌─────────────┐
│ PDF Files   │
│ in data/pdf │
└──────┬──────┘
       │
       ↓
┌─────────────────────┐
│ Airflow DAG         │
│ (Manual Trigger)    │
│                     │
│ • Parse (Docling)   │
│ • Chunk (600 words) │
│ • Embed (768D)      │
│ • Index (OpenSearch)│
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│ Questions CSV       │
│ (question.csv)      │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│ RAG Pipeline        │
│                     │
│ 1. Search (Hybrid)  │
│ 2. LLM Generate     │
│ 3. Parse Answer     │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│ Output CSV          │
│ (answers_output.csv)│
│                     │
│ • Đáp án            │
│ • Reasoning         │
│ • Confidence        │
│ • Sources           │
└─────────────────────┘
```

## 📊 Ví Dụ Output

```
═══════════════════════════════════════════════════════════════════
  🚀 RAG MCQ SYSTEM - AUTOMATIC ANSWERING
═══════════════════════════════════════════════════════════════════

📅 Bắt đầu: 2024-01-15 10:30:00

────────────────────────────────────────────────────────────────────
📌 BƯỚC 0: Kiểm tra hệ thống
────────────────────────────────────────────────────────────────────

✅ API Status: healthy

📦 Services:
  ✅ postgres: healthy
  ✅ opensearch: ready
  ✅ ollama: ready
  ✅ airflow: healthy

✅ Hệ thống hoạt động bình thường!

────────────────────────────────────────────────────────────────────
📌 BƯỚC 1: Kiểm tra PDF files
────────────────────────────────────────────────────────────────────

✅ Tìm thấy 5 file(s) PDF:
  1. document1.pdf (2.34 MB)
  2. document2.pdf (1.89 MB)
  3. document3.pdf (3.12 MB)
  4. document4.pdf (2.67 MB)
  5. document5.pdf (1.45 MB)

────────────────────────────────────────────────────────────────────
📌 BƯỚC 4: Đọc câu hỏi từ CSV
────────────────────────────────────────────────────────────────────

✅ Đọc thành công 10 câu hỏi

────────────────────────────────────────────────────────────────────
📌 BƯỚC 5: Trả lời câu hỏi
────────────────────────────────────────────────────────────────────

🎯 Bắt đầu trả lời 10 câu hỏi...

[1/10] (10.0%) Q: Cho ma trận hiệp phương sai S của dữ liệu đã chuẩn...
    → Đáp án: A 🟢 (4.5s)
[2/10] (20.0%) Q: Tên gọi riêng cho đỉnh bậc 0 và đỉnh bậc 1...
    → Đáp án: B 🟢 (3.8s)
[3/10] (30.0%) Q: Cơ chế lưu trữ năng lượng của siêu tụ điện...
    → Đáp án: B 🟡 (4.2s)
...

────────────────────────────────────────────────────────────────────
✅ Hoàn thành! Tổng thời gian: 45.3s
⏱️  Trung bình: 4.5s/câu
────────────────────────────────────────────────────────────────────

✅ Đã lưu kết quả vào: /path/to/data/answers_output.csv
📊 Tổng số câu: 10

📈 Thống kê độ tin cậy:
  • high: 7 câu (70.0%)
  • medium: 2 câu (20.0%)
  • low: 1 câu (10.0%)
```

## 🐛 Troubleshooting

### Script không chạy được

```bash
# Kiểm tra Python version (cần 3.11+)
python --version

# Cài dependencies
cd rag_mcq_system
uv sync

# Hoặc dùng pip
pip install requests pandas
```

### Services chưa sẵn sàng

```bash
# Kiểm tra
docker compose ps

# Start lại
docker compose up -d

# Xem logs
docker compose logs -f
```

### Không có documents trong OpenSearch

```bash
# Trigger Airflow DAG
docker exec rag-mcq-airflow airflow dags trigger pdf_ingestion_dag

# Hoặc dùng UI: http://localhost:8080
```

### Timeout khi trả lời

```python
# Tăng TIMEOUT trong run_mcq_system.py
TIMEOUT = 120  # Tăng lên 120 seconds
```

## 📚 Tài Liệu

- **Quick Start Guide**: `../QUICK_START.md`
- **Full README**: `../README.md`
- **API Docs**: http://localhost:8000/docs
- **Completion Checklist**: `../COMPLETION_CHECKLIST.md`

## 💡 Tips

### Tăng chất lượng:
- Sử dụng `USE_HYBRID = True` (mặc định)
- Tăng `TOP_K = 10` để retrieve nhiều documents hơn
- Dùng model lớn hơn: `qwen2.5:7b` thay vì `llama3.2:3b`

### Tăng tốc độ:
- Giảm `TOP_K = 3`
- Dùng model nhỏ: `llama3.2:3b`
- Giảm `TIMEOUT` nếu LLM đã nhanh

### Debug:
- Check API health: `curl http://localhost:8000/health`
- Check documents: `curl -u admin:admin http://localhost:9200/mcq-documents/_count`
- Xem logs: `docker compose logs -f api`

## ✅ Checklist

- [ ] Docker đang chạy
- [ ] Services started: `docker compose up -d`
- [ ] LLM model pulled: `docker exec rag-mcq-ollama ollama pull llama3.2:3b`
- [ ] PDFs copied: `../data/pdf/*.pdf`
- [ ] Questions ready: `../data/question.csv`
- [ ] Airflow DAG completed
- [ ] Run script: `python run_mcq_system.py`
- [ ] Check output: `../data/answers_output.csv`

---

**🎉 Sẵn sàng! Chạy `python run_mcq_system.py` để bắt đầu!**