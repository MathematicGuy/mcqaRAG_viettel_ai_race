"""
Configuration management module for RAG MCQ System.
Handles all environment variables and settings using Pydantic Settings.
"""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    """PostgreSQL database configuration."""

    host: str = Field(default="localhost", alias="POSTGRES_HOST")
    port: int = Field(default=5432, alias="POSTGRES_PORT")
    user: str = Field(default="rag_user", alias="POSTGRES_USER")
    password: str = Field(default="rag_password", alias="POSTGRES_PASSWORD")
    database: str = Field(default="rag_mcq_db", alias="POSTGRES_DATABASE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def connection_string(self) -> str:
        """Generate PostgreSQL connection string."""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class OpenSearchSettings(BaseSettings):
    """OpenSearch configuration."""

    host: str = Field(default="http://localhost:9200", alias="OPENSEARCH_HOST")
    username: str = Field(default="admin", alias="OPENSEARCH_USERNAME")
    password: str = Field(default="admin", alias="OPENSEARCH_PASSWORD")
    index_name: str = Field(default="mcq-documents", alias="OPENSEARCH_INDEX_NAME")
    verify_certs: bool = Field(default=False, alias="OPENSEARCH_VERIFY_CERTS")
    use_ssl: bool = Field(default=False, alias="OPENSEARCH_USE_SSL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class EmbeddingsSettings(BaseSettings):
    """Embeddings model configuration."""

    model_name: str = Field(
        default="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        alias="EMBEDDINGS_MODEL_NAME",
    )
    device: str = Field(default="cpu", alias="EMBEDDINGS_DEVICE")
    batch_size: int = Field(default=32, alias="EMBEDDINGS_BATCH_SIZE")
    max_length: int = Field(default=512, alias="EMBEDDINGS_MAX_LENGTH")
    dimensions: int = Field(default=768, alias="EMBEDDINGS_DIMENSIONS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ChunkingSettings(BaseSettings):
    """Document chunking configuration."""

    chunk_size: int = Field(default=600, alias="CHUNKING_CHUNK_SIZE")
    overlap_size: int = Field(default=100, alias="CHUNKING_OVERLAP_SIZE")
    min_chunk_size: int = Field(default=100, alias="CHUNKING_MIN_CHUNK_SIZE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class PDFParserSettings(BaseSettings):
    """PDF parser configuration for Docling."""

    max_pages: int = Field(default=1000, alias="PDF_PARSER_MAX_PAGES")
    do_ocr: bool = Field(default=False, alias="PDF_PARSER_DO_OCR")
    extract_tables: bool = Field(default=True, alias="PDF_PARSER_EXTRACT_TABLES")
    extract_images: bool = Field(default=False, alias="PDF_PARSER_EXTRACT_IMAGES")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class OllamaSettings(BaseSettings):
    """Ollama LLM configuration."""

    host: str = Field(default="http://localhost:11434", alias="OLLAMA_HOST")
    model: str = Field(default="llama3.2:3b", alias="OLLAMA_MODEL")
    timeout: int = Field(default=120, alias="OLLAMA_TIMEOUT")
    max_response_words: int = Field(default=500, alias="OLLAMA_MAX_RESPONSE_WORDS")
    temperature: float = Field(default=0.1, alias="OLLAMA_TEMPERATURE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class SearchSettings(BaseSettings):
    """Search configuration."""

    top_k_default: int = Field(default=5, alias="SEARCH_TOP_K_DEFAULT")
    use_hybrid_default: bool = Field(default=True, alias="SEARCH_USE_HYBRID_DEFAULT")
    bm25_weight: float = Field(default=0.5, alias="SEARCH_BM25_WEIGHT")
    vector_weight: float = Field(default=0.5, alias="SEARCH_VECTOR_WEIGHT")
    min_score: float = Field(default=0.0, alias="SEARCH_MIN_SCORE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class RedisSettings(BaseSettings):
    """Redis cache configuration."""

    host: str = Field(default="localhost", alias="REDIS_HOST")
    port: int = Field(default=6379, alias="REDIS_PORT")
    db: int = Field(default=0, alias="REDIS_DB")
    cache_ttl_hours: int = Field(default=24, alias="REDIS_CACHE_TTL_HOURS")
    max_connections: int = Field(default=10, alias="REDIS_MAX_CONNECTIONS")
    enabled: bool = Field(default=True, alias="REDIS_ENABLED")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def url(self) -> str:
        """Generate Redis URL."""
        return f"redis://{self.host}:{self.port}/{self.db}"


class LangfuseSettings(BaseSettings):
    """Langfuse monitoring configuration."""

    public_key: str = Field(default="", alias="LANGFUSE_PUBLIC_KEY")
    secret_key: str = Field(default="", alias="LANGFUSE_SECRET_KEY")
    host: str = Field(default="http://localhost:3000", alias="LANGFUSE_HOST")
    enabled: bool = Field(default=False, alias="LANGFUSE_ENABLED")
    flush_interval: float = Field(default=1.0, alias="LANGFUSE_FLUSH_INTERVAL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DataSettings(BaseSettings):
    """Data paths configuration."""

    pdf_dir: str = Field(default="../data/pdf", alias="DATA_PDF_DIR")
    question_csv: str = Field(default="../data/question.csv", alias="DATA_QUESTION_CSV")
    processed_dir: str = Field(default="./data/processed", alias="DATA_PROCESSED_DIR")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class APISettings(BaseSettings):
    """API server configuration."""

    host: str = Field(default="0.0.0.0", alias="API_HOST")
    port: int = Field(default=8000, alias="API_PORT")
    reload: bool = Field(default=True, alias="API_RELOAD")
    workers: int = Field(default=1, alias="API_WORKERS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    """Main application settings combining all configurations."""

    debug: bool = Field(default=True, alias="DEBUG")
    environment: str = Field(default="development", alias="ENVIRONMENT")

    # Sub-configurations
    postgres: PostgresSettings = Field(default_factory=PostgresSettings)
    opensearch: OpenSearchSettings = Field(default_factory=OpenSearchSettings)
    embeddings: EmbeddingsSettings = Field(default_factory=EmbeddingsSettings)
    chunking: ChunkingSettings = Field(default_factory=ChunkingSettings)
    pdf_parser: PDFParserSettings = Field(default_factory=PDFParserSettings)
    ollama: OllamaSettings = Field(default_factory=OllamaSettings)
    search: SearchSettings = Field(default_factory=SearchSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    langfuse: LangfuseSettings = Field(default_factory=LangfuseSettings)
    data: DataSettings = Field(default_factory=DataSettings)
    api: APISettings = Field(default_factory=APISettings)

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings: Application settings
    """
    return Settings()


# Export commonly used settings
__all__ = [
    "Settings",
    "PostgresSettings",
    "OpenSearchSettings",
    "EmbeddingsSettings",
    "ChunkingSettings",
    "PDFParserSettings",
    "OllamaSettings",
    "SearchSettings",
    "RedisSettings",
    "LangfuseSettings",
    "DataSettings",
    "APISettings",
    "get_settings",
]
