"""
Ollama LLM client for answer generation.
Supports multiple models and streaming responses.
"""

import json
import logging
from typing import AsyncGenerator, Dict, List, Optional

import httpx

logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Ollama LLM client for MCQ answer generation.
    Supports local inference with configurable models.
    """

    def __init__(
        self,
        host: str = "http://localhost:11434",
        model: str = "llama3.2:3b",
        temperature: float = 0.1,
        max_response_words: int = 500,
        timeout: int = 120,
    ):
        """
        Initialize Ollama client.

        Args:
            host: Ollama server host
            model: Model name to use
            temperature: Temperature for generation (0.0-1.0)
            max_response_words: Maximum words in response
            timeout: Request timeout in seconds
        """
        self.host = host.rstrip("/")
        self.model = model
        self.temperature = temperature
        self.max_response_words = max_response_words
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

        self.logger.info(f"Ollama client initialized: {host}, model: {model}")

    async def generate_mcq_answer(
        self,
        question: str,
        options: Dict[str, str],
        context_chunks: List[Dict],
    ) -> Dict:
        """
        Generate answer for multiple choice question.

        Args:
            question: Question text
            options: Dict of options {"A": "text", "B": "text", ...}
            context_chunks: List of retrieved chunks

        Returns:
            Dict with answer, reasoning, confidence
        """
        # Build prompt
        prompt = self._build_mcq_prompt(question, options, context_chunks)

        # Generate response
        try:
            response = await self._generate(prompt)
            answer_text = response.get("response", "")

            # Parse response
            parsed = self._parse_mcq_response(answer_text)

            return {
                "answer_text": answer_text,
                "predicted_option": parsed["option"],
                "reasoning": parsed["reasoning"],
                "confidence": parsed["confidence"],
                "model": self.model,
            }

        except Exception as e:
            self.logger.error(f"Error generating MCQ answer: {e}", exc_info=True)
            return {
                "answer_text": f"Error: {str(e)}",
                "predicted_option": None,
                "reasoning": "Failed to generate answer",
                "confidence": "low",
                "model": self.model,
            }

    def _build_mcq_prompt(
        self,
        question: str,
        options: Dict[str, str],
        chunks: List[Dict],
    ) -> str:
        """Build optimized prompt for MCQ answering."""
        # System instruction
        system = """
SYSTEM INSTRUCTION:
Bạn là một trợ lý AI chuyên trả lời câu hỏi trắc nghiệm dựa trên context được cung cấp.
Mục tiêu của bạn là sử dụng context được cung cấp để chọn tất cả đáp án đúng (có thể có nhiều đáp án đúng) và giải thích ngắn gọn lý do.

---

NHIỆM VỤ:
1. Đọc kỹ context.
2. Phân tích câu hỏi và 4 options (A, B, C, D).
3. Xác định tất cả đáp án đúng và sai dựa trên context.
4. Giải thích ngắn gọn vì sao các đáp án đó đúng.
5. Giải thích ngắn gọn vì sao các đáp án còn lại sai.
6. Đánh giá độ tự tin với kết quả.

---

ĐỊNH DẠNG TRẢ LỜI BẮT BUỘC:
ANSWER: [Danh sách đáp án đúng, ví dụ: A,C hoặc B hoặc A,B,C]
REASONING: [Giải thích ngắn gọn dựa trên context, tối đa 2-3 câu cho mỗi option]
CONFIDENCE: [high / medium / low]

---

VÍ DỤ VỀ ĐỊNH DẠNG TRẢ LỜI:
ANSWER: A, C
REASONING:
- Các đáp án đúng:
A. [Giải thích ngắn gọn vì sao A đúng]
C. [Giải thích ngắn gọn vì sao C đúng]
- Các đáp án sai:
B. [Giải thích ngắn gọn vì sao B sai]
D. [Giải thích ngắn gọn vì sao D sai]
CONFIDENCE: high
---

LƯU Ý:
- Sử dụng triệt để thông tin từ context kết hợp kiến thức sẵn có để suy luận câu trả lời tốt nhất.
- KHÔNG ĐƯỢC BỊA THÊM DỮ LIỆU HOẶC SỰ KIỆN KHÔNG CÓ TRONG CONTEXT.
- Luôn tuân thủ format đầu ra và KHÔNG BAO GIỜ TRẢ VỀ "none" trong mục ANSWER.
"""

        few_shot_examples = """
---
FEW-SHOT EXAMPLE 1:
Đây là ví dụ về một câu hỏi với **một đáp án đúng**

NGỮ CẢNH TỪ TÀI LIỆU:
[Tài liệu 1 - Giới thiệu về IPv4]
IPv4 sử dụng địa chỉ 32-bit, cho phép khoảng 4.3 tỷ địa chỉ duy nhất. Nó là phiên bản thứ tư của Giao thức Internet và được sử dụng rộng rãi.

CÂU HỎI:
Đâu là đặc điểm chính xác của giao thức IPv4?

CÁC LỰA CHỌN:
A. IPv4 sử dụng địa chỉ 128-bit.
B. IPv4 sử dụng địa chỉ 32-bit.
C. IPv4 hỗ trợ mã hóa end-to-end mặc định.
D. IPv4 có không gian địa chỉ gần như vô hạn.

TRẢ LỜI:
ANSWER: B
REASONING:
- Các đáp án đúng:
B. Tài liệu 1 nêu rõ "IPv4 sử dụng địa chỉ 32-bit".
- Các đáp án sai:
A. Sai, tài liệu 1 chỉ ra IPv4 sử dụng 32-bit, không phải 128-bit.
C. Sai, context không đề cập IPv4 có mã hóa end-to-end mặc định.
D. Sai, không gian địa chỉ IPv4 là hữu hạn (khoảng 4.3 tỷ địa chỉ).
CONFIDENCE: high

---
FEW-SHOT EXAMPLE 2:
Đây là ví dụ về một câu hỏi với **nhiều đáp án đúng**

NGỮ CẢNH TỪ TÀI LIỆU:
[Tài liệu 1 - Mạng diện rộng (WAN)]
Mạng WAN (Wide Area Network) kết nối các mạng LAN qua các khoảng cách địa lý rộng lớn, thường sử dụng các đường truyền thuê bao (leased lines) hoặc công nghệ VPN để liên kết các văn phòng, chi nhánh ở các thành phố hoặc quốc gia khác nhau. Tốc độ có thể khác nhau tùy thuộc vào công nghệ được sử dụng.
[Tài liệu 2 - So sánh LAN và WAN]
Không giống như LAN có tốc độ rất cao trong phạm vi nhỏ, WAN tập trung vào khả năng mở rộng và kết nối xa.

CÂU HỎI:
Các đặc điểm nào sau đây thường liên quan đến mạng WAN?

CÁC LỰA CHỌN:
A. Kết nối các khu vực địa lý rộng lớn.
B. Tốc độ truyền tải dữ liệu rất cao (Gbps trở lên) trong phạm vi nhỏ.
C. Sử dụng các đường truyền thuê bao hoặc VPN.
D. Có thể liên kết nhiều mạng LAN lại với nhau.

TRẢ LỜI:
ANSWER: A, C, D
REASONING:
- Các đáp án đúng:
A. Tài liệu 1 nói "kết nối các mạng LAN qua các khoảng cách địa lý rộng lớn".
C. Tài liệu 1 đề cập "thường sử dụng các đường truyền thuê bao (leased lines) hoặc công nghệ VPN".
D. Tài liệu 1 nói "liên kết các văn phòng, chi nhánh ở các thành phố hoặc quốc gia khác nhau", ngụ ý liên kết nhiều mạng LAN.
- Các đáp án sai:
B. Tài liệu 2 chỉ ra rằng tốc độ rất cao trong phạm vi nhỏ là đặc điểm của LAN, không phải WAN.
CONFIDENCE: high

---
FEW-SHOT EXAMPLE 3:
Đây là ví dụ về một câu hỏi mà **context hoàn toàn không cung cấp bất kì thông tin gì liên quan đến options** để có thể sử dụng làm cơ sở suy luận

NGỮ CẢNH TỪ TÀI LIỆU:
[Tài liệu 1 - Phương pháp Agile]
Agile là một tập hợp các phương pháp phát triển phần mềm lặp đi lặp lại và tăng dần. Agile khuyến khích lập kế hoạch thích ứng, phát triển tiến hóa, phân phối sớm, cải tiến liên tục và khuyến khích phản ứng linh hoạt với sự thay đổi. Nó tập trung vào sự hợp tác giữa các nhóm tự tổ chức và khách hàng.

CÂU HỎI:
Công cụ nào sau đây là tốt nhất để quản lý dự án theo mô hình Waterfall?

CÁC LỰA CHỌN:
A. Jira
B. Trello
C. Azure DevOps
D. Microsoft Project

TRẢ LỜI:
ANSWER: D
REASONING:
- Các đáp án đúng:
D. Microsoft Project là công cụ truyền thống phù hợp với việc lập kế hoạch tuần tự, chi tiết của mô hình Waterfall.
- Các đáp án sai:
A. Jira, B. Trello, C. Azure DevOps (khi dùng cho Agile) thường được sử dụng cho các phương pháp Agile, không phải Waterfall. Context không cung cấp thông tin về công cụ quản lý dự án cho Waterfall.
CONFIDENCE: low

---
FEW-SHOT EXAMPLE 4:
Đây là ví dụ về một câu hỏi yêu cầu **tính toán, áp dụng công thức/phương pháp từ context** vào một bài tập mới.

NGỮ CẢNH TỪ TÀI LIỆU:
[Tài liệu 1 - Tính Chỉ số BMI]
Chỉ số khối cơ thể (BMI) được tính bằng công thức: `BMI = cân nặng (kg) / (chiều cao (m))^2`.
Ví dụ: Một người nặng 70kg cao 1.75m có BMI = 70 / (1.75 * 1.75) = 22.86.

CÂU HỎI:
Một người nặng 80kg và cao 1.80m sẽ có chỉ số BMI là bao nhiêu?

CÁC LỰA CHỌN:
A. 23.56
B. 24.69
C. 25.12
D. 26.05

TRẢ LỜI:
ANSWER: B
REASONING:
- Các đáp án đúng:
B. Áp dụng công thức từ Tài liệu 1: BMI = 80kg / (1.80m * 1.80m) = 80 / 3.24 = 24.69.
- Các đáp án sai:
A, C, D. Các giá trị này không khớp với kết quả tính toán từ công thức đã cho.
CONFIDENCE: high

---
FEW-SHOT EXAMPLE 5:
Đây là ví dụ về một câu hỏi yêu cầu **tóm tắt nội dung chính** từ một phần nào đó trong tài liệu cụ thể

NGỮ CẢNH TỪ TÀI LIỆU:
[Tài liệu 1 - Các giai đoạn phát triển phần mềm]
1. Phân tích yêu cầu: Thu thập và ghi lại các yêu cầu từ khách hàng.
2. Thiết kế: Lập kế hoạch kiến trúc hệ thống và giao diện người dùng.
3. Triển khai: Viết mã nguồn dựa trên thiết kế.
4. Kiểm thử: Đảm bảo phần mềm hoạt động đúng theo yêu cầu.
5. Triển khai và bảo trì: Đưa phần mềm vào sử dụng và hỗ trợ sau này.

[Tài liệu 2 - Vai trò của kiểm thử]
Kiểm thử phần mềm là quá trình đánh giá và xác minh rằng một sản phẩm hoặc ứng dụng phần mềm thực hiện đúng như mong đợi. Lợi ích chính của kiểm thử là xác định lỗi hoặc thiếu sót.

CÂU HỎI:
Nội dung chính của Tài liệu 2 là gì?

CÁC LỰA CHỌN:
A. Các bước chính trong vòng đời phát triển phần mềm.
B. Định nghĩa và lợi ích của việc kiểm thử phần mềm.
C. Cách thu thập yêu cầu từ khách hàng.
D. Hướng dẫn viết mã hiệu quả.

TRẢ LỜI:
ANSWER: B
REASONING:
- Các đáp án đúng:
B. Tài liệu 2 tập trung vào việc định nghĩa kiểm thử phần mềm ("quá trình đánh giá và xác minh...") và lợi ích chính của nó ("xác định lỗi hoặc thiếu sót").
- Các đáp án sai:
A. Đây là nội dung của Tài liệu 1, không phải Tài liệu 2.
C. Đây là một phần của giai đoạn phân tích yêu cầu, không phải nội dung chính của Tài liệu 2.
D. Tài liệu 2 không đề cập đến hướng dẫn viết mã.
CONFIDENCE: high
"""
        # Context from chunks
        context_parts = []
        for i, chunk in enumerate(chunks):
            chunk_text = chunk.get("chunk_text", "")
            section = chunk.get("section_name", "Unknown")
            context_parts.append(f"[Tài liệu {i + 1} - {section}]\n{chunk_text}")

        context = "\n\n".join(context_parts)

        # Options formatting
        options_text = "\n".join([f"{key}. {value}" for key, value in options.items()])

        # Complete prompt
        prompt = f"""{system}
{few_shot_examples}
### NGỮ CẢNH TỪ TÀI LIỆU:
{context}

### CÂU HỎI:
{question}

### CÁC LỰA CHỌN:
{options_text}

### TRẢ LỜI (theo đúng format bên trên):"""

        return prompt

    def _parse_mcq_response(self, response: str) -> Dict:
        """Parse LLM response to extract answer."""
        result = {
            "option": None,
            "reasoning": "",
            "confidence": "medium",
        }

        lines = response.strip().split("\n")

        for line in lines:
            line = line.strip()

            if line.startswith("ANSWER:"):
                # Extract A, B, C, or D
                answer_part = line.split(":", 1)[-1].strip()
                # Look for A, B, C, or D in the answer
                for char in ["A", "B", "C", "D"]:
                    if char in answer_part.upper():
                        result["option"] = char
                        break

            elif line.startswith("REASONING:"):
                result["reasoning"] = line.split(":", 1)[-1].strip()

            elif line.startswith("CONFIDENCE:"):
                confidence = line.split(":", 1)[-1].strip().lower()
                if confidence in ["high", "medium", "low"]:
                    result["confidence"] = confidence

        # If no option found, try to extract from beginning of response
        if not result["option"]:
            for char in ["A", "B", "C", "D"]:
                if response.upper().startswith(char):
                    result["option"] = char
                    break

        return result

    async def _generate(self, prompt: str) -> Dict:
        """
        Call Ollama generate API.

        Args:
            prompt: Prompt text

        Returns:
            Response dict
        """
        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_response_words * 2,  # Words to tokens approximation
            },
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return response.json()

    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        """
        Stream tokens as they are generated.

        Args:
            prompt: Prompt text

        Yields:
            Generated tokens
        """
        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_response_words * 2,
            },
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            async with client.stream("POST", url, json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        try:
                            data = json.loads(line)
                            if "response" in data:
                                yield data["response"]
                        except json.JSONDecodeError:
                            continue

    async def check_model(self) -> bool:
        """
        Check if model is available.

        Returns:
            True if model exists
        """
        try:
            url = f"{self.host}/api/tags"
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.get(url)
                response.raise_for_status()
                data = response.json()

                models = data.get("models", [])
                model_names = [m.get("name") for m in models]

                return self.model in model_names

        except Exception as e:
            self.logger.error(f"Error checking model: {e}")
            return False

    def health_check(self) -> Dict:
        """
        Check Ollama server health.

        Returns:
            Health status dict
        """
        try:
            import requests

            response = requests.get(f"{self.host}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                models = [m.get("name") for m in data.get("models", [])]
                return {
                    "status": "healthy",
                    "host": self.host,
                    "available_models": models,
                    "current_model": self.model,
                    "model_available": self.model in models,
                }
            else:
                return {"status": "unhealthy", "error": "Cannot connect to Ollama"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
