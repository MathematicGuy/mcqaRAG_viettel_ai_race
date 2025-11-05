"""
API Schemas for request/response validation.
Pydantic models for all API endpoints.
"""

from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field


# Health Check Schemas
class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str = Field(..., description="Overall system status")
    environment: str = Field(..., description="Environment name")
    services: Dict = Field(..., description="Individual service statuses")
    configuration: Optional[Dict] = Field(None, description="System configuration")


# Search Schemas
class SearchRequest(BaseModel):
    """Search request schema."""

    query: str = Field(..., description="Search query text", min_length=1)
    ### Điều này có nghĩa là top k >=1 và <= 20
    top_k: int = Field(default=5, ge=1, le=50, description="Number of results to return")
    use_hybrid: bool = Field(default=True, description="Use hybrid search (BM25 + Vector)")
    source_folder: Optional[str] = Field(None, description="Filter by source folder")
    min_score: float = Field(default=0.0, ge=0.0, description="Minimum score threshold")


class SearchHit(BaseModel):
    """Single search result."""

    chunk_id: str
    # document_id: str
    chunk_text: str
    section_name: Optional[str] = None
    score: float
    # chunk_index: Optional[int] = None
    # word_count: Optional[int] = None
    # source_folder: Optional[str] = None
    document_file_name: Optional[str] = None
    document_title: Optional[str] = None


class SearchResponse(BaseModel):
    """Search response schema."""

    query: str
    total: int = Field(..., description="Total number of results")
    hits: List[SearchHit] = Field(default_factory=list)
    search_mode: str = Field(..., description="Search mode used (bm25/vector/hybrid)")
    timing_ms: Optional[int] = Field(None, description="Search time in milliseconds")
    document_counts: List[Dict[str, Union[str, int]]] = Field(default_factory=list, description="Count of chunks per document in top_k results, sorted by count descending")


# RAG Schemas
class AskRequest(BaseModel):
    """MCQ question answering request."""

    question: str = Field(..., description="Question text", min_length=1)
    options: Dict[str, str] = Field(
        ...,
        description="Answer options as dict {A: text, B: text, C: text, D: text}",
        example={"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
    )
    top_k: int = Field(default=5, ge=1, le=10, description="Number of chunks to retrieve")
    use_hybrid: bool = Field(default=True, description="Use hybrid search")
    source_folder: Optional[str] = Field(None, description="Filter by source folder")
    model: Optional[str] = Field(None, description="Override default LLM model")


class SourceInfo(BaseModel):
    """Source information for RAG response."""

    document_id: str
    chunk_id: str
    section_name: Optional[str] = None
    score: float
    preview: str


class AskResponse(BaseModel):
    """MCQ answer response."""

    question: str
    options: Dict[str, str]
    predicted_option: Optional[str] = Field(
        None, description="Predicted answer (A/B/C/D)", pattern="^[ABCD]$"
    )
    answer_text: str = Field(..., description="Full answer text from LLM")
    reasoning: str = Field(..., description="Reasoning for the answer")
    confidence: str = Field(
        ..., description="Confidence level (high/medium/low)", pattern="^(high|medium|low)$"
    )
    sources: List[SourceInfo] = Field(default_factory=list, description="Source chunks used")
    search_mode: str = Field(..., description="Search mode used")
    model: Optional[str] = Field(None, description="LLM model used")
    timing: Dict[str, int] = Field(
        ...,
        description="Timing breakdown",
        example={"total_ms": 5000, "retrieval_ms": 200, "generation_ms": 4800},
    )
    from_cache: bool = Field(default=False, description="Whether result was from cache")
    error: Optional[str] = Field(None, description="Error message if any")


# Document Schemas
class DocumentCreate(BaseModel):
    """Schema for creating a new document."""

    doc_id: str
    filename: str
    file_path: str
    title: Optional[str] = None
    source_folder: Optional[str] = None


class DocumentResponse(BaseModel):
    """Document response schema."""

    id: int
    doc_id: str
    filename: str
    title: Optional[str] = None
    page_count: int
    processing_status: str
    created_at: str
    chunk_count: Optional[int] = None

    class Config:
        from_attributes = True


# Batch Processing Schemas
class BatchAskRequest(BaseModel):
    """Batch MCQ answering request."""

    questions: List[AskRequest] = Field(..., description="List of questions to answer")


class BatchAskResponse(BaseModel):
    """Batch MCQ answering response."""

    results: List[AskResponse]
    total_questions: int
    successful: int
    failed: int
    total_time_ms: int


# Statistics Schemas
class SystemStats(BaseModel):
    """System statistics."""

    total_documents: int
    total_chunks: int
    total_questions_answered: int
    cache_hit_rate: Optional[float] = None
    average_response_time_ms: Optional[float] = None


# Indexing Schemas
class IndexRequest(BaseModel):
    """Request to trigger document indexing."""

    pdf_paths: List[str] = Field(..., description="Paths to PDF files to index")
    source_folder: Optional[str] = Field(None, description="Source folder tag")
    force_reindex: bool = Field(default=False, description="Force reindexing existing docs")


class IndexResponse(BaseModel):
    """Indexing operation response."""

    status: str
    documents_processed: int
    chunks_created: int
    chunks_indexed: int
    errors: List[str] = Field(default_factory=list)
    processing_time_ms: int
