# NLP with spaCy

This document provides detailed background for the spaCy part of an English-language bonus notebook on Natural Language Processing.

Verification note: technical claims and references in this document were checked on 2026-05-11 against official spaCy documentation and authoritative NLP references listed at the end of the file.

---

## 1. What spaCy is good for

spaCy is a Python library for practical NLP workflows. Its official documentation presents it as a library designed for real work with language data, including large-scale information extraction, trained pipelines, custom components, named entity recognition, part-of-speech tagging, dependency parsing, sentence segmentation, text classification, lemmatization, morphological analysis, and visualization.

For an introductory Python course, spaCy is useful because it demonstrates the modern pipeline approach:

1. Load a trained language pipeline.
2. Pass raw text to the pipeline.
3. Receive a `Doc` object with tokens and annotations.
4. Inspect linguistic features through object attributes.
5. Add rule-based patterns or custom components when needed.

This style contrasts nicely with NLTK, where students usually call separate functions for each step.

---

## 2. Installation and English model

Install spaCy:

```bash
pip install -U spacy
```

Download the small English pipeline:

```bash
python -m spacy download en_core_web_sm
```

Load it in Python:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

Check installed pipeline compatibility:

```bash
python -m spacy validate
```

The official spaCy documentation recommends using `python -m spacy` for commands so the command runs in the intended Python environment.

---

## 3. Trained pipelines and model choice

spaCy separates the library from trained pipeline packages. A pipeline package contains language data, components, model weights, and metadata.

For English, common packages include:

| Pipeline | Typical use |
| --- | --- |
| `en_core_web_sm` | small, fast, good for teaching and lightweight demos |
| `en_core_web_md` | medium pipeline, includes word vectors in many spaCy releases |
| `en_core_web_lg` | larger and more accurate than small pipelines, higher memory cost |
| `en_core_web_trf` | transformer-based, more accurate for many tasks, heavier dependency and runtime cost |

For a beginner notebook, use `en_core_web_sm` because:

- installation is smaller;
- it is fast enough for classroom use;
- it supports the core demonstrations: tokens, lemmas, POS tags, dependencies, named entities, and noun chunks.

For production or research, model choice should be based on accuracy, speed, memory, and domain fit.

---

## 4. Core spaCy objects

spaCy's object model is central to using the library.

| Object | Meaning |
| --- | --- |
| `Language` | The loaded pipeline object, usually named `nlp` |
| `Doc` | A processed document, created by calling `nlp(text)` |
| `Token` | One token inside a `Doc` |
| `Span` | A slice of a `Doc`, such as a sentence, entity, or noun phrase |
| `Vocab` | Shared vocabulary and string store |

Example:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
text = "Anna joined Acme Robotics in London."
doc = nlp(text)

print(type(nlp))
print(type(doc))
print(type(doc[0]))
print(type(doc[0:2]))
```

The official API describes `Doc` as a container for linguistic annotations and a sequence of `Token` objects. `Token` represents an individual token such as a word, punctuation symbol, or whitespace-related unit.

---

## 5. Processing text

The main workflow is:

```python
doc = nlp(text)
```

When called on a string, spaCy:

1. tokenizes the text;
2. runs enabled pipeline components in order;
3. returns a processed `Doc`.

Example:

```python
text = (
    "In 2026, Anna joined Acme Robotics in London. "
    "She builds Python tools for language data."
)

doc = nlp(text)

for token in doc:
    print(token.text)
```

Teaching point:

`doc` is not just a list of strings. It is a structured object containing token text, lemmas, POS tags, dependencies, entity annotations, sentence boundaries, and other information depending on the loaded pipeline.

---

## 6. Tokenization

Tokenization splits text into meaningful segments.

```python
for token in doc:
    print(token.text, token.idx)
```

Useful token attributes:

| Attribute | Meaning |
| --- | --- |
| `token.text` | original token text |
| `token.idx` | character offset in original text |
| `token.is_alpha` | whether token consists of alphabetic characters |
| `token.is_punct` | whether token is punctuation |
| `token.like_num` | whether token resembles a number |
| `token.is_stop` | whether token is marked as a stop word |

spaCy tokenization is non-destructive. The official docs state that the original text can be reconstructed from tokenized output, so `doc.text == input_text` should hold.

```python
print(doc.text == text)
```

This matters for annotation tasks because character offsets can be preserved.

---

## 7. Sentence segmentation

Sentences are available through `doc.sents`.

```python
for sent in doc.sents:
    print(sent.text)
```

`doc.sents` yields `Span` objects, not plain strings.

```python
for sent in doc.sents:
    print(type(sent), sent.start, sent.end, sent.text)
```

In many trained English pipelines, sentence boundaries are provided by the dependency parser. spaCy also has rule-based sentence segmentation components, such as `sentencizer`, for workflows that do not need a full parser.

---

## 8. Lemmas, POS tags, and morphology

spaCy makes common linguistic annotations available as token attributes.

```python
for token in doc:
    print(
        token.text,
        token.lemma_,
        token.pos_,
        token.tag_,
        token.morph,
    )
```

Important attributes:

| Attribute | Meaning |
| --- | --- |
| `token.lemma_` | base form |
| `token.pos_` | coarse-grained part of speech |
| `token.tag_` | fine-grained POS tag |
| `token.morph` | morphological features |

Example teaching discussion:

- `joined` may have lemma `join`.
- `builds` may have lemma `build`.
- `Anna` may be tagged as a proper noun.
- `2026` may be tagged as a number.

The exact result depends on the trained pipeline.

---

## 9. Dependency parsing

Dependency parsing identifies grammatical relations between tokens.

```python
for token in doc:
    print(token.text, token.dep_, token.head.text)
```

Useful attributes:

| Attribute | Meaning |
| --- | --- |
| `token.dep_` | dependency relation label |
| `token.head` | syntactic head token |
| `token.children` | tokens syntactically dependent on this token |
| `token.ancestors` | chain of heads above this token |
| `token.subtree` | token and syntactic descendants |

Example:

```python
for token in doc:
    if token.dep_ in {"nsubj", "dobj", "pobj"}:
        print(token.text, token.dep_, "->", token.head.text)
```

Dependency parses are useful for information extraction. For example, if an entity is an amount of money, dependency links can help identify the noun phrase it refers to. The official spaCy linguistic features documentation gives this as a typical dependency parsing use case.

---

## 10. Noun chunks

Noun chunks are base noun phrases.

```python
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
```

Example noun chunks in the sample text may include:

- `Anna`
- `Acme Robotics`
- `London`
- `She`
- `Python tools`
- `language data`

Noun chunks are convenient for quick phrase extraction. They are based on the dependency parse, so they require a pipeline with parser support.

---

## 11. Named entity recognition

Named Entity Recognition identifies spans that refer to named or numeric entities.

```python
for ent in doc.ents:
    print(ent.text, ent.label_, ent.start_char, ent.end_char)
```

Common English entity labels include:

| Label | Meaning |
| --- | --- |
| `PERSON` | person |
| `ORG` | organization |
| `GPE` | country, city, state |
| `LOC` | non-GPE location |
| `DATE` | date or period |
| `TIME` | time |
| `MONEY` | monetary value |
| `PRODUCT` | product |
| `EVENT` | named event |

The official spaCy docs emphasize that NER is statistical and depends on training examples. Students should inspect results and expect errors for unusual names, domain-specific vocabulary, or short ambiguous text.

---

## 12. Visualizing with displaCy

spaCy includes visualizers for dependencies and named entities.

In a notebook:

```python
from spacy import displacy

displacy.render(doc, style="ent", jupyter=True)
```

For dependency visualization:

```python
displacy.render(doc, style="dep", jupyter=True)
```

Use visualizations sparingly in the notebook:

- They are excellent for demonstrating parser output.
- They can become wide or hard to read for long sentences.
- Short examples work best.

---

## 13. Rule-based matching with `Matcher`

The `Matcher` finds token patterns. It is useful when a rule is clearer than a statistical model.

```python
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

pattern = [
    {"LOWER": "python"},
    {"LOWER": {"IN": ["course", "notebook", "tools"]}},
]

matcher.add("PYTHON_TERM", [pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    label = nlp.vocab.strings[match_id]
    print(label, span.text)
```

Teaching points:

- Patterns are lists of token constraints.
- The matcher returns match id, start token index, and end token index.
- `doc[start:end]` creates a `Span`.
- Rule-based matching is useful for predictable terms, product names, course-specific vocabulary, or domain phrases.

The official spaCy rule-based matching documentation explains that matcher patterns operate over token attributes and return `(match_id, start, end)` tuples.

---

## 14. Rule-based entities with `EntityRuler`

`EntityRuler` adds entity spans from patterns and dictionaries.

```python
nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "COURSE", "pattern": "Python course"},
    {"label": "TOPIC", "pattern": "language data"},
]

ruler.add_patterns(patterns)

doc = nlp("This Python course includes language data examples.")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

When to use `EntityRuler`:

- course-specific terms;
- product catalogs;
- known organization names;
- dictionaries of domain entities;
- correcting or supplementing statistical NER.

Pipeline order matters. If the ruler is added before `ner`, the statistical NER component can see existing entities. If it is added after `ner`, it can add or overwrite matches depending on configuration.

---

## 15. Batch processing

For many texts, use `nlp.pipe()` instead of calling `nlp()` repeatedly.

```python
texts = [
    "Anna joined Acme Robotics.",
    "Python is useful for language data.",
    "The workshop takes place in London.",
]

for doc in nlp.pipe(texts):
    print([(ent.text, ent.label_) for ent in doc.ents])
```

The official spaCy processing pipeline documentation recommends `nlp.pipe()` for stream and batch processing because it is usually more efficient.

If only named entities are needed, disable unnecessary components:

```python
for doc in nlp.pipe(texts, disable=["tagger", "parser", "lemmatizer"]):
    print(doc.ents)
```

Use this carefully:

- disabling `parser` removes dependency parse and noun chunks;
- disabling `tagger` removes POS tags;
- disabling components can speed up processing but removes annotations.

---

## 16. Inspecting the pipeline

Students should learn how to inspect what the pipeline contains.

```python
print(nlp.pipe_names)
print(nlp.pipeline)
```

Analyze component requirements:

```python
nlp.analyze_pipes(pretty=True)
```

The official docs explain that trained pipelines typically include components such as:

- tokenizer
- tagger
- parser
- named entity recognizer
- lemmatizer
- text categorizer, if present
- custom components, if added

The tokenizer is special: it converts a string into a `Doc` and is not listed like ordinary pipeline components in `nlp.pipe_names`.

---

## 17. Custom pipeline components

A custom component is a function that receives a `Doc`, modifies it, and returns it.

```python
from spacy.language import Language

@Language.component("course_flagger")
def course_flagger(doc):
    doc._.has_python = any(token.lower_ == "python" for token in doc)
    return doc
```

To use custom extension attributes:

```python
from spacy.tokens import Doc

Doc.set_extension("has_python", default=False, force=True)
nlp.add_pipe("course_flagger", last=True)

doc = nlp("This Python notebook introduces NLP.")
print(doc._.has_python)
```

This is optional for the bonus notebook. It is useful as an advanced note if students have already seen functions and decorators.

---

## 18. Common problems and fixes

### `OSError: Can't find model 'en_core_web_sm'`

Cause: spaCy is installed, but the English pipeline package is not.

Fix:

```bash
python -m spacy download en_core_web_sm
```

### The command `spacy` is not found

Fix: use:

```bash
python -m spacy download en_core_web_sm
python -m spacy validate
```

This uses the spaCy installed in the active Python environment.

### No named entities appear

Possible causes:

- the text has no recognizable entities;
- the pipeline has no `ner` component;
- the `ner` component was disabled;
- the entity is outside the model's training distribution.

Check:

```python
print(nlp.pipe_names)
```

### No noun chunks are available

Possible causes:

- the pipeline does not include a parser;
- the parser was disabled.

Noun chunks require syntactic analysis.

### Results differ from examples online

Possible causes:

- different spaCy version;
- different pipeline package;
- different model version;
- different tokenization;
- different custom components.

Use:

```python
import spacy

print(spacy.__version__)
print(nlp.meta)
```

---

## 19. When to use spaCy

Use spaCy when you want to:

- process text through a complete NLP pipeline;
- extract named entities;
- inspect dependencies and noun chunks;
- write rule-based matchers over token attributes;
- combine statistical predictions with dictionary rules;
- process many texts efficiently;
- build production-style NLP workflows.

Use NLTK instead, or in addition, when you want to:

- teach classic NLP algorithms step by step;
- work with built-in corpora;
- demonstrate stemming and WordNet lemmatization explicitly;
- build small feature-dictionary classifiers;
- show how tagging and chunking can be separate tasks.

---

## 20. Suggested spaCy notebook exercises

### Exercise 1: Inspect tokens

Process a paragraph and print:

- token text
- lemma
- POS tag
- dependency label
- head token

### Exercise 2: Extract entities

Use a short news-style paragraph and extract all entities with labels and character offsets.

### Exercise 3: Find noun chunks

Print all noun chunks and their syntactic heads.

### Exercise 4: Match course phrases

Create a `Matcher` pattern that finds:

- `Python course`
- `Python notebook`
- `language data`

### Exercise 5: Add custom entities

Use `EntityRuler` to mark `LU Python course` as `COURSE`.

### Exercise 6: Batch process texts

Create a list of 5 short texts and use `nlp.pipe()` to extract entities from all of them.

---

## 21. Minimal full example

```python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

text = (
    "Anna joined Acme Robotics in London. "
    "She builds Python tools for language data."
)

doc = nlp(text)

print("Tokens")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_, token.head.text)

print("\nSentences")
for sent in doc.sents:
    print(sent.text)

print("\nEntities")
for ent in doc.ents:
    print(ent.text, ent.label_)

print("\nNoun chunks")
for chunk in doc.noun_chunks:
    print(chunk.text)

matcher = Matcher(nlp.vocab)
matcher.add(
    "PYTHON_TERM",
    [[{"LOWER": "python"}, {"LOWER": {"IN": ["tools", "course", "notebook"]}}]],
)

print("\nMatches")
for match_id, start, end in matcher(doc):
    print(nlp.vocab.strings[match_id], doc[start:end].text)
```

---

## 22. Authoritative references

Primary spaCy documentation:

- spaCy official site: <https://spacy.io/>
- spaCy installation: <https://spacy.io/usage>
- spaCy models and languages: <https://spacy.io/usage/models>
- spaCy linguistic features: <https://spacy.io/usage/linguistic-features>
- spaCy processing pipelines: <https://spacy.io/usage/processing-pipelines>
- spaCy rule-based matching: <https://spacy.io/usage/rule-based-matching>
- spaCy visualizers: <https://spacy.io/usage/visualizers>
- spaCy `Doc` API: <https://spacy.io/api/doc>
- spaCy `Token` API: <https://spacy.io/api/token>
- spaCy `Matcher` API: <https://spacy.io/api/matcher>
- spaCy `EntityRuler` API: <https://spacy.io/api/entityruler>

Authoritative NLP references:

- Daniel Jurafsky and James H. Martin, *Speech and Language Processing*, 3rd edition draft, online manuscript released January 6, 2026: <https://web.stanford.edu/~jurafsky/slp3/>
- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schuetze, *Introduction to Information Retrieval*, tokenization chapter: <https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html>
- Manning, Raghavan, and Schuetze, stemming and lemmatization section: <https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html>
