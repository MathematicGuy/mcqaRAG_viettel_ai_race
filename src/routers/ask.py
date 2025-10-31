"""
Ask Router - RAG Question Answering API.
Provides endpoints for MCQ answering using RAG pipeline.
"""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.schemas.api import AskRequest, AskResponse, BatchAskRequest, BatchAskResponse
from src.services.factories import (
    make_embeddings_service,
    make_ollama_client,
    make_opensearch_client,
)
from src.services.rag.pipeline import RAGPipeline

logger = logging.getLogger(__name__)

router = APIRouter()


# Dependency injection
def get_rag_pipeline() -> RAGPipeline:
    """Create RAG pipeline with all dependencies."""
    opensearch = make_opensearch_client()
    embeddings = make_embeddings_service()
    ollama = make_ollama_client()

    return RAGPipeline(
        opensearch_client=opensearch,
        embeddings_service=embeddings,
        ollama_client=ollama,
        cache_service=None,  # TODO: Add Redis cache
    )


RAGPipelineDep = Annotated[RAGPipeline, Depends(get_rag_pipeline)]


@router.post("/ask", response_model=AskResponse, summary="Answer MCQ question")
async def ask_question(
    request: AskRequest,
    pipeline: RAGPipelineDep,
) -> AskResponse:
    """
    Answer a multiple choice question using RAG.

    This endpoint:
    1. Retrieves relevant document chunks (hybrid search by default)
    2. Generates answer using LLM with context
    3. Returns predicted option (A/B/C/D) with reasoning

    Args:
        request: Question with options and search parameters
        pipeline: RAG pipeline dependency

    Returns:
        Answer with predicted option, reasoning, confidence, and sources

    Example:
        ```json
        {
            "question": "What is active learning?",
            "options": {
                "A": "A learning method",
                "B": "A machine learning approach",
                "C": "A neural network",
                "D": "A database technique"
            },
            "top_k": 5,
            "use_hybrid": true
        }
        ```
    """
    try:
        logger.info(f"Processing question: {request.question[:100]}...")

        # Validate options
        if not request.options or len(request.options) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least 2 options (A, B) are required",
            )

        # Run RAG pipeline
        result = await pipeline.answer_question(
            question=request.question,
            options=request.options,
            top_k=request.top_k,
            use_hybrid=request.use_hybrid,
            source_folder=request.source_folder,
        )

        # Chắc chắn phải ép kiểu, opensearch làm tôi đau khổ với lỗi này ghê !!! 
        if "sources" in result and isinstance(result["sources"], list):
            for src in result["sources"]:
                if "document_id" in src:
                    src["document_id"] = str(src["document_id"])
                if "chunk_id" in src:
                    src["chunk_id"] = str(src["chunk_id"])
        response = AskResponse(**result)

        logger.info(
            f"Question answered: {response.predicted_option}, "
            f"confidence: {response.confidence}, "
            f"time: {response.timing['total_ms']}ms"
        )

        return response

    except Exception as e:
        logger.error(f"Error processing question: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question: {str(e)}",
        )


@router.post(
    "/ask/batch",
    response_model=BatchAskResponse,
    summary="Answer multiple MCQ questions",
)
async def ask_batch_questions(
    request: BatchAskRequest,
    pipeline: RAGPipelineDep,
) -> BatchAskResponse:
    """
    Answer multiple MCQ questions in batch.

    Processes multiple questions sequentially and returns all results.
    Use this for batch evaluation or processing multiple questions at once.

    Args:
        request: List of questions to answer
        pipeline: RAG pipeline dependency

    Returns:
        Batch results with success/failure counts

    Example:
        ```json
        {
            "questions": [
                {
                    "question": "What is GAN?",
                    "options": {"A": "...", "B": "...", "C": "...", "D": "..."}
                },
                {
                    "question": "What is transformer?",
                    "options": {"A": "...", "B": "...", "C": "...", "D": "..."}
                }
            ]
        }
        ```
    """
    import time

    try:
        logger.info(f"Processing batch of {len(request.questions)} questions")

        start_time = time.time()

        # Process all questions
        questions_data = [
            {
                "question": q.question,
                "options": q.options,
                "top_k": q.top_k,
                "use_hybrid": q.use_hybrid,
                "source_folder": q.source_folder,
            }
            for q in request.questions
        ]

        results = await pipeline.batch_answer_questions(questions_data)

        # Convert to response models
        response_results = [AskResponse(**r) for r in results]

        # Calculate statistics
        successful = sum(1 for r in response_results if r.predicted_option is not None)
        failed = len(response_results) - successful
        total_time = int((time.time() - start_time) * 1000)

        logger.info(
            f"Batch complete: {successful}/{len(request.questions)} successful, "
            f"time: {total_time}ms"
        )

        return BatchAskResponse(
            results=response_results,
            total_questions=len(request.questions),
            successful=successful,
            failed=failed,
            total_time_ms=total_time,
        )

    except Exception as e:
        logger.error(f"Error processing batch: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing batch: {str(e)}",
        )


@router.get("/models", summary="List available LLM models")
async def list_models() -> dict:
    """
    List available Ollama models.

    Returns:
        Dict with available models and current model
    """
    try:
        ollama = make_ollama_client()
        health = ollama.health_check()

        return {
            "current_model": health.get("current_model"),
            "available_models": health.get("available_models", []),
            "status": health.get("status"),
        }

    except Exception as e:
        logger.error(f"Error listing models: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
