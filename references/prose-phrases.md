# Prose Phrases: the most-wanted list

Words and phrases that read as AI slop. This is a reference for the scan, not an execution list, obey the exclusion zones in SKILL.md (quotes, proper names, literal uses, and specificity-anchored uses are not crimes).

## Contents
- Throat-clearing openers
- Overused verbs
- Overused adjectives
- Overused metaphorical nouns
- Empty intensifiers and filler
- Transitions and connectors
- Opening / transitional / concluding phrases
- Inflated symbolism phrases
- Hedging markers
- Academic tells
- Hallucinated markup artifacts (zero tolerance)

---

## Throat-clearing openers

Announcement phrases before the actual point. Cut them and state the point.

"Here's the thing:", "Here's what/why/how [X]", "The uncomfortable truth is", "It turns out", "The real [X] is", "Let me be clear", "The truth is,", "I'll say it again:", "I'm going to be honest", "Can we talk about", "Here's what I find interesting", "Here's the problem though", "Let's delve into", "Imagine a world where".

Rule of thumb: any "here's what/this/that" construction is throat-clearing. Delete and lead with the fact.

## Overused verbs

| Avoid | Use |
|-------|-----|
| delve (into) | explore, examine, look at |
| leverage | use, apply, draw on |
| utilize / utilise | use |
| facilitate | help, enable |
| foster | encourage, develop, nurture |
| bolster | strengthen, reinforce |
| underscore | emphasize, highlight |
| unveil | reveal, show, introduce |
| navigate (abstract) | manage, handle, work through |
| streamline | simplify |
| enhance | improve, strengthen |
| optimize / optimise | improve, refine |
| endeavour | try, attempt |
| ascertain | find out, determine |
| elucidate | explain, clarify |
| shed light on | clarify, explain, reveal |
| pave the way for | enable, allow |

## Overused adjectives

| Avoid | Use |
|-------|-----|
| robust | strong, reliable, solid |
| comprehensive | complete, thorough, full |
| pivotal / crucial / vital | key, important, essential |
| transformative | significant, major |
| cutting-edge / groundbreaking / innovative | new, original, advanced |
| seamless | smooth, easy |
| intricate / nuanced / multifaceted | complex, detailed, subtle |
| holistic | complete, whole |
| paramount | very important, essential |

## Overused metaphorical nouns

AI uses these metaphorically for false gravitas. Literal uses are fine (flag only the metaphor).

tapestry ("a tapestry of regulations"), symphony ("a symphony of features"), beacon ("a beacon of hope"), realm ("in the realm of X"), testament ("a testament to innovation"), ecosystem ("the repair ecosystem"), landscape ("the regulatory landscape").

## Empty intensifiers and filler

Kill adverbs doing vague work. Cut or replace with the specific thing.

absolutely, actually, basically, certainly, clearly, definitely, essentially, extremely, fundamentally, incredibly, interestingly, importantly, crucially, literally, naturally, obviously, quite, really, significantly, simply, surely, truly, ultimately, undoubtedly, very, just, genuinely, honestly, deeply, inherently, inevitably.

Filler phrases: "At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where", "The reality is", "a myriad of", "a plethora of", "the fact that", "prior to" (→ before), "subsequent to" (→ after), "in light of", "with respect to", "in terms of", "pertaining to".

## Latinate bias (prefer the short Anglo-Saxon word)

AI reaches for longer Latin-derived words where a plain one is clearer and more human. Swap them.

| Avoid | Use |
|-------|-----|
| utilize | use |
| commence | start, begin |
| facilitate | help |
| obtain / acquire | get |
| require | need |
| purchase | buy |
| assist | help |
| attempt | try |
| demonstrate | show |
| numerous | many |
| additional | more, extra |
| sufficient | enough |
| individuals | people |
| approximately | about |
| initial | first |
| terminate | end, stop |
| implement | build, do, add |
| leverage | use |

The point isn't that long words are banned; it's that AI defaults to them and humans usually don't. If the short word carries the meaning, use it.

## Transitions and connectors

| Avoid | Use |
|-------|-----|
| furthermore / moreover | also, and, besides |
| notwithstanding | despite, still |
| that being said | however, still |
| to put it simply | in short |
| it is worth noting that | note that |
| in the realm/landscape of | in, within |

## Opening / transitional / concluding phrases

**Openers:** "In today's fast-paced/digital world...", "In an era of...", "In the ever-evolving landscape of...", "It's important to note that...".

**Transitions:** "With that in mind...", "It's worth mentioning that...", "In essence...", "This begs the question...".

**Closers:** "In conclusion...", "To sum up...", "By [doing X], you can [achieve Y]...", "In the final analysis...", "All things considered...", "At the end of the day...".

## Inflated symbolism phrases

These appear far more often in AI text than human writing (corpus analysis). High-confidence tells:

"provide a valuable insight", "left an indelible mark", "play a significant role in shaping", "an unwavering commitment", "open a new avenue", "a stark reminder", "gain a comprehensive understanding", "serves as a testament", "watershed moment", "deeply rooted".

## Hedging markers

AI hedges 4–7× more than humans. Thin these unless the fact is genuinely disputed or pending.

Modals: may, might, could, potentially. Cognitive verbs: I think, I believe, it seems, it appears. Limiters: probably, generally, usually, arguably, likely. Uncertainty: unclear, remains to be seen, further research is needed. Phrases: "It is worth noting that", "It should be noted that", "One could argue that", "While X, Y remains", "It is widely acknowledged that".

Human hedging grounds uncertainty in evidence ("the FTC's 2024 data suggests a 12% increase"); AI hedging blankets established facts. Keep the former, cut the latter.

## Hallucinated markup artifacts: zero tolerance

Any occurrence means text was pasted from a chatbot without editing. Remove every one:

`oaicite`, `contentReference`, `turn0search0`, `grok_card`, `attributableIndex`.
