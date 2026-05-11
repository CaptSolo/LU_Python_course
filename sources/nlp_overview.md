# Natural Language Processing in Python: Overview

This document is background material for an English-language bonus notebook on Natural Language Processing (NLP) techniques in Python.

Verification note: technical claims and references in this document were checked on 2026-05-11 against official project documentation and authoritative NLP references listed at the end of the file.

---

## 1. Scope

Natural Language Processing is the area of computing concerned with representing, processing, analyzing, and generating human language. In an introductory Python course, NLP is best presented as a practical workflow:

1. Start with raw text.
2. Split it into useful units.
3. Normalize or annotate those units.
4. Extract information or build simple models.
5. Interpret the result carefully, because NLP output is often probabilistic or rule-dependent.

The proposed notebook should focus on English examples and two Python libraries:

- **NLTK** for teaching, corpora, classic NLP techniques, and transparent algorithmic examples.
- **spaCy** for modern pipeline-based processing, fast annotation, information extraction, and production-style workflows.

This bonus topic should not try to cover every part of modern NLP. Large language models, transformers, embeddings, and deep learning can be mentioned as next steps, but the main notebook should stay grounded in core text-processing tasks that students can understand from Python basics.

---

## 2. Suggested notebook identity

Recommended filename:

```text
notebooks/bonus_topic_1_nlp_techniques.ipynb
```

Recommended notebook title:

```text
Bonus Topic 1 - Natural Language Processing with NLTK and spaCy
```

Reasoning:

- The existing course syllabus is organized by teaching weeks and currently reaches Week 15.
- NLP is an extra topic, not a Week 16 lesson.
- `bonus_topic_1_nlp_techniques.ipynb` clearly communicates that the material is optional and expandable.
- If later bonus notebooks are added, the naming can continue as `bonus_topic_2_...`, `bonus_topic_3_...`.

---

## 3. Core NLP pipeline

A typical NLP pipeline converts raw strings into structured information.

```text
Raw text
  -> sentence segmentation
  -> tokenization
  -> normalization
  -> linguistic annotation
  -> extraction, counting, classification, or search
```

Example raw text:

```text
In 2026, Anna joined Acme Robotics in London. She builds Python tools for language data.
```

Possible structured output:

- Sentences:
  - `In 2026, Anna joined Acme Robotics in London.`
  - `She builds Python tools for language data.`
- Tokens:
  - `In`, `2026`, `,`, `Anna`, `joined`, `Acme`, `Robotics`, ...
- Lemmas:
  - `join` for `joined`
  - `build` for `builds`
- Part-of-speech tags:
  - `Anna` as a proper noun
  - `joined` as a verb
- Named entities:
  - `Anna` as a person
  - `Acme Robotics` as an organization, depending on the model
  - `London` as a geopolitical entity or location

The important teaching point is that the computer does not automatically "understand" the text in a human sense. It applies rules, statistical models, lexical resources, or trained pipelines to produce useful annotations.

---

## 4. Essential terminology

| Term | Practical meaning | Example |
| --- | --- | --- |
| Corpus | A collection of texts used for analysis or training | product reviews, news articles, books |
| Document | One text unit in a corpus | one review, one email, one article |
| Sentence segmentation | Splitting text into sentences | `Hello. I am here.` -> two sentences |
| Tokenization | Splitting text into meaningful pieces | `don't` may become `do` + `n't` depending on tokenizer |
| Token | One processed unit of text | word, punctuation mark, number |
| Type | A unique token form | `cat` as a vocabulary item |
| Normalization | Making forms more comparable | lowercasing, removing punctuation, lemmatizing |
| Stop word | Very common word sometimes removed for search or counting | `the`, `and`, `of` |
| Stem | A reduced word form, often produced by heuristic suffix removal | `running` -> `run` or `runn` depending on stemmer |
| Lemma | Dictionary or base form | `was` -> `be`, `cars` -> `car` |
| POS tag | Part-of-speech label | noun, verb, adjective |
| Chunk | Shallow phrase group | noun phrase such as `the red car` |
| Named entity | Named real-world object or value | person, organization, place, date |
| Dependency parse | Grammatical links between words | subject, object, modifier |
| Feature | Input signal used by a classifier | whether a word appears in a document |

---

## 5. Common NLP use cases

### Search and retrieval

NLP can prepare text for search by tokenizing, normalizing, removing selected terms, or extracting keywords. Search systems must be careful: removing common words can help some keyword searches, but it can harm phrase searches such as `President of the United States`.

### Information extraction

NLP can extract structured facts from text:

- people
- organizations
- places
- dates
- product names
- amounts of money
- noun phrases
- simple relation patterns

spaCy is especially useful here because it combines tokenization, part-of-speech tagging, dependency parsing, named entity recognition, and rule-based matching in one pipeline.

### Corpus exploration

For teaching and research, NLTK is useful for:

- loading sample corpora
- counting words
- finding concordance lines
- studying collocations
- comparing stemmers and lemmatizers
- building simple classifiers

### Text classification

Text classification assigns labels to texts:

- spam vs. not spam
- positive vs. negative review
- topic category
- language identification
- intent category

For an introductory notebook, a small Naive Bayes classifier is a good teaching example because it connects directly to dictionaries, counters, and feature functions.

### Data cleaning

NLP tools can help clean text data before analysis:

- remove or keep punctuation consistently
- normalize case
- split sentences
- identify words vs. numbers vs. symbols
- remove boilerplate
- detect text that should not be processed

Cleaning rules must match the task. For example, removing punctuation may be fine for word frequency counts but bad for named entities, contractions, code snippets, or URLs.

---

## 6. NLTK and spaCy at a glance

| Question | NLTK | spaCy |
| --- | --- | --- |
| Best teaching role | Classic NLP concepts, corpora, transparent algorithms | Modern NLP pipelines and structured annotations |
| Typical workflow | Call individual functions and classes | Load a pipeline and process text into `Doc` objects |
| Strengths | Corpora, tokenizers, stemmers, taggers, classifiers, linguistic teaching | Speed, production APIs, POS, dependencies, NER, rule-based matching |
| Data resources | Many corpora and lexical resources, including WordNet interfaces | Trained pipelines packaged as Python packages |
| Good first tasks | word counts, stemming, lemmatization, POS tagging, simple classification | entity extraction, noun chunks, dependency-based extraction, batch processing |
| Output style | Python lists, tuples, trees, frequency distributions | `Doc`, `Token`, `Span`, annotations, pipeline components |
| Main caution | Many functions require separate NLTK data downloads | Results depend on the installed trained pipeline |

The notebook should not frame one library as replacing the other. They serve different teaching purposes.

---

## 7. What students should learn

By the end of the bonus notebook, students should be able to:

1. Explain what tokenization, lemmatization, POS tagging, and named entity recognition do.
2. Use NLTK to tokenize text, remove stop words, stem, lemmatize, tag parts of speech, count words, and run simple classification examples.
3. Use spaCy to process English text with a trained pipeline.
4. Inspect spaCy `Doc`, `Token`, and `Span` objects.
5. Compare NLTK and spaCy results on the same text.
6. Choose a tool based on the task instead of memorizing one "best" library.
7. Recognize that NLP output may be wrong and should be checked against the use case.

---

## 8. Recommended notebook structure

### Section 1: Introduction

- What NLP is.
- Where students encounter NLP in real systems.
- Why text is harder than numbers and tables.
- The same English example text used throughout the notebook.

### Section 2: Setup

Recommended setup cells:

```python
# Install packages if needed:
# pip install nltk spacy
# python -m spacy download en_core_web_sm
```

For NLTK, data packages should be downloaded explicitly in the notebook so students see the dependency between code and data:

```python
import nltk

for package in [
    "punkt_tab",
    "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker_tab",
    "words",
    "wordnet",
    "omw-1.4",
    "stopwords",
    "universal_tagset",
]:
    nltk.download(package)
```

Practical note: older NLTK installations may ask for older package names such as `punkt` or `averaged_perceptron_tagger`. If a `LookupError` appears, students should read the error message and download the resource named by their installed NLTK version.

### Section 3: NLTK basics

- `sent_tokenize`
- `word_tokenize`
- `stopwords`
- `PorterStemmer`
- `WordNetLemmatizer`
- `pos_tag`
- `ne_chunk`
- `FreqDist`

### Section 4: spaCy basics

- `spacy.load("en_core_web_sm")`
- `doc = nlp(text)`
- `Token.text`, `Token.lemma_`, `Token.pos_`, `Token.dep_`
- `doc.sents`
- `doc.ents`
- `doc.noun_chunks`
- `Matcher`
- `EntityRuler`
- `displacy`

### Section 5: Side-by-side comparison

Use the same English paragraph and compare:

- tokens
- lemmas
- POS tags
- named entities
- strengths and limitations

### Section 6: Exercises

Suggested exercises:

1. Tokenize a short product review.
2. Remove stop words and count the most frequent content words.
3. Compare stemming and lemmatization for a list of verbs.
4. Extract named entities from a short news-style paragraph.
5. Use spaCy to list noun chunks.
6. Write a spaCy matcher pattern for mentions of `Python course`, `Python notebook`, or `language data`.
7. Build a tiny NLTK classifier from hand-written positive and negative sentences.

---

## 9. Important cautions

### Tokenization is not trivial

Even English has ambiguous tokenization cases:

- contractions: `don't`, `isn't`
- names: `O'Neill`
- hyphenation: `state-of-the-art`
- programming terms: `C++`, `C#`
- URLs and email addresses
- dates and phone numbers

A good tokenizer is task-aware. The "right" tokenization for search may differ from the "right" tokenization for grammar analysis.

### Stop word removal is task-dependent

Stop word removal can simplify word frequency examples, but it is not always correct. It can damage:

- phrase search
- negation handling, such as `not good`
- names and titles
- legal or academic text

For teaching, stop word removal should be introduced as a tool, not a universal rule.

### Stemming and lemmatization are different

Stemming usually uses heuristic word reductions. Lemmatization tries to return a dictionary form and often needs vocabulary and part-of-speech information. Stemming can increase recall in search, but it can also merge words that should remain separate.

### Named entity recognition is not guaranteed

NER systems are useful, but model output can be wrong. Errors are common with:

- unfamiliar names
- domain-specific terms
- ambiguous organization and product names
- unusual capitalization
- short text without context

Students should inspect results and not assume that all entity labels are correct.

### Models and resources must be reproducible

NLP results depend on:

- package versions
- trained model versions
- downloaded corpora and taggers
- language settings
- preprocessing rules

For serious projects, record the versions of NLTK, spaCy, and the spaCy pipeline package.

---

## 10. Minimal comparison example

The same text can demonstrate the different style of each library.

```python
text = "Anna joined Acme Robotics in London. She builds Python tools for language data."
```

NLTK style:

```python
import nltk
from nltk.chunk import ne_chunk

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
entities = ne_chunk(tagged)

print(tokens)
print(tagged)
print(entities)
```

spaCy style:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)

for ent in doc.ents:
    print(ent.text, ent.label_)
```

Teaching contrast:

- NLTK exposes separate steps directly.
- spaCy packages processing into a pipeline and gives a rich annotated object.

---

## 11. Authoritative references

Primary library documentation:

- NLTK official documentation: <https://www.nltk.org/>
- NLTK installation: <https://www.nltk.org/install.html>
- NLTK data installation: <https://www.nltk.org/data.html>
- NLTK API reference: <https://www.nltk.org/api/nltk.html>
- NLTK Book, *Natural Language Processing with Python*: <https://www.nltk.org/book/>
- spaCy official site: <https://spacy.io/>
- spaCy installation: <https://spacy.io/usage>
- spaCy models and languages: <https://spacy.io/usage/models>
- spaCy linguistic features: <https://spacy.io/usage/linguistic-features>
- spaCy processing pipelines: <https://spacy.io/usage/processing-pipelines>
- spaCy rule-based matching: <https://spacy.io/usage/rule-based-matching>

Authoritative NLP references:

- Daniel Jurafsky and James H. Martin, *Speech and Language Processing*, 3rd edition draft, online manuscript released January 6, 2026: <https://web.stanford.edu/~jurafsky/slp3/>
- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schuetze, *Introduction to Information Retrieval*, tokenization chapter: <https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html>
- Manning, Raghavan, and Schuetze, stop words section: <https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html>
- Manning, Raghavan, and Schuetze, stemming and lemmatization section: <https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html>
- Princeton WordNet: <https://wordnet.princeton.edu/>
