import csv
import requests
import json

# Thay đổi URL này nếu API của bạn chạy ở một địa chỉ khác
API_URL = "http://localhost:8000/api/v1/ask"

def load_questions_from_csv(csv_file):
    """
    Đọc dữ liệu câu hỏi và lựa chọn từ file CSV.

    Args:
        csv_file (str): Đường dẫn đến file CSV.

    Returns:
        list: Danh sách các dictionary, mỗi dictionary đại diện cho một câu hỏi và các lựa chọn của nó.
              Trả về danh sách rỗng nếu có lỗi xảy ra.
    """
    questions_data = []
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            # Kiểm tra xem các cột cần thiết có tồn tại không
            required_columns = ["Question", "A", "B", "C", "D"]
            if not all(col in csv_reader.fieldnames for col in required_columns):
                print(f"Lỗi: File CSV phải chứa các cột: {', '.join(required_columns)}")
                return []

            for row in csv_reader:
                question = row["Question"]
                options = {
                    "option_a": row["A"],
                    "option_b": row["B"],
                    "option_c": row["C"],
                    "option_d": row["D"]
                }
                questions_data.append({"question": question, "options": options})
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{csv_file}'")
        return []
    except Exception as e:
        print(f"Lỗi khi đọc file CSV: {e}")
        return []
    return questions_data

def call_ask_api(question_data):
    """
    Gọi API /v1/ask với dữ liệu câu hỏi và các lựa chọn.

    Args:
        question_data (dict): Dictionary chứa 'question' và 'options'.

    Returns:
        dict: Kết quả trả về từ API, hoặc None nếu có lỗi.
    """
    payload = {
        "question": question_data["question"],
        "options": question_data["options"]
        # Nếu API của bạn yêu cầu thêm trường 'context_chunks', bạn cần thêm nó vào đây.
        # Ví dụ: "context_chunks": retrieved_context
    }
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gọi API: {e}")
        # In ra chi tiết lỗi nếu có thể, ví dụ:
        if hasattr(e, 'response') and e.response is not None:
            try:
                print(f"Chi tiết lỗi từ server: {e.response.json()}")
            except json.JSONDecodeError:
                print(f"Chi tiết lỗi từ server (không phải JSON): {e.response.text}")
        return None

def main():
    """
    Hàm chính để chạy script.
    """
    csv_file_path = "data/q.csv"
    questions = load_questions_from_csv(csv_file_path)

    if not questions:
        print("Không có câu hỏi nào để xử lý. Thoát script.")
        return

    for i, q_data in enumerate(questions):
        print(f"\n--- Đang xử lý câu hỏi {i+1}/{len(questions)} ---")
        print(f"Câu hỏi: {q_data['question']}")
        print(f"Các lựa chọn: {q_data['options']}")

        api_response = call_ask_api(q_data)

        if api_response:
            print("\n--- Kết quả từ API ---")
            # In ra toàn bộ response để bạn có thể xem cấu trúc
            print(json.dumps(api_response, indent=2, ensure_ascii=False))

            # Trích xuất và in ra các thông tin quan trọng nếu có
            predicted_option = api_response.get("predicted_option", "N/A")
            reasoning = api_response.get("reasoning", "N/A")
            confidence = api_response.get("confidence", "N/A")

            print(f"Lựa chọn dự đoán: {predicted_option}")
            print(f"Lý giải: {reasoning}")
            print(f"Độ tự tin: {confidence}")
        else:
            print("Không nhận được phản hồi hợp lệ từ API.")

if __name__ == "__main__":
    main()