"""Your reranker (stage 1): ask Claude to reorder hybrid's top 20.

This is the 13 lab's rerank_one() on p2's pieces:
- the first stage is hybrid (bm25 and dense fused), taken through p2.retrievers.build;
- the top 20 go to Claude as numbered passages, cut to passage_chars characters, in one claude -p call;
- the schema forces the reply into {"order": [n numbers]}, each between 1 and n, so Claude cannot name a passage that does not exist;
- a reply that is not each number once, or a failed call, keeps the first-stage order for that query and prints a warning;
- the documents below the 20 keep their first-stage order underneath.

Settings are read from an optional [rerank] table in p2.toml: candidates (default 20) and passage_chars (default 600, the lab's).
NEEDS_CLAUDE = True, so CI never calls Claude: p2 check compares these runs with the trace committed beside them in traces/.
`p2 answer` uses search_chunks: the same reranking over hybrid's top 20 chunks.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers

NEEDS_CLAUDE = True

PROMPT = """Below are {n} passages from US federal mine safety and health regulations (30 CFR), numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.model = cfg.model
        table = cfg.table("rerank")
        self.candidates = int(table.get("candidates", 20))
        self.passage_chars = int(table.get("passage_chars", 600))
        self.first = retrievers.build("hybrid", corpus, cfg)

    def _reorder(self, text: str, ids: list[str], passages: list[str]) -> list[str]:
        """The top candidates in Claude's order; the first-stage order if the call or the reply is bad."""
        top = ids[: self.candidates]
        n = len(top)
        if n < 2:
            return ids
        body = "\n\n".join(f"[{i}] {p[: self.passage_chars]}" for i, p in enumerate(passages[:n], 1))
        reply = claude.call(
            PROMPT.format(n=n, query=text, passages=body), schema(n),
            model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg),
        )
        order = (reply.output or {}).get("order")
        if reply.error or not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            why = reply.error or f"reply was not each of 1 to {n} once: {order}"
            print(f"WARNING: rerank kept the first-stage order for {text[:50]!r}: {why}", file=sys.stderr)
            return ids
        return [top[i - 1] for i in order] + ids[n:]

    @staticmethod
    def _scored(ids: list[str], k: int) -> list[tuple[str, float]]:
        # Scores only have to fall as the rank rises; 1 / rank keeps them distinct at six decimals.
        return [(item, 1.0 / rank) for rank, item in enumerate(ids[:k], 1)]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ids = [d for d, _ in self.first.search(text, max(k, self.candidates))]
        passages = [self.corpus.docs[d].text for d in ids[: self.candidates]]
        return self._scored(self._reorder(text, ids, passages), k)

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ids = [c for c, _ in self.first.search_chunks(text, max(k, self.candidates))]
        by_id = {c.id: c.text for c in self.first.parts[0].chunks}
        passages = [by_id[c] for c in ids[: self.candidates]]
        return self._scored(self._reorder(text, ids, passages), k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
