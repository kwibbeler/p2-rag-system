# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I picked a corpus of open-access scientific papers about snow and avalanches, specifically avalanche forecasting, snowpack stability, and avalanche hazard because I am interested in backcountry skiing how the science of the snowpack impacts the avalanche danger and forecast. I would expect hybrid to perform the best of all the options because it balances the techinical terms and the context the best. I think that the reranker would perform the worst because it only looks at the first 600 characters and each document is much longer. 
---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

When I was working on section 5 of the EVAL.md, I was debating if I should measure the effect of doubling the chunk size or cutting it in half. I ended up picking a chunk size of 600 words because I wanted to see if there was any impact on the query results if there was more context per chunk. The main reason I did not choose 150 words is because that would mean double the chunks to embed and score than 300 words and I was not confident that would perform well with the lack of detail so I went with the 600 word size. What I gave up because I only tested the larger side, is that I can't say whether smaller chunks would have beaten 300 words.I never actually ran a comparison with 150 words so I don't know what the results were. The results I do have for this choice show that 600 words vs. 300 words has no detectable difference with a mean of +0.014 and the interval for MRR@10 being [−0.033, +0.067]. 

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

There was not a case where I overruled the agent. I think this was mainly due to the fact that I was only focusing on one step at a time and not all of the steps for the whole project, so I wasn't challenging something the agent said that might have an impact down the road because I was not looking that far either. In order to notice I would have had to compare the paper count the agent gave me with the rows in corpora/own/manifest.tsv, and read the license column against the publisher pages. The agent assumed every paper from 2018 on was CC BY 4.0, and it found the two CC BY 3.0 papers later; I would only have noticed by reading the license column myself.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

A number I do not fully trust is from rerank minus hybrid with MRR@10 = +0.019 and the interval [−0.056, +0.093]. Since the interval includes zero it does not fully tell me that rerank was better than hybrid. Zero inside the interval means the data are compatible with no difference, but the real problem is power. The MDD for this pair is 0.109, and the difference I saw was 0.019, about a fifth of that. With 40 queries, this gold set could only have detected a gap more than five times bigger than the one I measured. For scale, using my PREREG standard deviation of 0.247, detecting 0.019 would take about 1,300 queries. So in order to trust this result I would like to have about 1,300 queries and then evaluate the results that way. 

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

One thing that is not right, or that I want to investigate more is that the queries that I wrote by hand performed worse than the queries written by claude. I would like to investigate if this is because I wrote harder queries, or if there are patterns in each of the groups that would tell us where the systems struggled or did well. 
