"""
Health Check Router.
Provides comprehensive health checks for all system services.
"""

import logging
from typing import Dict

from fastapi import APIRouter

from src.config import get_settings
from src.services.factories import (
    make_embeddings_service,
    make_ollama_client,
    make_opensearch_client,
)

logger = logging.getLogger(__name__)

router = APIRouter()

settings = get_settings()


@router.get("/health", summary="System health check")
async def health_check() -> Dict:
    """
    Comprehensive system health check.

    Checks the health of all services:
    - API service
    - PostgreSQL database
    - OpenSearch cluster
    - Redis cache
    - Ollama LLM service
    - Embeddings model

    Returns:
        Dict with status of all services and configuration
    """
    health_status = {
        "status": "healthy",
        "environment": settings.environment,
        "services": {},
        "configuration": {},
    }

    # Check OpenSearch
    try:
        opensearch = make_opensearch_client()
        os_health = opensearch.health_check()
        doc_count = await opensearch.get_document_count()

        health_status["services"]["opensearch"] = {
            "status": "healthy" if os_health.get("status") == "green" else "degraded",
            "cluster_status": os_health.get("status"),
            "index_exists": os_health.get("index_exists", False),
            "document_count": doc_count,
        }
    except Exception as e:
        logger.error(f"OpenSearch health check failed: {e}")
        health_status["services"]["opensearch"] = {
            "status": "unhealthy",
            "error": str(e),
        }
        health_status["status"] = "degraded"

    # Check Ollama
    try:
        ollama = make_ollama_client()
        ollama_health = ollama.health_check()

        health_status["services"]["ollama"] = {
            "status": ollama_health.get("status"),
            "model": ollama_health.get("current_model"),
            "model_available": ollama_health.get("model_available", False),
            "available_models": ollama_health.get("available_models", []),
        }

        if ollama_health.get("status") != "healthy":
            health_status["status"] = "degraded"

    except Exception as e:
        logger.error(f"Ollama health check failed: {e}")
        health_status["services"]["ollama"] = {
            "status": "unhealthy",
            "error": str(e),
        }
        health_status["status"] = "degraded"

    # Check Embeddings
    try:
        embeddings = make_embeddings_service()
        model_info = embeddings.get_model_info()

        health_status["services"]["embeddings"] = {
            "status": "healthy",
            "model": model_info["model_name"],
            "dimensions": model_info["dimensions"],
            "device": model_info["device"],
        }
    except Exception as e:
        logger.error(f"Embeddings health check failed: {e}")
        health_status["services"]["embeddings"] = {
            "status": "unhealthy",
            "error": str(e),
        }
        health_status["status"] = "degraded"

    # PostgreSQL check (basic)
    health_status["services"]["postgres"] = {
        "status": "unknown",
        "host": settings.postgres.host,
        "database": settings.postgres.database,
        "note": "Database connectivity check not implemented",
    }

    # Redis check (basic)
    health_status["services"]["redis"] = {
        "status": "unknown",
        "enabled": settings.redis.enabled,
        "host": settings.redis.host,
        "note": "Redis connectivity check not implemented",
    }

    # Configuration summary
    health_status["configuration"] = {
        "embedding_model": settings.embeddings.model_name,
        "embedding_dimensions": settings.embeddings.dimensions,
        "chunk_size": settings.chunking.chunk_size,
        "chunk_overlap": settings.chunking.overlap_size,
        "search_top_k_default": settings.search.top_k_default,
        "search_use_hybrid_default": settings.search.use_hybrid_default,
        "ollama_model": settings.ollama.model,
        "cache_enabled": settings.redis.enabled,
    }

    return health_status


@router.get("/ready", summary="Readiness check")
async def readiness_check() -> Dict:
    """
    Simple readiness check for Kubernetes/Docker.

    Returns:
        Basic status indicating if the service is ready
    """
    try:
        # Quick check of critical services
        opensearch = make_opensearch_client()
        opensearch.health_check()

        return {
            "status": "ready",
            "message": "Service is ready to accept requests",
        }
    except Exception as e:
        logger.error(f"Readiness check failed: {e}")
        return {
            "status": "not_ready",
            "message": str(e),
        }


@router.get("/live", summary="Liveness check")
async def liveness_check() -> Dict:
    """
    Simple liveness check for Kubernetes/Docker.

    Returns:
        Basic status indicating if the service is alive
    """
    return {
        "status": "alive",
        "message": "Service is running",
    }
