"""
Main FastAPI application for RAG MCQ System.
Provides REST API endpoints for document search and question answering.
"""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import get_settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    Lifespan context manager for FastAPI application.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info("Starting RAG MCQ System API...")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Debug mode: {settings.debug}")

    # Initialize services
    try:
        logger.info("✓ Configuration loaded")
        logger.info(f"✓ PostgreSQL: {settings.postgres.host}:{settings.postgres.port}")
        logger.info(f"✓ OpenSearch: {settings.opensearch.host}")
        logger.info(f"✓ Redis: {settings.redis.host}:{settings.redis.port}")
        logger.info(f"✓ Ollama: {settings.ollama.host}")
        logger.info(f"✓ Embedding model: {settings.embeddings.model_name}")
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        raise

    yield

    # Shutdown
    logger.info("Shutting down RAG MCQ System API...")


# Create FastAPI application
app = FastAPI(
    title="RAG MCQ System API",
    description="Production-ready RAG system for multiple choice question answering from PDF documents",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "RAG MCQ System API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns the status of all services.
    """
    health_status = {
        "status": "healthy",
        "environment": settings.environment,
        "services": {
            "api": "healthy",
            "postgres": {
                "status": "unknown",
                "host": settings.postgres.host,
                "port": settings.postgres.port,
            },
            "opensearch": {
                "status": "unknown",
                "host": settings.opensearch.host,
            },
            "redis": {
                "status": "unknown",
                "enabled": settings.redis.enabled,
                "host": settings.redis.host,
            },
            "ollama": {
                "status": "unknown",
                "host": settings.ollama.host,
                "model": settings.ollama.model,
            },
        },
        "configuration": {
            "embedding_model": settings.embeddings.model_name,
            "chunk_size": settings.chunking.chunk_size,
            "chunk_overlap": settings.chunking.overlap_size,
            "top_k_default": settings.search.top_k_default,
            "use_hybrid_default": settings.search.use_hybrid_default,
        },
    }

    # Try to check service health
    try:
        # TODO: Add actual health checks for each service
        # For now, just return the configuration
        pass
    except Exception as e:
        logger.error(f"Health check error: {e}")
        health_status["status"] = "degraded"
        health_status["error"] = str(e)

    return health_status


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc) if settings.debug else "An error occurred",
        },
    )


# Import and include routers
try:
    from src.routers import ask, health, search

    app.include_router(health.router, tags=["health"])
    app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
    app.include_router(ask.router, prefix="/api/v1", tags=["rag"])

    logger.info("✓ All routers registered successfully")
except ImportError as e:
    logger.error(f"Failed to import routers: {e}", exc_info=True)
    raise


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host=settings.api.host,
        port=settings.api.port,
        reload=settings.api.reload,
        workers=settings.api.workers,
        log_level="info" if settings.debug else "warning",
    )
