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
Mục tiêu của bạn là chọn tất cả đáp án đúng (có thể một hoặc nhiều) dựa trên context và giải thích ngắn gọn (2-3 câu).

---

NHIỆM VỤ:
1. Đọc kỹ context.
2. Phân tích câu hỏi và 4 lựa chọn (A, B, C, D).
3. Xác định tất cả đáp án đúng dựa trên context.
4. Giải thích ngắn gọn vì sao các đáp án đó đúng.
5. Đánh giá độ tự tin với kết quả.

---

ĐỊNH DẠNG TRẢ LỜI BẮT BUỘC:
ANSWER: [Danh sách đáp án đúng, ví dụ: A,C hoặc B hoặc A,B,C hoặc none]
REASONING: [Giải thích ngắn gọn dựa trên context, tối đa 2-3 câu]
CONFIDENCE: [high / medium / low]

---

FEW-SHOT EXAMPLES

Ví dụ 1 — 1 đáp án đúng:
Context: Nước sôi ở 100°C ở áp suất tiêu chuẩn.
Question: Ở điều kiện bình thường, nước sôi ở bao nhiêu độ C?
Options:
A. 90°C
B. 100°C
C. 120°C
D. 0°C

ANSWER: B
REASONING: Context cho biết nước sôi ở 100°C, trùng với lựa chọn B.
CONFIDENCE: high

---

Ví dụ 2 — 2 đáp án đúng:
Context: Vitamin C và Vitamin E đều là chất chống oxy hóa giúp bảo vệ tế bào.
Question: Dưới đây, những vitamin nào là chất chống oxy hóa?
Options:
A. Vitamin A
B. Vitamin B12
C. Vitamin C
D. Vitamin E

ANSWER: C,D
REASONING: Context nêu rõ Vitamin C và E là chất chống oxy hóa. Hai lựa chọn này đúng.
CONFIDENCE: high

---

Ví dụ 3 — 3 đáp án đúng:
Context: Hệ Mặt Trời gồm Mặt Trời và các hành tinh: Sao Thủy, Sao Kim, Trái Đất, Sao Hỏa, Sao Mộc, Sao Thổ, Sao Thiên Vương, Sao Hải Vương.
Question: Những hành tinh nào thuộc Hệ Mặt Trời?
Options:
A. Sao Hỏa
B. Sao Kim
C. Sao Diêm Vương
D. Sao Mộc

ANSWER: A,B,D
REASONING: Context liệt kê A, B, D thuộc Hệ Mặt Trời; Sao Diêm Vương không còn được tính là hành tinh.
CONFIDENCE: high

---

Ví dụ 4 — Không đủ thông tin (CONFIDENCE: low):
Context: Einstein là một nhà vật lý nổi tiếng thế kỷ 20.
Question: Einstein đã nhận giải Nobel Hòa bình năm nào?
Options:
A. 1921
B. 1922
C. 1930
D. Không có thông tin

ANSWER: none
REASONING: Context chỉ nói Einstein là nhà vật lý, không đề cập giải Nobel Hòa bình.
CONFIDENCE: low

---

Ví dụ 5 — Context mơ hồ (CONFIDENCE: medium):
Context: Một số loài chim có thể bay ở độ cao trên 3000 mét.
Question: Loài nào chắc chắn có thể bay ở độ cao trên 3000 mét?
Options:
A. Đại bàng
B. Chim cánh cụt
C. Vịt trời
D. Không có thông tin rõ ràng

ANSWER: A,C
REASONING: Context nói "một số loài chim" có thể bay cao, A và C hợp lý nhưng không chắc chắn hoàn toàn.
CONFIDENCE: medium

---

LƯU Ý:
- Sử dụng triệt để thông tin từ context kết hợp kiến thức sẵn có để suy luận đáp án tốt nhất
- Nếu không có thông tin để xác định, trả lời ANSWER: none và CONFIDENCE: low.
- Luôn tuân thủ format đầu ra, không thêm bất kỳ văn bản nào khác.
"""

        # Context from chunks (top 5 only for efficiency)
        context_parts = []
        for i, chunk in enumerate(chunks[:5]):
            chunk_text = chunk.get("chunk_text", "")
            section = chunk.get("section_name", "Unknown")
            context_parts.append(f"[Tài liệu {i + 1} - {section}]\n{chunk_text[:800]}")

        context = "\n\n".join(context_parts)

        # Options formatting
        options_text = "\n".join([f"{key}. {value}" for key, value in options.items()])

        # Complete prompt
        prompt = f"""{system}

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
