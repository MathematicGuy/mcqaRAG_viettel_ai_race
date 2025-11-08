"""
RAG Pipeline Orchestrator.
Coordinates retrieval and generation for MCQ answering.
"""

import logging
import time
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class RAGPipeline:
    """
    Complete RAG pipeline orchestration.
    Coordinates retrieval (OpenSearch) and generation (Ollama).
    """

    def __init__(
        self,
        opensearch_client,
        embeddings_service,
        ollama_client,
        cache_service=None,
    ):
        """
        Initialize RAG pipeline.

        Args:
            opensearch_client: OpenSearch client for retrieval
            embeddings_service: Embeddings service for query encoding
            ollama_client: Ollama client for answer generation
            cache_service: Optional Redis cache service
        """
        self.opensearch = opensearch_client
        self.embeddings = embeddings_service
        self.ollama = ollama_client
        self.cache = cache_service
        self.logger = logging.getLogger(__name__)

    async def answer_question(
        self,
        question: str,
        options: Dict[str, str],
        top_k: int = 15,
        use_hybrid: bool = True,
        source_folder: Optional[str] = None,
    ) -> Dict:
        """
        Complete RAG pipeline for MCQ answering.

        Args:
            question: Question text
            options: Dict of options {"A": "text", "B": "text", ...}
            top_k: Number of chunks to retrieve
            use_hybrid: Use hybrid search (BM25 + Vector)
            source_folder: Filter by source folder

        Returns:
            Dict with answer, sources, timing, search mode
        """
        start_time = time.time()

        # 1. Check cache if available
        cache_key = None
        if self.cache:
            cache_key = self._generate_cache_key(question, options, top_k, use_hybrid)
            cached = await self._check_cache(cache_key)
            if cached:
                self.logger.info(f"Cache hit for question: {question[:50]}...")
                cached["from_cache"] = True
                return cached

        # 2. Retrieval phase
        retrieval_start = time.time()
        # # tạo câu truy vấn kết hợp cả question và options để sử dụng thông tin từ options
        # options_text = ""
        options_list = [f"- {value}" for key, value in sorted(options.items())]
        options_text = "\n".join(options_list)
        combined_query = f"{question}\n{options_text}" # Nối câu hỏi và options với xuống dòng
        self.logger.info(f"Using combined query for retrieval: {combined_query}")

        try:
            if use_hybrid:
                # Generate query embedding
                query_embedding = await self.embeddings.embed_query(combined_query)

                # Hybrid search (BM25 + Vector)
                chunks = await self.opensearch.search_hybrid(
                    query=combined_query,
                    query_embedding=query_embedding.tolist(),
                    top_k=top_k,
                    source_folder=source_folder,
                )
                search_mode = "hybrid"
            else:
                # BM25 only
                chunks = await self.opensearch.search_bm25(
                    query=combined_query,
                    top_k=top_k,
                    source_folder=source_folder,
                )
                search_mode = "bm25"

            retrieval_time = int((time.time() - retrieval_start) * 1000)

            if not chunks:
                self.logger.warning(f"No chunks retrieved for question: {combined_query}")
                return {
                    "question": question,
                    "options": options,
                    "predicted_option": None,
                    "answer_text": "Không tìm thấy tài liệu liên quan để trả lời câu hỏi.",
                    "reasoning": "No relevant documents found",
                    "confidence": "low",
                    "sources": [],
                    "search_mode": search_mode,
                    "timing": {
                        "total_ms": int((time.time() - start_time) * 1000),
                        "retrieval_ms": retrieval_time,
                        "generation_ms": 0,
                    },
                    "from_cache": False,
                }

        except Exception as e:
            self.logger.error(f"Retrieval error: {e}", exc_info=True)
            return self._error_response(question, options, str(e), start_time)

        # 3. Generation phase
        generation_start = time.time()

        try:
            response = await self.ollama.generate_mcq_answer(
                question=question,
                options=options,
                context_chunks=chunks,
            )

            generation_time = int((time.time() - generation_start) * 1000)

        except Exception as e:
            self.logger.error(f"Generation error: {e}", exc_info=True)
            return self._error_response(question, options, str(e), start_time, retrieval_time)

        # 4. Compile result
        result = {
            "question": question,
            "options": options,
            "predicted_option": response["predicted_option"],
            "answer_text": response["answer_text"],
            "reasoning": response["reasoning"],
            "confidence": response["confidence"],
            "sources": self._format_sources(chunks),
            "search_mode": search_mode,
            "model": response["model"],
            "timing": {
                "total_ms": int((time.time() - start_time) * 1000),
                "retrieval_ms": retrieval_time,
                "generation_ms": generation_time,
            },
            "from_cache": False,
        }

        # 5. Cache result if available
        if self.cache and cache_key:
            await self._store_cache(cache_key, result)

        return result

    def _format_sources(self, chunks: List[Dict]) -> List[Dict]:
        """Format chunks as sources."""
        sources = []
        seen_docs = set()

        for chunk in chunks:
            doc_id = chunk.get("document_id")
            if doc_id and doc_id not in seen_docs:
                sources.append(
                    {
                        "document_id": doc_id,
                        "chunk_id": chunk.get("chunk_id"),
                        "section_name": chunk.get("section_name"),
                        "score": chunk.get("score", chunk.get("fusion_score", 0)),
                        "preview": chunk.get("chunk_text", "")[:200] + "...",
                    }
                )
                seen_docs.add(doc_id)

        return sources

    def _generate_cache_key(
        self,
        question: str,
        options: Dict[str, str],
        top_k: int,
        use_hybrid: bool,
    ) -> str:
        """Generate cache key for question."""
        import hashlib

        # Create deterministic string from inputs
        key_parts = [
            question,
            str(sorted(options.items())),
            str(top_k),
            str(use_hybrid),
        ]
        key_string = "|".join(key_parts)

        # Hash to fixed length
        return hashlib.sha256(key_string.encode()).hexdigest()

    async def _check_cache(self, cache_key: str) -> Optional[Dict]:
        """Check if result is cached."""
        if not self.cache:
            return None

        try:
            return await self.cache.get(cache_key)
        except Exception as e:
            self.logger.warning(f"Cache check failed: {e}")
            return None

    async def _store_cache(self, cache_key: str, result: Dict):
        """Store result in cache."""
        if not self.cache:
            return

        try:
            await self.cache.set(cache_key, result)
        except Exception as e:
            self.logger.warning(f"Cache store failed: {e}")

    def _error_response(
        self,
        question: str,
        options: Dict[str, str],
        error: str,
        start_time: float,
        retrieval_time: int = 0,
    ) -> Dict:
        """Generate error response."""
        return {
            "question": question,
            "options": options,
            "predicted_option": None,
            "answer_text": f"Lỗi khi xử lý câu hỏi: {error}",
            "reasoning": "System error",
            "confidence": "low",
            "sources": [],
            "search_mode": "error",
            "timing": {
                "total_ms": int((time.time() - start_time) * 1000),
                "retrieval_ms": retrieval_time,
                "generation_ms": 0,
            },
            "from_cache": False,
            "error": error,
        }

    async def batch_answer_questions(
        self,
        questions: List[Dict],
        **kwargs,
    ) -> List[Dict]:
        """
        Answer multiple questions in batch.

        Args:
            questions: List of question dicts with 'question' and 'options'
            **kwargs: Additional arguments for answer_question

        Returns:
            List of answers
        """
        results = []

        for i, q in enumerate(questions):
            self.logger.info(f"Processing question {i + 1}/{len(questions)}")

            try:
                result = await self.answer_question(
                    question=q["question"],
                    options=q["options"],
                    **kwargs,
                )
                results.append(result)
            except Exception as e:
                self.logger.error(f"Error processing question {i + 1}: {e}")
                results.append(
                    self._error_response(
                        q["question"],
                        q["options"],
                        str(e),
                        time.time(),
                    )
                )

        return results
