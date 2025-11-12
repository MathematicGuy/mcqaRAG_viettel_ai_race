import os
from pathlib import Path
from src.config import get_settings
from src.services.ollama.ollamacpp_client import OllamaCppClient
# ./server -m "C:\Users\APC\AppData\Local\llama.cpp\bartowski_SmallThinker-3B-Preview-GGUF_SmallThinker-3B-Preview-Q4_K_M.gguf" -c 16384
API_BASE_URL = "http://localhost:8000"
AIRFLOW_URL = "http://localhost:8080"

# Host & port các service
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432          # hoặc 5433 nếu muốn connect airflow-db
REDIS_HOST = "localhost"
REDIS_PORT = 6379
OPENSEARCH_HOST = "http://localhost:9200"
LLAMACPP_HOST = "http://127.0.0.1:8080"

# Cấu hình RAG
TOP_K = 10
USE_HYBRID = True
TIMEOUT = 180
MAX_WORKERS = 1

# Initialize llama.cpp client
llama_client = OllamaCppClient(
    host=LLAMACPP_HOST,
    model="gpt-like-model",
    temperature=0.3,
    max_response_words=400,
    timeout=TIMEOUT
)

settings = get_settings()
pdf_dir = Path(settings.data.pdf_dir)

pdf_files = list(pdf_dir.glob("*.pdf"))
pdf_paths = [str(f) for f in pdf_files]

print(f"Found {len(pdf_paths)} PDF files:")
print(f"Llama.cpp client initialized at: {LLAMACPP_HOST}")

import requests
import pandas as pd
import time
import json
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime
import socket
from urllib.parse import urlparse

# Đường dẫn files
DATA_DIR = Path("data")
PDF_DIR = DATA_DIR / "pdf"
QUESTION_FILE = DATA_DIR / "question.csv"
OUTPUT_FILE = DATA_DIR / "answers_mcq.csv"


def print_header(text: str):
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)

def print_step(step_num: int, text: str):
    print(f"\n{'─' * 80}")
    print(f"📌 BƯỚC {step_num}: {text}")
    print(f"{'─' * 80}")

def print_step(step_num: int, text: str):
    print(f"\n{'─' * 80}")
    print(f"📌 BƯỚC {step_num}: {text}")
    print(f"{'─' * 80}")


def load_questions() -> pd.DataFrame:
    """Đọc câu hỏi từ CSV file."""
    print_step(4, "Đọc câu hỏi từ CSV")

    if not QUESTION_FILE.exists():
        print(f"\n❌ File không tồn tại: {QUESTION_FILE}")
        print("Vui lòng tạo file question.csv với format:")
        print("  Question,A,B,C,D,source_folder")
        return None

    try:
        df = pd.read_csv(QUESTION_FILE)
        print(f"\n✅ Đọc thành công {len(df)} câu hỏi")

        # Kiểm tra columns
        required_cols = ["Question", "A", "B", "C", "D"]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"❌ Thiếu columns: {missing_cols}")
            return None

        # Hiển thị sample
        print("\n📝 Ví dụ câu hỏi đầu tiên:")
        print(f"   Q: {df.iloc[0]['Question']}...")

        return df

    except Exception as e:
        print(f"❌ Lỗi khi đọc CSV: {e}")
        return None

# load_questions().head()

async def ask_single_question_direct(
    question: str,
    options: Dict[str, str],
    context_chunks: List[Dict] = None
) -> Dict[str, Any]:
    """
    Trả lời câu hỏi MCQ using OllamaCppClient directly.

    Args:
        question: Question text
        options: Dict of options {"A": "...", "B": "...", ...}
        context_chunks: Optional list of retrieved context chunks
                        If None, will answer without context

    Returns:
        Dict with predicted_option, reasoning, confidence, etc.
    """
    try:
        # Use empty context if none provided
        if context_chunks is None:
            context_chunks = []

        # Call llama.cpp client directly
        result = await llama_client.generate_mcq_answer(
            question=question,
            options=options,
            context_chunks=context_chunks
        )

        return result

    except Exception as e:
        print(f"    ❌ Lỗi: {str(e)[:100]}")
        return {
            "error": str(e),
            "predicted_option": None,
            "confidence": "low",
            "reasoning": f"Error: {str(e)}"
        }


# Option 3: Synchronous wrapper for direct client usage
def ask_single_question_cpp(
    question: str,
    options: Dict[str, str],
    source_folder: str = None,
    context_chunks: List[Dict] = None
) -> Dict[str, Any]:
    """
    Synchronous wrapper for OllamaCppClient.
    Can be used with or without context chunks.
    """
    import asyncio

    # Create event loop if needed
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Run async function
    result = loop.run_until_complete(
        ask_single_question_direct(question, options, context_chunks)
    )

    return result


import re
import requests
from IPython.display import Markdown

def retrieve(query, top_k=TOP_K, use_hybrid=USE_HYBRID):
    """Retrieve chunks from OpenSearch API."""
    url = "http://localhost:8000/api/v1/search/"  # Fixed URL (was missing /)
    payload = {
        "query": query,
        "top_k": top_k,
        "use_hybrid": use_hybrid
    }
    try:
        r = requests.post(url, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print(f"❌ retrieve() error: {e}")
        return {"hits": []}


def extract_doc_id_from_question(question: str) -> str:
    """
    Extract Public_XXX pattern from question text.
    Returns the pattern if found, otherwise None.

    Example: "Question about Public_422" -> "Public_422"
    """
    match = re.search(r'Public_\d+', question)
    return match.group(0) if match else None


def dynamic_retrieve_context(question: str, top_k: int = TOP_K) -> List[Dict]:
    """
    Retrieve top_k chunks for question.
    Auto-adjusts top_k and filtering based on question pattern.

    - If Public_XXX pattern found: top_k=30 and filter by doc_id
    - Otherwise: use default top_k

    Returns list of chunk dicts with metadata.
    """
    # Try to find Public_XXX pattern in question first
    doc_id_prefix = extract_doc_id_from_question(question)

    # ✅ Dynamic top_k adjustment
    effective_top_k = 50 if doc_id_prefix else top_k

    # Get chunks from OpenSearch with adjusted top_k
    response_data = retrieve(question, top_k=effective_top_k, use_hybrid=USE_HYBRID)
    hits = response_data.get('hits', [])

    results = []
    for hit in hits:
        chunk_id = hit.get('chunk_id', '')

        # Filter by doc_id_prefix only if found in question
        if doc_id_prefix:
            if not chunk_id.startswith(doc_id_prefix):
                continue  # Skip chunks that don't match doc_id

        # Build chunk dict with metadata
        results.append({
            'chunk_id': chunk_id,
            'chunk_text': hit.get('chunk_text', ''),
            'section_name': hit.get('section_name'),
            'document_id': hit.get('document_id'),
            'document_file_name': hit.get('document_file_name'),
            'document_title': hit.get('document_title'),
        })

        if len(results) >= TOP_K:
            break  # Limit to TOP_K after filtering

    # ✅ Better logging
    if doc_id_prefix:
        print(f"✅ Found {len(results)} chunks (filtered by {doc_id_prefix}, searched top {effective_top_k})")
    else:
        print(f"✅ Found {len(results)} chunks (default search with top {effective_top_k})")

    return results


def _process_single_question(args: tuple) -> Dict[str, Any]:
    """
    Process a single question for parallel execution.
    Uses OllamaCppClient directly without context retrieval.

    Args:
        args: Tuple of (index, row, q_num, total)

    Returns:
        Result dictionary for the question
    """
    idx, row, q_num, total = args

    progress = (q_num / total) * 100
    print(f"[{q_num}/{total}] ({progress:.1f}%) Q: {row['Question']}")

    options = {"A": str(row["A"]), "B": str(row["B"]), "C": str(row["C"]), "D": str(row["D"])}
    source_folder = row.get("source_folder", None)

    q_start = time.time()

    # Use direct llama.cpp client (no context retrieval)
    # If you want to add context, retrieve it first and pass to context_chunks parameter
    answer_data = ask_single_question_cpp(
        question=row["Question"],
        options=options,
        context_chunks=dynamic_retrieve_context(row["Question"])  # No context - direct generation only
        # context_chunks=[]  # No context - direct generation only
    )

    q_time = time.time() - q_start

    predicted = answer_data.get("predicted_option", "N/A")
    confidence = answer_data.get("confidence", "unknown")
    reasoning = answer_data.get("reasoning", "")
    error = answer_data.get("error", None)

    conf_icon = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(confidence, "⚪")
    print(f"    → Đáp án: {predicted} {conf_icon} ({q_time:.1f}s)")
    print(f"      Suy luận: {reasoning}")

    result = {
        "question_number": q_num,
        "question": row["Question"],
        "option_A": row["A"],
        "option_B": row["B"],
        "option_C": row["C"],
        "option_D": row["D"],
        "source_folder": source_folder if pd.notna(source_folder) else "",
        "predicted_answer": predicted,
        "confidence": confidence,
        "reasoning": reasoning[:500] if reasoning else "",
        "processing_time_seconds": round(q_time, 2),
        "error": error if error else "",
        "timestamp": datetime.now().isoformat(),
    }

    return result


def answer_all_questions(df: pd.DataFrame, max_workers: int = 4) -> pd.DataFrame:
    """Trả lời tất cả câu hỏi trong dataframe sử dụng parallel processing."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    print_step(5, "Trả lời câu hỏi (Parallel)")

    results = []
    total = len(df)

    print(f"\n🎯 Bắt đầu trả lời {total} câu hỏi...\n")
    print(f"⚙️  Using {max_workers} parallel workers\n")
    # print(f"🔧 Mode: Direct llama.cpp generation (no context retrieval)\n")

    start_time = time.time()

    # Prepare task arguments
    tasks = [(idx, row, idx + 1, total) for idx, (_, row) in enumerate(df.iterrows())]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_process_single_question, task): task[0] for task in tasks}

        completed_count = 0
        for future in as_completed(futures):
            try:
                result = future.result(timeout=TIMEOUT + 30)
                results.append(result)
                completed_count += 1

                if completed_count % 5 == 0:
                    print()

            except Exception as e:
                completed_count += 1
                print(f"❌ Error processing question: {str(e)[:100]}")
                results.append({
                    "error": str(e),
                    "predicted_option": None,
                    "question_number": futures[future] + 1
                })

    total_time = time.time() - start_time

    print("\n" + "─" * 80)
    print(f"✅ Hoàn thành! Tổng thời gian: {total_time:.1f}s")
    print(f"⏱️  Trung bình: {total_time / total:.1f}s/câu")
    print(f"⚡ Tốc độ: {total / total_time:.2f} câu/giây")
    print("─" * 80)

    # Sort results by question number
    results.sort(key=lambda x: x.get("question_number", 0))

    return pd.DataFrame(results)

def save_results(results_df: pd.DataFrame):
    """Lưu kết quả ra CSV file."""
    print_step(6, "Lưu kết quả")

    try:
        results_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

        print(f"\n✅ Đã lưu kết quả vào: {OUTPUT_FILE}")
        print(f"📊 Tổng số câu: {len(results_df)}")

        # Thống kê
        conf_counts = results_df["confidence"].value_counts()
        print("\n📈 Thống kê độ tin cậy:")
        for conf, count in conf_counts.items():
            percentage = (count / len(results_df)) * 100
            print(f"  • {conf}: {count} câu ({percentage:.1f}%)")

        # Kiểm tra errors
        errors = results_df[results_df["error"] != ""]
        if len(errors) > 0:
            print(f"\n⚠️  Có {len(errors)} câu bị lỗi:")
            for idx, row in errors.iterrows():
                print(f"  • Câu {row['question_number']}: {row['error']}")

    except Exception as e:
        print(f"❌ Lỗi khi lưu file: {e}")

def display_summary(results_df: pd.DataFrame):
    """Hiển thị tóm tắt kết quả."""
    print_header("📊 TÓM TẮT KẾT QUẢ")

    total = len(results_df)
    successful = len(results_df[results_df["error"] == ""])

    print(f"\n✅ Tổng số câu: {total}")
    print(f"✅ Trả lời thành công: {successful}")
    print(f"❌ Lỗi: {total - successful}")

    # Top 5 câu có confidence cao
    high_conf = results_df[results_df["confidence"] == "high"].head(20)
    if len(high_conf) > 0:
        print(f"\n🟢 Top {len(high_conf)} câu có độ tin cậy cao:")
        for idx, row in high_conf.iterrows():
            print(
                f"  {row['question_number']}. Đáp án {row['predicted_answer']}: {row['question']}"
            )

    # Câu có confidence thấp
    low_conf = results_df[results_df["confidence"] == "low"]
    if len(low_conf) > 0:
        print(f"\n🔴 {len(low_conf)} câu có độ tin cậy thấp:")
        for idx, row in low_conf.head(20).iterrows():
            print(f"  {row['question_number']}. {row['question']}")

    print("\n" + "=" * 80)



def main():
    """Hàm chính để chạy toàn bộ pipeline."""
    MAX_WORKERS  = 1
    print_header("🚀 RAG MCQ SYSTEM - AUTOMATIC ANSWERING")
    print(f"\n📅 Bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    questions_df = load_questions()
    if questions_df is None:
        return

    results_df = answer_all_questions(questions_df, max_workers=MAX_WORKERS)

    save_results(results_df)

if __name__ == "__main__":
    main()