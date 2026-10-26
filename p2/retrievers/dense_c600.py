"""Ablation of dense: the chunk size doubled from 300 to 600 words, everything else the same.

The overlap stays at the p2.toml value (50 words), the model is dense's own (bge-small-en-v1.5 unless [dense] says otherwise),
and a document still scores its best chunk. Note that bge-small reads at most about 512 tokens, roughly the first 380 words of a
600-word chunk, so this variant changes the chunk size and also how much of each chunk dense can see.
"""

from __future__ import annotations

from p2.retrievers.dense import Dense

BASE = "dense"
NEEDS_CLAUDE = False

CHUNK_WORDS = 600


def build(corpus, cfg):
    return Dense(corpus, cfg.replace(chunk_words=CHUNK_WORDS))
