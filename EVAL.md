# Evaluation report
This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

The embedding model used for dense is bge-small-en-v1.5, and documents are chunked into 300-word sections with 50 words of overlap. A document is scored by its best chunk, which differs from lab 12: the lab embedded whole articles, and scoring chunks keeps a specific passage from being diluted by the rest of a long document. It also uses the course’s cache helper in place of the lab’s own. 

Hybrid fuses the rankings from bm25 and dense using reciprocal rank fusion, where each document scores 1/(60 + rank) from each system and the two are summed. It fuses full rankings rather than top-10 lists, so a document ranked low by one system still gets partial credit from it. The difference from the lab is an added chunk-level fusion for the answer step.

Rerank takes the top 20 documents from hybrid, and Claude sees them as numbered passages cut to 600 characters, returning the order as JSON. An invalid reply keeps hybrid’s order, which happened 0 times in 60 calls. The differences from lab 13 are the 1–20 range on the output schema and a prompt that describes the passages as mine safety regulations instead of “help center.”


### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.733 | 0.800 | 0.746 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.643 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.659 | 0.626 | 0.987 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.108 | [-0.133, +0.350] | 0.351 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.227 | [-0.009, +0.452] | 0.335 | not distinguishable |
| rerank minus dense | Recall@10 | +0.175 | [+0.033, +0.333] | 0.221 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.266 | [+0.123, +0.424] | 0.219 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | 0.160 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.302 | [+0.173, +0.436] | 0.192 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

TODO: write what the practice-query intervals let you claim.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | hybrid | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 16 of 16 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

TODO: write your answer choices and your three-answer audit.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

The corpus has 57 papers from the years 2018 to 2026 (3.7 MB or about 796,000 estimated tokens, and 240 documents) focusing on avalanche and snow science and the papers are open-access under Creative Commons Attribution (CC BY): 55 under version 4.0 and 2 under version 3.0. I was least sure about nhess-18-3235-2018 but I decided to remove it because it was unclear if I had the permissions to use the swisstopo line. Both versions are on the course's allowed list. I check the license basis by looking at the paper's own rights statement, the publisher's article page for each flagged paper, and the p2 license --online check which found no mismatches. The scan's 52 remaining flags were just the paper's own rights line. The other 24 flagged documents carried credit lines for third-party imagery (swisstopo, Airbus, Google), and I chose to remove them instead of keeping them. The scan only flags text it recognizes. Papers can include figures or data from other sources with their own terms so I made sure the corpus contains only the extracted text (no images).

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

My gold set has 40 queries total, 10 written by hand and 30 written by claude. I have 3 query categories, paraphrase, identifier and mixed and in the context of my own corpus the identifier names a specific method, scale, model, test or place (for example "EAWS matrix," "extended column test," "AutoATES"). Paraphrase is a plain-language question that avoids the papers' own terms, and mixed is a technical term plus plain wording. The reason for this class split is to be able to distinguish the dense (paraphrase) and bm25 (identifier) behavior would differ.

A document is relevant to a query if it directly answers the query rather than just talking about adjacent information. Since the papers are split into about 4 parts I would count a document as relevant even if has a brief mention if it is directly related to the query. 

I found the candidates by running three retrievers that don't call Claude (bm25, dense, hybrid) on the query text and took each one's top 10 documents and I did this for each of the 40 queries. The candidates for a query are the union of those lists, usually 14 to 18 documents. I did not use rerank, because it would cost Claude calls and starts from hybrid's results anyway. I only read certain passages of the documents rather than the whole thing. 

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.691 | 0.823 | 0.680 |
| dense | 0.655 | 0.851 | 0.679 |
| hybrid | 0.721 | 0.887 | 0.740 |
| rerank | 0.760 | 0.907 | 0.783 |

40 judged queries; nDCG uses binary labels; a random ranking of the 240 documents would get recall@10 near 0.042.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=13) | paraphrase (n=15) | mixed (n=12) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.859 | 0.421 | 0.847 |
| bm25 | MRR@10 | 1.000 | 0.604 | 0.903 |
| bm25 | nDCG@10 | 0.867 | 0.399 | 0.827 |
| dense | Recall@10 | 0.713 | 0.538 | 0.738 |
| dense | MRR@10 | 0.923 | 0.761 | 0.884 |
| dense | nDCG@10 | 0.737 | 0.563 | 0.760 |
| hybrid | Recall@10 | 0.801 | 0.561 | 0.835 |
| hybrid | MRR@10 | 0.962 | 0.778 | 0.944 |
| hybrid | nDCG@10 | 0.829 | 0.582 | 0.842 |
| rerank | Recall@10 | 0.831 | 0.616 | 0.862 |
| rerank | MRR@10 | 1.000 | 0.857 | 0.868 |
| rerank | nDCG@10 | 0.888 | 0.645 | 0.842 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=30) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.475 | 0.763 | -0.289 | [-0.478, -0.113] | claude higher |
| bm25 | MRR@10 | 0.703 | 0.862 | -0.159 | [-0.427, +0.088] | not distinguishable |
| bm25 | nDCG@10 | 0.462 | 0.752 | -0.290 | [-0.477, -0.101] | claude higher |
| dense | Recall@10 | 0.412 | 0.736 | -0.325 | [-0.494, -0.152] | claude higher |
| dense | MRR@10 | 0.636 | 0.922 | -0.286 | [-0.544, -0.044] | claude higher |
| dense | nDCG@10 | 0.416 | 0.766 | -0.351 | [-0.533, -0.160] | claude higher |
| hybrid | Recall@10 | 0.498 | 0.796 | -0.298 | [-0.478, -0.130] | claude higher |
| hybrid | MRR@10 | 0.667 | 0.961 | -0.294 | [-0.533, -0.078] | claude higher |
| hybrid | nDCG@10 | 0.491 | 0.824 | -0.333 | [-0.515, -0.153] | claude higher |
| rerank | Recall@10 | 0.551 | 0.829 | -0.278 | [-0.435, -0.107] | claude higher |
| rerank | MRR@10 | 0.703 | 0.975 | -0.272 | [-0.519, -0.050] | claude higher |
| rerank | nDCG@10 | 0.544 | 0.862 | -0.318 | [-0.520, -0.116] | claude higher |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.027 | +0.063 | -0.036 | [-0.258, +0.203] | not distinguishable |
| MRR@10 | -0.060 | +0.067 | -0.127 | [-0.375, +0.146] | not distinguishable |
| nDCG@10 | -0.014 | +0.047 | -0.061 | [-0.262, +0.147] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.75 (10 queries), claude 0.89 (30 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 30 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.036 | [-0.124, +0.052] | 0.126 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.028 | [-0.070, +0.130] | 0.144 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.001 | [-0.084, +0.083] | 0.119 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.030 | [-0.046, +0.102] | 0.107 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.065 | [-0.018, +0.156] | 0.125 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | +0.061 | [-0.005, +0.128] | 0.096 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.066 | [+0.019, +0.112] | 0.067 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.037 | [-0.029, +0.107] | 0.098 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.062 | [+0.025, +0.098] | 0.053 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.068 | [+0.0003, +0.134] | 0.097 | rerank higher |
| rerank minus bm25 | MRR@10 | +0.084 | [-0.020, +0.195] | 0.157 | not distinguishable |
| rerank minus bm25 | nDCG@10 | +0.103 | [+0.030, +0.175] | 0.105 | rerank higher |
| rerank minus dense | Recall@10 | +0.105 | [+0.038, +0.172] | 0.097 | rerank higher |
| rerank minus dense | MRR@10 | +0.056 | [+0.008, +0.116] | 0.078 | rerank higher |
| rerank minus dense | nDCG@10 | +0.104 | [+0.049, +0.165] | 0.083 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.038 | [-0.020, +0.097] | 0.083 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.019 | [-0.056, +0.093] | 0.109 | not distinguishable |
| rerank minus hybrid | nDCG@10 | +0.042 | [-0.009, +0.093] | 0.073 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

I expect varying the chunk size from 300 words to 600 words in dense to raise MRR@10 on my corpus because there will be more context provided in the chunk to be able to answer the query. 

<!-- p2:begin own-ablation -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
_No ablation runs yet: `uv run p2 run --corpus own --system NAME --ablation` writes one to runs/own/ablation/, then `uv run p2 score` fills this table._
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

TODO: write the ablation: the one change, the hypothesis, the result and the claim.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-hybrid.jsonl | hybrid | 12 | 12 | 2 | 103,142 | 8,173 | 103.9 | 8,595 | 681 | 8.7 |
| traces/answers-hybrid.r1.jsonl | hybrid | 12 | 12 | 0 | 90,657 | 8,194 | 104.5 | 7,555 | 683 | 8.7 |
| traces/answers-hybrid.r2.jsonl | hybrid | 12 | 12 | 0 | 74,195 | 6,135 | 87.5 | 6,183 | 511 | 7.3 |
| traces/answers-hybrid.r3.jsonl | hybrid | 12 | 12 | 0 | 88,717 | 8,633 | 110.1 | 7,393 | 719 | 9.2 |
| traces/own-own-rerank.jsonl | rerank | 40 | 40 | 2 | 708,585 | 40,411 | 503.6 | 17,715 | 1,010 | 12.6 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 314,797 | 9,810 | 147.3 | 15,740 | 490 | 7.4 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 334,267 | 12,507 | 178.7 | 16,713 | 625 | 8.9 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 323,987 | 15,339 | 208.2 | 16,199 | 767 | 10.4 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 320,916 | 11,419 | 167.9 | 16,046 | 571 | 8.4 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 678,811 | 21,601 | 383.1 | 16,970 | 540 | 9.6 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 15,740 | 7.4 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 15,740 | 7.4 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 15,740 | 7.4 | rerank higher |
| own: bm25 minus rerank | 40 | -0.084 | [-0.195, +0.020] | 17,715 | 12.6 | not distinguishable |
| own: dense minus rerank | 40 | -0.056 | [-0.116, -0.008] | 17,715 | 12.6 | rerank higher |
| own: hybrid minus rerank | 40 | -0.019 | [-0.093, +0.056] | 17,715 | 12.6 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 40 | 0.04 | 0.9 |
| traces/retrieval/own-own-dense.jsonl | dense | 40 | 0.17 | 4.1 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 40 | 0.21 | 5.2 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.03 | 1.6 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.13 | 6.4 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.18 | 8.8 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.07 | 1.6 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.23 | 5.7 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.36 | 9.0 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.733 | 0.800 | 0.739 |
| rerank.r2 | 0.758 | 0.800 | 0.751 |
| rerank.r3 | 0.721 | 0.775 | 0.715 |
| range (max minus min) | 0.037 | 0.025 | 0.036 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.129 | [+0.025, +0.250] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.304 | [+0.140, +0.482] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.296 | [+0.168, +0.427] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.308 | [+0.180, +0.438] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.271 | [+0.135, +0.414] | rerank.r3 higher |

Repeated answers shared/hybrid:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| hybrid.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| hybrid.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| hybrid.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
