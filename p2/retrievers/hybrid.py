"""Your hybrid retriever (stage 1): reciprocal rank fusion of bm25 and dense.

This is the 13 lab's rrf() on the two systems' full rankings: a document scores the sum of
1 / (k + rank) over the rankings it appears in, so a document that both keyword search and
embedding search put high wins, and one that only a single system finds still gets credit.
- both systems are asked for every document (or chunk), not a top 10, because a document that is
  11th in both lists can belong in the fused top 10;
- p2.retrievers.build gives the same bm25 and dense objects the other systems use, so each index is built once;
- p2.runfile.order puts equal scores in document id order.

The fusion constant is read from an optional [hybrid] table in p2.toml (k = ...), and defaults to the lab's 60.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False


def rrf(rankings, k: int = 60) -> list[tuple[str, float]]:
    """Fuse rankings (lists of ids, best first) into (id, score) pairs, best first."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.k = int(cfg.table("hybrid").get("k", 60))
        self.parts = [retrievers.build(name, corpus, cfg) for name in ("bm25", "dense")]
        self.n_chunks = len(self.parts[0].chunks)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        full = [[d for d, _ in part.search(text, len(self.corpus.docs))] for part in self.parts]
        return rrf(full, self.k)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        full = [[c for c, _ in part.search_chunks(text, self.n_chunks)] for part in self.parts]
        return rrf(full, self.k)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
