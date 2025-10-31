"""
Embeddings service using Sentence Transformers.
Replaces Jina AI with local multilingual model.
"""

import logging
from typing import List, Union

import numpy as np
import torch
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class EmbeddingsService:
    """
    Embeddings generation using Sentence Transformers.
    Uses multilingual model for Vietnamese support.
    """

    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        device: str = "cpu",
        batch_size: int = 32,
        max_length: int = 512,
    ):
        """
        Initialize embeddings service.

        Args:
            model_name: Sentence transformer model name
            device: Device to run on ('cpu' or 'cuda')
            batch_size: Batch size for encoding
            max_length: Maximum sequence length
        """
        self.model_name = model_name
        self.device = device
        self.batch_size = batch_size
        self.max_length = max_length
        self.logger = logging.getLogger(__name__)

        self.logger.info(f"Loading embeddings model: {model_name}")

        # Load model
        self.model = SentenceTransformer(model_name)
        self.model.to(device)
        self.model.max_seq_length = max_length

        # Get embedding dimension
        self.dimensions = self.model.get_sentence_embedding_dimension()

        self.logger.info(
            f"Embeddings model loaded: {model_name}, "
            f"dimensions: {self.dimensions}, "
            f"device: {device}"
        )

    async def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of text strings

        Returns:
            numpy array of shape (len(texts), dimensions)
        """
        if not texts:
            return np.array([])

        self.logger.debug(f"Generating embeddings for {len(texts)} texts")

        try:
            # Encode in batches
            embeddings = self.model.encode(
                texts,
                batch_size=self.batch_size,
                show_progress_bar=len(texts) > 100,
                convert_to_numpy=True,
                normalize_embeddings=True,  # L2 normalization
                device=self.device,
            )

            self.logger.debug(f"Generated embeddings shape: {embeddings.shape}")
            return embeddings

        except Exception as e:
            self.logger.error(f"Error generating embeddings: {e}", exc_info=True)
            raise

    async def embed_query(self, query: str) -> np.ndarray:
        """
        Generate embedding for a single query.

        Args:
            query: Query string

        Returns:
            numpy array of shape (dimensions,)
        """
        if not query.strip():
            self.logger.warning("Empty query provided for embedding")
            return np.zeros(self.dimensions)

        try:
            embedding = self.model.encode(
                query,
                convert_to_numpy=True,
                normalize_embeddings=True,
                device=self.device,
            )

            return embedding

        except Exception as e:
            self.logger.error(f"Error generating query embedding: {e}", exc_info=True)
            raise

    async def embed_documents(self, documents: List[str]) -> List[List[float]]:
        """
        Generate embeddings and return as list of lists (for JSON serialization).

        Args:
            documents: List of document texts

        Returns:
            List of embeddings as lists
        """
        embeddings = await self.embed_texts(documents)
        return embeddings.tolist()

    def get_dimensions(self) -> int:
        """Get embedding dimensions."""
        return self.dimensions

    def get_model_info(self) -> dict:
        """Get model information."""
        return {
            "model_name": self.model_name,
            "dimensions": self.dimensions,
            "device": self.device,
            "batch_size": self.batch_size,
            "max_length": self.max_length,
        }
