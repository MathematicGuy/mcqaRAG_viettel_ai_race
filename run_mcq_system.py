#!/usr/bin/env python3
"""
RAG MCQ System - Simple Usage Script
====================================

Script đơn giản để:
1. Xử lý tất cả PDF trong folder data/pdf
2. Đọc câu hỏi từ file data/question.csv
3. Trả lời từng câu hỏi bằng RAG system
4. Xuất kết quả ra file data/answers_output.csv

Usage:
    python run_mcq_system.py
"""

import requests
import pandas as pd
import time
import json
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


# =====================================================================
# CONFIGURATION
# =====================================================================

API_BASE_URL = "http://localhost:8000"
AIRFLOW_URL = "http://localhost:8080"

# Đường dẫn files
DATA_DIR = Path("../data")
PDF_DIR = DATA_DIR / "pdf"
QUESTION_FILE = DATA_DIR / "question.csv"
OUTPUT_FILE = DATA_DIR / "answers_output.csv"

# Cấu hình RAG
TOP_K = 5  # Số lượng documents để retrieve
USE_HYBRID = True  # Sử dụng hybrid search (BM25 + Vector)
TIMEOUT = 60  # Timeout cho mỗi câu hỏi (seconds)


# =====================================================================
# UTILITY FUNCTIONS
# =====================================================================


def print_header(text: str):
    """In header đẹp."""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)


def print_step(step_num: int, text: str):
    """In bước thực hiện."""
    print(f"\n{'─' * 80}")
    print(f"📌 BƯỚC {step_num}: {text}")
    print(f"{'─' * 80}")


def check_system_health() -> bool:
    """Kiểm tra health của hệ thống."""
    print_step(0, "Kiểm tra hệ thống")

    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=10)
        health_data = response.json()

        print(f"\n✅ API Status: {health_data['status']}")

        services = health_data.get("services", {})
        all_healthy = True

        print("\n📦 Services:")
        for service, status in services.items():
            is_ok = status in ["healthy", "ready", "connected"]
            icon = "✅" if is_ok else "❌"
            print(f"  {icon} {service}: {status}")
            if not is_ok:
                all_healthy = False

        if not all_healthy:
            print("\n⚠️  CẢNH BÁO: Một số services chưa sẵn sàng!")
            print("Vui lòng chạy: docker compose up -d")
            return False

        print("\n✅ Hệ thống hoạt động bình thường!")
        return True

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Không thể kết nối tới API: {e}")
        print("\nVui lòng kiểm tra:")
        print("  1. Docker containers đang chạy: docker compose ps")
        print("  2. Start services: docker compose up -d")
        return False


def check_pdf_files() -> List[Path]:
    """Kiểm tra PDF files trong folder."""
    print_step(1, "Kiểm tra PDF files")

    if not PDF_DIR.exists():
        print(f"\n⚠️  Thư mục không tồn tại: {PDF_DIR}")
        PDF_DIR.mkdir(parents=True, exist_ok=True)
        print(f"✅ Đã tạo thư mục: {PDF_DIR}")

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    if pdf_files:
        print(f"\n✅ Tìm thấy {len(pdf_files)} file(s) PDF:")
        for i, pdf_file in enumerate(pdf_files, 1):
            size_mb = pdf_file.stat().st_size / (1024 * 1024)
            print(f"  {i}. {pdf_file.name} ({size_mb:.2f} MB)")
    else:
        print(f"\n⚠️  Chưa có PDF nào trong: {PDF_DIR}")
        print("Vui lòng copy PDF files vào folder này!")
        return []

    return pdf_files


def trigger_pdf_processing():
    """Hướng dẫn trigger Airflow DAG để xử lý PDF."""
    print_step(2, "Xử lý PDF files")

    print("\n📝 Để xử lý PDF, vui lòng chọn một trong hai cách:")
    print("\n1️⃣  Sử dụng Airflow UI:")
    print(f"   - Mở: {AIRFLOW_URL}")
    print("   - Login: admin / admin")
    print("   - Tìm DAG: 'pdf_ingestion_dag'")
    print("   - Click nút 'Trigger DAG' (▶️)")

    print("\n2️⃣  Sử dụng CLI:")
    print("   docker exec rag-mcq-airflow airflow dags trigger pdf_ingestion_dag")

    print("\n⏱️  Thời gian xử lý: ~2-5 phút/PDF")
    print("\n📊 Quy trình:")
    print("   → Parse PDF (Docling + GROBID)")
    print("   → Chunk documents (section-aware)")
    print("   → Generate embeddings (768D)")
    print("   → Index to OpenSearch")

    # Hỏi user có muốn đợi không
    input("\n⏸️  Nhấn ENTER sau khi đã trigger DAG và đợi xử lý xong...")


def check_indexed_documents() -> int:
    """Kiểm tra số lượng documents đã được index."""
    print_step(3, "Kiểm tra documents đã index")

    try:
        opensearch_auth = ("admin", "admin")
        response = requests.get(
            "http://localhost:9200/mcq-documents/_count",
            auth=opensearch_auth,
            verify=False,
            timeout=10,
        )

        if response.status_code == 200:
            count = response.json().get("count", 0)
            print(f"\n📄 Số lượng document chunks: {count}")

            if count > 0:
                print("✅ Hệ thống đã sẵn sàng để trả lời câu hỏi!")
            else:
                print("⚠️  Chưa có documents nào. Vui lòng chạy Airflow DAG trước!")

            return count
        else:
            print(f"❌ Lỗi khi query OpenSearch: {response.status_code}")
            return 0

    except Exception as e:
        print(f"❌ Không thể kết nối OpenSearch: {e}")
        return 0


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
        print(f"   Q: {df.iloc[0]['Question'][:100]}...")

        return df

    except Exception as e:
        print(f"❌ Lỗi khi đọc CSV: {e}")
        return None


def ask_single_question(
    question: str, options: Dict[str, str], source_folder: str = None
) -> Dict[str, Any]:
    """Trả lời một câu hỏi MCQ."""

    payload = {"question": question, "options": options, "top_k": TOP_K, "use_hybrid": USE_HYBRID}

    if source_folder and pd.notna(source_folder):
        payload["source_folder"] = source_folder

    try:
        response = requests.post(f"{API_BASE_URL}/api/v1/ask", json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print(f"    ⏱️  Timeout (>{TIMEOUT}s)")
        return {"error": "timeout", "predicted_option": None}

    except Exception as e:
        print(f"    ❌ Lỗi: {str(e)[:100]}")
        return {"error": str(e), "predicted_option": None}


def answer_all_questions(df: pd.DataFrame) -> pd.DataFrame:
    """Trả lời tất cả câu hỏi trong dataframe."""
    print_step(5, "Trả lời câu hỏi")

    results = []
    total = len(df)

    print(f"\n🎯 Bắt đầu trả lời {total} câu hỏi...\n")

    start_time = time.time()

    for idx, row in df.iterrows():
        q_num = idx + 1

        # Progress
        progress = (q_num / total) * 100
        print(f"[{q_num}/{total}] ({progress:.1f}%) ", end="")
        print(f"Q: {row['Question'][:60]}...")

        # Chuẩn bị options
        options = {"A": str(row["A"]), "B": str(row["B"]), "C": str(row["C"]), "D": str(row["D"])}

        # Lấy source_folder nếu có
        source_folder = row.get("source_folder", None)

        # Gọi API
        q_start = time.time()
        answer_data = ask_single_question(
            question=row["Question"], options=options, source_folder=source_folder
        )
        q_time = time.time() - q_start

        # Parse kết quả
        predicted = answer_data.get("predicted_option", "N/A")
        confidence = answer_data.get("confidence", "unknown")
        reasoning = answer_data.get("reasoning", "")
        error = answer_data.get("error", None)

        # Hiển thị kết quả
        conf_icon = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(confidence, "⚪")

        print(f"    → Đáp án: {predicted} {conf_icon} ({q_time:.1f}s)")

        # Lưu kết quả
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
            "reasoning": reasoning[:500] if reasoning else "",  # Giới hạn độ dài
            "processing_time_seconds": round(q_time, 2),
            "error": error if error else "",
            "timestamp": datetime.now().isoformat(),
        }

        # Thêm timing details nếu có
        if "timing" in answer_data:
            timing = answer_data["timing"]
            result["retrieval_time_ms"] = timing.get("retrieval_ms", 0)
            result["generation_time_ms"] = timing.get("generation_ms", 0)

        results.append(result)

        # Ngắt dòng sau mỗi câu
        if q_num % 5 == 0:
            print()

    total_time = time.time() - start_time

    print("\n" + "─" * 80)
    print(f"✅ Hoàn thành! Tổng thời gian: {total_time:.1f}s")
    print(f"⏱️  Trung bình: {total_time / total:.1f}s/câu")
    print("─" * 80)

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
                print(f"  • Câu {row['question_number']}: {row['error'][:50]}")

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
    high_conf = results_df[results_df["confidence"] == "high"].head(5)
    if len(high_conf) > 0:
        print(f"\n🟢 Top {len(high_conf)} câu có độ tin cậy cao:")
        for idx, row in high_conf.iterrows():
            print(
                f"  {row['question_number']}. Đáp án {row['predicted_answer']}: {row['question'][:60]}..."
            )

    # Câu có confidence thấp
    low_conf = results_df[results_df["confidence"] == "low"]
    if len(low_conf) > 0:
        print(f"\n🔴 {len(low_conf)} câu có độ tin cậy thấp:")
        for idx, row in low_conf.head(3).iterrows():
            print(f"  {row['question_number']}. {row['question'][:60]}...")

    print("\n" + "=" * 80)


# =====================================================================
# MAIN FUNCTION
# =====================================================================


def main():
    """Hàm chính để chạy toàn bộ pipeline."""

    print_header("🚀 RAG MCQ SYSTEM - AUTOMATIC ANSWERING")
    print(f"\n📅 Bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 0: Check system health
    if not check_system_health():
        print("\n❌ Hệ thống chưa sẵn sàng. Vui lòng khởi động services trước!")
        return

    # Step 1: Check PDF files
    pdf_files = check_pdf_files()
    if not pdf_files:
        print("\n⚠️  Không có PDF nào để xử lý!")
        proceed = input("Bạn có muốn tiếp tục trả lời câu hỏi không? (y/n): ")
        if proceed.lower() != "y":
            return

    # Step 2: Process PDFs (manual trigger)
    if pdf_files:
        trigger_pdf_processing()

    # Step 3: Check indexed documents
    doc_count = check_indexed_documents()
    if doc_count == 0:
        print("\n❌ Không có documents nào trong hệ thống!")
        print("Không thể trả lời câu hỏi. Vui lòng xử lý PDF trước!")
        return

    # Step 4: Load questions
    questions_df = load_questions()
    if questions_df is None:
        return

    # Step 5: Answer all questions
    results_df = answer_all_questions(questions_df)

    # Step 6: Save results
    save_results(results_df)

    # Display summary
    display_summary(results_df)

    print_header("✅ HOÀN TẤT!")
    print(f"\n📁 Kết quả đã được lưu tại: {OUTPUT_FILE.absolute()}")
    print(f"📅 Kết thúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "=" * 80 + "\n")


# =====================================================================
# ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Đã dừng bởi người dùng (Ctrl+C)")
    except Exception as e:
        print(f"\n\n❌ Lỗi không mong đợi: {e}")
        import traceback

        traceback.print_exc()