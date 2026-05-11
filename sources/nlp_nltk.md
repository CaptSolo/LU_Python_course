# NLP with NLTK

This document provides detailed background for the NLTK part of an English-language bonus notebook on Natural Language Processing.

Verification note: technical claims and references in this document were checked on 2026-05-11 against official NLTK documentation and authoritative NLP references listed at the end of the file.

---

## 1. What NLTK is good for

NLTK, the Natural Language Toolkit, is a Python library for working with human language data. The official NLTK documentation describes it as a platform with interfaces to many corpora and lexical resources, including WordNet, and libraries for classification, tokenization, stemming, tagging, parsing, and related tasks.

For a Python course, NLTK is especially useful because it makes classic NLP steps visible:

- tokenization as a separate function call
- stop word filtering as a list operation
- stemming as an explicit algorithm
- lemmatization through WordNet
- POS tagging as a list of `(word, tag)` tuples
- named entity chunking as a tree
- frequency analysis as counters and distributions
- classification as feature dictionaries and labels

NLTK is a strong teaching library because students can inspect intermediate Python objects instead of only seeing the final output of a large pipeline.

---

## 2. Installation and data

Install NLTK with pip:

```bash
pip install nltk
```

NLTK code often needs separate data packages. This is intentional: the Python package and the data resources are distributed separately.

For the proposed English notebook, use:

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

What these resources support:

| Resource | Used for |
| --- | --- |
| `punkt_tab` | sentence and word tokenization data in current NLTK releases |
| `averaged_perceptron_tagger_eng` | English POS tagging |
| `maxent_ne_chunker_tab` | named entity chunking |
| `words` | word list used by NER examples |
| `wordnet` | WordNet lexical database interface |
| `omw-1.4` | Open Multilingual WordNet data used with WordNet |
| `stopwords` | common stop word lists |
| `universal_tagset` | mapping from detailed POS tags to the universal POS tagset |

Practical compatibility note:

Some older NLTK examples use resource names such as `punkt`, `averaged_perceptron_tagger`, and `maxent_ne_chunker`. Current NLTK 3.9.x examples and errors may request the newer `_tab` or `_eng` package names. If a notebook raises `LookupError`, students should read the error message and download the resource named there.

---

## 3. Example text for demonstrations

Use a short English text that contains names, places, verbs, punctuation, and repeated words:

```python
text = (
    "In 2026, Anna joined Acme Robotics in London. "
    "She builds Python tools for language data, and she enjoys teaching Python."
)
```

This text supports several tasks:

- sentence splitting
- word tokenization
- lowercasing
- stop word removal
- stemming
- lemmatization
- POS tagging
- named entity chunking
- frequency counting

---

## 4. Sentence and word tokenization

Tokenization splits text into units that later NLP steps can process.

```python
from nltk.tokenize import sent_tokenize, word_tokenize

sentences = sent_tokenize(text)
tokens = word_tokenize(text)

print(sentences)
print(tokens)
```

Expected teaching points:

- Sentence tokenization is not the same as splitting on every period.
- Word tokenization is not the same as `text.split()`.
- Punctuation can be returned as separate tokens.
- Contractions may be split into multiple tokens depending on tokenizer rules.

For specialized tokenization, NLTK also provides classes such as:

- `RegexpTokenizer` for custom regular-expression tokenization.
- `TweetTokenizer` for social media style text.
- `WhitespaceTokenizer` for simple whitespace splitting.
- `TreebankWordTokenizer`, the tokenizer behind many English examples.

Example with a regular expression tokenizer:

```python
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r"[A-Za-z]+")
word_tokens = tokenizer.tokenize(text)

print(word_tokens)
```

This example keeps alphabetic words and drops punctuation and numbers. It is useful for word-frequency examples, but it would be too destructive for NER, URLs, or code snippets.

---

## 5. Lowercasing and simple normalization

Normalization makes tokens easier to compare.

```python
tokens_lower = [token.lower() for token in tokens]
print(tokens_lower)
```

Lowercasing is useful for counting words:

```python
"Python" == "python"  # False
"Python".lower() == "python"  # True
```

But lowercasing can lose information:

- `Apple` may be a company.
- `apple` may be a fruit.
- `US` and `us` are different.
- Proper nouns often rely on capitalization.

Use lowercasing when the task benefits from it, not as an automatic habit.

---

## 6. Stop words

Stop words are common words that are sometimes removed before counting or indexing.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
tokens = word_tokenize(text)

filtered = [
    token
    for token in tokens
    if token.lower() not in stop_words and token.isalpha()
]

print(filtered)
```

Teaching points:

- Stop word removal is useful for simple keyword counts.
- It is not always appropriate.
- Removing `not` can damage sentiment analysis.
- Removing `of` and `the` can damage phrase search and names.

The Stanford *Introduction to Information Retrieval* discusses why stop word removal can reduce index size, but also why it can harm phrase queries and some special searches.

---

## 7. Frequency analysis

NLTK provides `FreqDist`, a frequency distribution class built for counting observed samples.

```python
from nltk.probability import FreqDist

fdist = FreqDist(token.lower() for token in filtered)

print(fdist.most_common(10))
print(fdist["python"])
```

Frequency analysis is a good bridge from regular Python dictionaries and counters to text analysis.

Useful questions for students:

- Which words occur most often?
- What changes when stop words are removed?
- What changes when words are lowercased?
- What changes when stemming or lemmatization is applied first?

---

## 8. Stemming

Stemming reduces words to stems, usually with heuristic suffix rules.

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["connect", "connected", "connecting", "connection", "connections"]
stems = [(word, stemmer.stem(word)) for word in words]

print(stems)
```

Typical teaching points:

- Stems are not always dictionary words.
- Stemming can group related forms quickly.
- Stemming may over-combine words that should stay distinct.
- Stemming is common in information retrieval examples.

The Stanford information retrieval book explains the difference between stemming and lemmatization: stemming is usually a cruder heuristic process, while lemmatization aims for a dictionary form using vocabulary and morphological analysis.

---

## 9. Lemmatization with WordNet

Lemmatization returns a base or dictionary form.

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["cars", "running", "better", "was"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
```

Important point: `WordNetLemmatizer.lemmatize()` assumes nouns by default. For better results, pass part of speech where possible.

```python
print(lemmatizer.lemmatize("running", pos="v"))  # run
print(lemmatizer.lemmatize("better", pos="a"))   # good
print(lemmatizer.lemmatize("was", pos="v"))      # be
```

For notebook exercises, compare stemming and lemmatization:

```python
words = ["studies", "studying", "studied", "better", "organization"]

for word in words:
    stem = stemmer.stem(word)
    lemma_noun = lemmatizer.lemmatize(word)
    lemma_verb = lemmatizer.lemmatize(word, pos="v")
    print(word, stem, lemma_noun, lemma_verb)
```

---

## 10. Part-of-speech tagging

Part-of-speech tagging assigns grammatical labels to tokens.

```python
from nltk import pos_tag
from nltk.tokenize import word_tokenize

tokens = word_tokenize(text)
tagged = pos_tag(tokens)

print(tagged)
```

Example output shape:

```text
[("In", "IN"), ("2026", "CD"), (",", ","), ("Anna", "NNP"), ...]
```

Common Penn Treebank-style tags:

| Tag | Meaning | Example |
| --- | --- | --- |
| `NN` | noun, singular or mass | `course` |
| `NNS` | noun, plural | `tools` |
| `NNP` | proper noun, singular | `Anna` |
| `VB` | verb, base form | `build` |
| `VBD` | verb, past tense | `joined` |
| `VBG` | verb, gerund or present participle | `teaching` |
| `JJ` | adjective | `useful` |
| `RB` | adverb | `quickly` |
| `IN` | preposition or subordinating conjunction | `in`, `for` |
| `DT` | determiner | `the`, `a` |
| `CD` | cardinal number | `2026` |

NLTK also supports the universal tagset:

```python
tagged_universal = pos_tag(tokens, tagset="universal")
print(tagged_universal)
```

For multiple sentences, use `pos_tag_sents()` rather than calling `pos_tag()` repeatedly:

```python
from nltk import pos_tag_sents

tokenized_sentences = [word_tokenize(sentence) for sentence in sent_tokenize(text)]
tagged_sentences = pos_tag_sents(tokenized_sentences)
```

---

## 11. Chunking

Chunking groups tagged tokens into shallow phrases. A common teaching example is noun phrase chunking.

```python
import nltk

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(tagged)

print(tree)
```

The grammar says:

- optional determiner: `<DT>?`
- zero or more adjectives: `<JJ.*>*`
- one or more nouns or proper nouns: `<NN.*>+`

This is a useful demonstration because students can see how POS tags and regular-expression-like rules combine.

Limitations:

- Rule-based chunking is brittle.
- It depends on correct POS tags.
- It captures shallow phrases, not full syntax.
- Complex grammar needs more robust parsing tools.

---

## 12. Named entity chunking

NLTK includes a named entity chunker.

```python
from nltk.chunk import ne_chunk

entities = ne_chunk(tagged)
print(entities)
```

The result is an NLTK tree. Named entity subtrees may have labels such as:

- `PERSON`
- `ORGANIZATION`
- `GPE`
- `LOCATION`
- `FACILITY`

To extract entity text:

```python
for node in entities:
    if hasattr(node, "label"):
        entity_text = " ".join(token for token, tag in node.leaves())
        print(entity_text, node.label())
```

Teaching caution:

NLTK named entity chunking is useful for showing the concept, but spaCy is usually more convenient for entity extraction in modern Python workflows.

---

## 13. WordNet

WordNet is a lexical database of English. Princeton WordNet groups nouns, verbs, adjectives, and adverbs into sets of cognitive synonyms called synsets, and links those synsets through conceptual-semantic and lexical relations.

NLTK provides an interface to WordNet:

```python
from nltk.corpus import wordnet as wn

synsets = wn.synsets("course")

for synset in synsets[:5]:
    print(synset.name(), "-", synset.definition())
```

Useful WordNet ideas:

- synonym sets, or synsets
- definitions, also called glosses
- examples
- hypernyms, more general terms
- hyponyms, more specific terms
- lemmas

Example:

```python
dog = wn.synset("dog.n.01")

print(dog.definition())
print(dog.hypernyms())
print(dog.hyponyms()[:5])
```

For an introductory course, WordNet is best presented as a structured lexical resource, not as a complete model of meaning.

---

## 14. Concordance and corpus-style exploration

NLTK can wrap a list of tokens in `nltk.Text` to support classic corpus exploration.

```python
from nltk.text import Text

tokens = word_tokenize(text)
nltk_text = Text(tokens)

nltk_text.concordance("Python")
nltk_text.similar("Python")
```

This is especially useful when working with larger corpora. For a short notebook, it can be shown briefly and then connected to NLTK's built-in corpora.

Example with the Brown Corpus:

```python
import nltk
nltk.download("brown")

from nltk.corpus import brown

words = brown.words(categories="news")
fdist = FreqDist(word.lower() for word in words if word.isalpha())

print(fdist.most_common(20))
```

---

## 15. Simple text classification

NLTK includes classifiers, including Naive Bayes.

For a small teaching example, use hand-written training data:

```python
from nltk.classify import NaiveBayesClassifier

training_data = [
    ("I love this course", "positive"),
    ("This notebook is helpful", "positive"),
    ("Python examples are clear", "positive"),
    ("I dislike this task", "negative"),
    ("This explanation is confusing", "negative"),
    ("The exercise is too hard", "negative"),
]

def document_features(sentence):
    words = set(word.lower() for word in word_tokenize(sentence) if word.isalpha())
    return {
        "contains_python": "python" in words,
        "contains_helpful": "helpful" in words,
        "contains_confusing": "confusing" in words,
        "contains_hard": "hard" in words,
        "contains_love": "love" in words,
        "contains_dislike": "dislike" in words,
    }

featuresets = [
    (document_features(sentence), label)
    for sentence, label in training_data
]

classifier = NaiveBayesClassifier.train(featuresets)

test_sentence = "This Python notebook is helpful"
print(classifier.classify(document_features(test_sentence)))
classifier.show_most_informative_features()
```

Teaching points:

- Classifiers need labeled examples.
- A feature extractor converts text into dictionaries.
- Small toy datasets are only for learning the mechanics.
- Real classification needs more data, train/test splits, and evaluation.

---

## 16. Good notebook exercises

### Exercise 1: Tokenize and count

Given a paragraph, tokenize it, remove punctuation, lowercase words, and print the 10 most common words.

### Exercise 2: Stop word effect

Count words before and after stop word removal. Explain what changed.

### Exercise 3: Stemming vs. lemmatization

Compare stems and lemmas for:

```python
["runs", "running", "ran", "studies", "studied", "better", "cars"]
```

### Exercise 4: POS tag inspection

Tag a sentence and print only nouns and verbs.

### Exercise 5: Named entities

Extract named entities from:

```text
Marie Curie worked in Paris and won the Nobel Prize.
```

### Exercise 6: Mini classifier

Create 10 short positive and negative training sentences, train a Naive Bayes classifier, and test it on 3 new sentences.

---

## 17. Common problems and fixes

### `LookupError: Resource not found`

Cause: an NLTK data package is missing.

Fix:

```python
import nltk
nltk.download("resource_name_from_error_message")
```

Use the exact resource name shown in the error.

### Lemmatizer returns the same word

Cause: `WordNetLemmatizer` assumes nouns unless a POS is supplied.

Fix:

```python
lemmatizer.lemmatize("running", pos="v")
```

### Stop word removal removes meaningful words

Cause: stop word lists are general-purpose, not task-specific.

Fix: inspect the stop word list and customize it.

```python
custom_stop_words = set(stopwords.words("english"))
custom_stop_words.discard("not")
```

### POS tags look cryptic

Cause: default English POS tags use Penn Treebank-style labels.

Fix: use `tagset="universal"` for simpler labels:

```python
pos_tag(tokens, tagset="universal")
```

---

## 18. When to use NLTK

Use NLTK when you want to:

- teach individual NLP concepts;
- inspect intermediate Python data structures;
- work with classic corpora;
- use WordNet;
- demonstrate stemming and lemmatization;
- build a simple classifier from feature dictionaries;
- explain how POS tags and chunking rules work.

Use spaCy instead, or in addition, when you want:

- fast processing of many documents;
- a single pipeline for tokenization, POS tagging, parsing, lemmatization, and NER;
- convenient entity extraction;
- dependency parsing;
- production-style batch processing.

---

## 19. Authoritative references

Primary NLTK documentation:

- NLTK official documentation: <https://www.nltk.org/>
- NLTK installation: <https://www.nltk.org/install.html>
- NLTK data installation: <https://www.nltk.org/data.html>
- NLTK tokenizer API: <https://www.nltk.org/api/nltk.tokenize.html>
- NLTK stemmer API: <https://www.nltk.org/api/nltk.stem.html>
- NLTK POS tagging API: <https://www.nltk.org/api/nltk.tag.html>
- NLTK chunking API: <https://www.nltk.org/api/nltk.chunk.html>
- NLTK `FreqDist` API: <https://www.nltk.org/api/nltk.probability.FreqDist.html>
- NLTK classifier API: <https://www.nltk.org/api/nltk.classify.html>
- NLTK Naive Bayes classifier API: <https://www.nltk.org/api/nltk.classify.naivebayes.html>
- NLTK WordNet how-to: <https://www.nltk.org/howto/wordnet.html>
- NLTK Book, *Natural Language Processing with Python*: <https://www.nltk.org/book/>

Authoritative NLP and lexical references:

- Princeton WordNet: <https://wordnet.princeton.edu/>
- Daniel Jurafsky and James H. Martin, *Speech and Language Processing*, 3rd edition draft, online manuscript released January 6, 2026: <https://web.stanford.edu/~jurafsky/slp3/>
- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schuetze, *Introduction to Information Retrieval*, tokenization chapter: <https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html>
- Manning, Raghavan, and Schuetze, stop words section: <https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html>
- Manning, Raghavan, and Schuetze, stemming and lemmatization section: <https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html>
