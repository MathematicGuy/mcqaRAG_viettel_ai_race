"""
OpenSearch client with hybrid search support.
Implements BM25, Vector, and Hybrid RRF search.
"""

import logging
from typing import Dict, List, Optional

from opensearchpy import OpenSearch, helpers

logger = logging.getLogger(__name__)


class OpenSearchClient:
    """
    OpenSearch client with hybrid search capabilities.
    Supports BM25 (keyword), Vector (semantic), and Hybrid (RRF fusion) search.
    """

    def __init__(
        self,
        host: str = "http://localhost:9200",
        index_name: str = "mcq-documents",
        username: str = "admin",
        password: str = "admin",
        use_ssl: bool = False,
        verify_certs: bool = False,
    ):
        """
        Initialize OpenSearch client.

        Args:
            host: OpenSearch host URL
            index_name: Index name for documents
            username: Authentication username
            password: Authentication password
            use_ssl: Use SSL connection
            verify_certs: Verify SSL certificates
        """
        self.host = host
        self.index_name = index_name
        self.logger = logging.getLogger(__name__)

        # Initialize client
        self.client = OpenSearch(
            hosts=[host],
            http_auth=(username, password),
            use_ssl=use_ssl,
            verify_certs=verify_certs,
            ssl_show_warn=False,
            timeout=30,
            max_retries=3,
            retry_on_timeout=True,
        )

        self.logger.info(f"OpenSearch client initialized: {host}, index: {index_name}")

    async def create_index(self, dimensions: int = 768):
        """
        Create index with BM25 and vector fields.

        Args:
            dimensions: Embedding dimensions
        """
        if self.client.indices.exists(index=self.index_name):
            self.logger.warning(f"Index {self.index_name} already exists")
            return

        index_body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
                "index": {
                    "knn": True,
                    "knn.algo_param.ef_search": 512,
                },
                "analysis": {
                    "analyzer": {
                        "text_analyzer": {
                            "type": "custom",
                            "tokenizer": "standard",
                            "filter": ["lowercase", "stop", "snowball"],
                        }
                    }
                },
            },
            "mappings": {
                "properties": {
                    "chunk_id": {"type": "keyword"},
                    "document_id": {"type": "keyword"},
                    "chunk_text": {"type": "text", "analyzer": "text_analyzer"},
                    "section_name": {
                        "type": "text",
                        "fields": {"keyword": {"type": "keyword"}},
                    },
                    "embedding": {
                        "type": "knn_vector",
                        "dimension": dimensions,
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "nmslib",
                            "parameters": {"ef_construction": 512, "m": 16},
                        },
                    },
                    "word_count": {"type": "integer"},
                    "chunk_index": {"type": "integer"},
                    "chunk_type": {"type": "keyword"},
                    "source_folder": {"type": "keyword"},
                    "created_at": {"type": "date"},
                }
            },
        }

        self.client.indices.create(index=self.index_name, body=index_body)
        self.logger.info(f"Created index: {self.index_name} with {dimensions}D vectors")

    async def index_chunk(self, chunk: Dict) -> bool:
        """
        Index a single chunk.

        Args:
            chunk: Chunk document to index

        Returns:
            True if successful
        """
        try:
            response = self.client.index(
                index=self.index_name,
                body=chunk,
                id=chunk.get("chunk_id"),
                refresh=True,
            )
            return response["result"] in ["created", "updated"]
        except Exception as e:
            self.logger.error(f"Error indexing chunk {chunk.get('chunk_id')}: {e}")
            return False

    async def index_chunks_bulk(self, chunks: List[Dict]) -> Dict:
        """
        Bulk index multiple chunks.

        Args:
            chunks: List of chunk documents

        Returns:
            Dict with success/error counts
        """
        actions = [
            {
                "_index": self.index_name,
                "_id": chunk.get("chunk_id"),
                "_source": chunk,
            }
            for chunk in chunks
        ]

        success, errors = helpers.bulk(self.client, actions, raise_on_error=False, refresh=True)

        self.logger.info(
            f"Bulk indexed {success} chunks, {len(errors)} errors to {self.index_name}"
        )

        return {"success": success, "errors": len(errors)}

    async def search_bm25(
        self,
        query: str,
        top_k: int = 5,
        source_folder: Optional[str] = None,
        min_score: float = 0.0,
    ) -> List[Dict]:
        """
        BM25 keyword search.

        Args:
            query: Search query
            top_k: Number of results to return
            source_folder: Filter by source folder
            min_score: Minimum score threshold

        Returns:
            List of matching chunks with scores
        """
        search_body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["chunk_text^2", "section_name"],
                                "type": "best_fields",
                                "operator": "or",
                            }
                        }
                    ]
                }
            },
            "size": top_k,
            "min_score": min_score,
            "_source": {
                "excludes": ["embedding"]  # Don't return embeddings for BM25
            },
        }

        # Add filter if specified
        if source_folder:
            search_body["query"]["bool"]["filter"] = [{"term": {"source_folder": source_folder}}]

        try:
            response = self.client.search(index=self.index_name, body=search_body)
            results = self._parse_response(response)
            self.logger.debug(f"BM25 search returned {len(results)} results")
            return results
        except Exception as e:
            self.logger.error(f"BM25 search error: {e}")
            return []

    async def search_vector(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        source_folder: Optional[str] = None,
    ) -> List[Dict]:
        """
        Vector similarity search.

        Args:
            query_embedding: Query embedding vector
            top_k: Number of results to return
            source_folder: Filter by source folder

        Returns:
            List of matching chunks with scores
        """
        search_body = {
            "query": {
                "knn": {
                    "embedding": {
                        "vector": query_embedding,
                        "k": top_k,
                    }
                }
            },
            "size": top_k,
            "_source": {"excludes": ["embedding"]},
        }

        # Add filter if specified
        if source_folder:
            search_body["query"]["knn"]["embedding"]["filter"] = {
                "term": {"source_folder": source_folder}
            }

        try:
            response = self.client.search(index=self.index_name, body=search_body)
            results = self._parse_response(response)
            self.logger.debug(f"Vector search returned {len(results)} results")
            return results
        except Exception as e:
            self.logger.error(f"Vector search error: {e}")
            return []

    async def search_hybrid(
        self,
        query: str,
        query_embedding: List[float],
        top_k: int = 5,
        source_folder: Optional[str] = None,
        rrf_k: int = 60,
    ) -> List[Dict]:
        """
        Hybrid search using RRF (Reciprocal Rank Fusion).
        Combines BM25 and vector search results.

        Args:
            query: Search query text
            query_embedding: Query embedding vector
            top_k: Number of final results
            source_folder: Filter by source folder
            rrf_k: RRF constant (default 60)

        Returns:
            List of fused results with scores
        """
        # Get results from both methods
        bm25_results = await self.search_bm25(query, top_k * 2, source_folder)
        vector_results = await self.search_vector(query_embedding, top_k * 2, source_folder)

        # Apply RRF fusion
        fused_results = self._rrf_fusion(bm25_results, vector_results, k=rrf_k)

        # Return top-k fused results
        return fused_results[:top_k]

    def _rrf_fusion(
        self, bm25_results: List[Dict], vector_results: List[Dict], k: int = 60
    ) -> List[Dict]:
        """
        Reciprocal Rank Fusion algorithm.

        RRF formula: score = sum(1 / (k + rank))

        Args:
            bm25_results: Results from BM25 search
            vector_results: Results from vector search
            k: RRF constant

        Returns:
            Fused results sorted by RRF score
        """
        scores = {}
        chunk_data = {}

        # Score BM25 results
        for rank, result in enumerate(bm25_results, start=1):
            chunk_id = result.get("chunk_id")
            scores[chunk_id] = scores.get(chunk_id, 0) + 1 / (k + rank)
            chunk_data[chunk_id] = result

        # Score vector results
        for rank, result in enumerate(vector_results, start=1):
            chunk_id = result.get("chunk_id")
            scores[chunk_id] = scores.get(chunk_id, 0) + 1 / (k + rank)
            if chunk_id not in chunk_data:
                chunk_data[chunk_id] = result

        # Sort by fused score
        fused = []
        for chunk_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            chunk = chunk_data[chunk_id].copy()
            chunk["fusion_score"] = score
            chunk["search_mode"] = "hybrid"
            fused.append(chunk)

        self.logger.debug(
            f"RRF fusion: {len(fused)} results from {len(bm25_results)}+{len(vector_results)}"
        )
        return fused

    def _parse_response(self, response: Dict) -> List[Dict]:
        """
        Parse OpenSearch response.

        Args:
            response: Raw OpenSearch response

        Returns:
            List of result documents with scores
        """
        hits = response.get("hits", {}).get("hits", [])
        results = []

        for hit in hits:
            result = hit["_source"]
            result["score"] = hit["_score"]
            results.append(result)

        return results

    async def delete_index(self):
        """Delete the index."""
        if self.client.indices.exists(index=self.index_name):
            self.client.indices.delete(index=self.index_name)
            self.logger.info(f"Deleted index: {self.index_name}")

    async def get_document_count(self) -> int:
        """Get total document count in index."""
        try:
            response = self.client.count(index=self.index_name)
            return response["count"]
        except Exception:
            return 0

    def health_check(self) -> Dict:
        """
        Check OpenSearch cluster health.

        Returns:
            Health status dict
        """
        try:
            health = self.client.cluster.health()
            return {
                "status": health["status"],
                "cluster_name": health["cluster_name"],
                "number_of_nodes": health["number_of_nodes"],
                "index_exists": self.client.indices.exists(index=self.index_name),
            }
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            return {"status": "error", "error": str(e)}
