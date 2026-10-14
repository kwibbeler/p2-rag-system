"""Your dense retriever (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

This is the 12 lab's dense_rankings ported to chunks:
- embed.doc_vectors encodes every chunk and caches the vectors in .cache/vectors/, so only the first run is slow;
- every vector has length 1, so one matrix product (chunk vectors @ query vector) gives all the cosines at once;
- ChunkScorer lifts the chunk scores to documents (a document scores its best chunk) and gives `p2 answer` its chunk search.

The model is read from an optional [dense] table in p2.toml (model = "..."), and defaults to bge-small-en-v1.5.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        if not len(self.vectors):
            return []
        query = self.embedder.encode([text])[0]
        return (self.vectors @ query).tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
