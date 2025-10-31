"""
Search Router - Document Search API.
Provides endpoints for searching documents using BM25, Vector, or Hybrid search.
"""

import logging
import time
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.schemas.api import SearchRequest, SearchResponse, SearchHit
from src.services.factories import make_embeddings_service, make_opensearch_client

logger = logging.getLogger(__name__)

router = APIRouter()


# Dependency injection
def get_opensearch():
    """Get OpenSearch client."""
    return make_opensearch_client()


def get_embeddings():
    """Get embeddings service."""
    return make_embeddings_service()


OpenSearchDep = Annotated[object, Depends(get_opensearch)]
EmbeddingsDep = Annotated[object, Depends(get_embeddings)]


@router.post("/", response_model=SearchResponse, summary="Search documents")
async def search_documents(
    request: SearchRequest,
    opensearch: OpenSearchDep,
    embeddings: EmbeddingsDep,
) -> SearchResponse:
    """
    Search documents using BM25, Vector, or Hybrid search.

    **Search Modes:**
    - `use_hybrid=false`: BM25 keyword search only (faster)
    - `use_hybrid=true`: Hybrid RRF fusion of BM25 + Vector (better quality)

    **Use Cases:**
    - BM25: Exact keywords, technical terms, specific names
    - Hybrid: Conceptual queries, paraphrased questions, semantic search

    Args:
        request: Search request with query and parameters
        opensearch: OpenSearch client
        embeddings: Embeddings service

    Returns:
        Search results with relevant chunks

    Example:
        ```json
        {
            "query": "active learning in medical imaging",
            "top_k": 5,
            "use_hybrid": true,
            "source_folder": "train_fix"
        }
        ```
    """
    try:
        start_time = time.time()

        logger.info(
            f"Search: query='{request.query[:50]}...', "
            f"top_k={request.top_k}, hybrid={request.use_hybrid}"
        )

        # Execute search based on mode
        if request.use_hybrid:
            # Generate query embedding
            query_embedding = await embeddings.embed_query(request.query)

            # Hybrid search
            results = await opensearch.search_hybrid(
                query=request.query,
                query_embedding=query_embedding.tolist(),
                top_k=request.top_k,
                source_folder=request.source_folder,
            )
            search_mode = "hybrid"

        else:
            # BM25 only
            results = await opensearch.search_bm25(
                query=request.query,
                top_k=request.top_k,
                source_folder=request.source_folder,
                min_score=request.min_score,
            )
            search_mode = "bm25"

        # Convert to response format
        hits = [
            SearchHit(**{
                **result,
                "document_id": str(result["document_id"]),
                "chunk_id": str(result["chunk_id"]),
            })
            for result in results
        ]

        timing_ms = int((time.time() - start_time) * 1000)

        logger.info(f"Search complete: {len(hits)} results, {timing_ms}ms, mode={search_mode}")

        return SearchResponse(
            query=request.query,
            total=len(hits),
            hits=hits,
            search_mode=search_mode,
            timing_ms=timing_ms,
        )

    except Exception as e:
        logger.error(f"Search error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Search failed: {str(e)}",
        )


@router.get("/health", summary="Check search service health")
async def search_health(opensearch: OpenSearchDep) -> dict:
    """
    Check search service health.

    Returns:
        Health status of OpenSearch and index information
    """
    try:
        health = opensearch.health_check()
        doc_count = await opensearch.get_document_count()

        return {
            "status": "healthy" if health.get("status") == "green" else "degraded",
            "opensearch": health,
            "document_count": doc_count,
            "index_name": opensearch.index_name,
        }

    except Exception as e:
        logger.error(f"Health check error: {e}")
        return {
            "status": "unhealthy",
            "error": str(e),
        }
