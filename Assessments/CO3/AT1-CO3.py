# 1 — Unsmoothed N-gram Language Model
print("\nQuestion 1 Output: \n")
import re
from collections import Counter
# --------------------------------------------------
# Training Corpus
# --------------------------------------------------
corpus = """
The student is studying natural language processing.
The student is learning machine learning.
The student is reading a book.
The teacher is teaching the student.
The teacher is explaining language models.
The student is using Python.
The student is writing a program.
The student is solving a problem.
The student is preparing for an examination.
Machine learning is an interesting subject.
Natural language processing is a useful field.
Python is a popular programming language.
The teacher is using Python.
The student is learning Python programming.
"""
# --------------------------------------------------
# Preprocessing
# --------------------------------------------------
def tokenize(text):
    text = text.lower()
    sentences = re.split(r'[.!?]+', text)
    tokenized = []
    for sentence in sentences:
        words = re.findall(r'\b[a-z]+\b', sentence)
        if words:
            words = ["<s>"] + words + ["</s>"]
            tokenized.append(words)
    return tokenized
sentences = tokenize(corpus)
# --------------------------------------------------
# Count N-grams
# --------------------------------------------------
unigrams = Counter()
bigrams = Counter()
trigrams = Counter()
for sentence in sentences:
    unigrams.update(sentence)
    for i in range(len(sentence) - 1):
        bigrams[(sentence[i], sentence[i + 1])] += 1
    for i in range(len(sentence) - 2):
        trigrams[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1
# --------------------------------------------------
# Probability Functions
# --------------------------------------------------
def unigram_probability(word):
    return unigrams[word] / sum(unigrams.values())
def bigram_probability(word1, word2):
    if unigrams[word1] == 0:
        return 0
    return bigrams[(word1, word2)] / unigrams[word1]
def trigram_probability(word1, word2, word3):
    if bigrams[(word1, word2)] == 0:
        return 0
    return trigrams[(word1, word2, word3)] / bigrams[(word1, word2)]
# --------------------------------------------------
# Display Counts and Probabilities
# --------------------------------------------------
print("=" * 70)
print("N-GRAM LANGUAGE MODEL")
print("=" * 70)
print("\nChoose N:")
print("1. Unigram")
print("2. Bigram")
print("3. Trigram")
n = int(input("Enter N: "))
if n == 1:
    print("\nUNIGRAM COUNTS AND PROBABILITIES")
    print("-" * 50)
    total = sum(unigrams.values())
    for word, count in unigrams.most_common():
        probability = count / total
        print(f"{word:<20} Count={count:<5} Probability={probability:.4f}")
elif n == 2:
    print("\nBIGRAM COUNTS AND PROBABILITIES")
    print("-" * 60)
    for pair, count in bigrams.most_common():
        probability = bigram_probability(pair[0], pair[1])
        print(
            f"{pair[0]} {pair[1]:<20} "
            f"Count={count:<5} Probability={probability:.4f}"
        )
elif n == 3:
    print("\nTRIGRAM COUNTS AND PROBABILITIES")
    print("-" * 70)
    for tri, count in trigrams.most_common():
        probability = trigram_probability(tri[0], tri[1], tri[2])
        print(
            f"{tri[0]} {tri[1]} {tri[2]:<20} "
            f"Count={count:<5} Probability={probability:.4f}"
        )
else:
    print("Invalid N")
# --------------------------------------------------
# Top-5 Next Word Prediction
# --------------------------------------------------
def predict_next(sentence, n):
    words = re.findall(r'\b[a-z]+\b', sentence.lower())
    if n == 1:
        candidates = []
        for word, count in unigrams.items():
            if word not in ["<s>", "</s>"]:
                candidates.append(
                    (word, count / sum(unigrams.values()))
                )
        return sorted(candidates, key=lambda x: x[1], reverse=True)[:5]
    elif n == 2:
        if not words:
            return []
        previous = words[-1]
        candidates = []
        for (w1, w2), count in bigrams.items():
            if w1 == previous:
                probability = count / unigrams[w1]
                candidates.append((w2, probability))
        return sorted(
            candidates,
            key=lambda x: x[1],
            reverse=True
        )[:5]
    elif n == 3:
        if len(words) < 2:
            return []
        w1 = words[-2]
        w2 = words[-1]
        candidates = []
        for (a, b, c), count in trigrams.items():
            if a == w1 and b == w2:
                probability = count / bigrams[(a, b)]
                candidates.append((c, probability))
        return sorted(
            candidates,
            key=lambda x: x[1],
            reverse=True
        )[:5]
query = input("\nEnter incomplete sentence: ")
print("\nTop-5 Next Word Predictions:")
print("-" * 40)
predictions = predict_next(query, n)
if predictions:
    for word, probability in predictions:
        print(f"{word:<20} {probability:.4f}")
else:
    print("No prediction available.")
# --------------------------------------------------
# Demonstrate Zero Probability
# --------------------------------------------------
print("\nZero Probability Demonstration")
print("-" * 40)
print(
    "Bigram P(student -> football) =",
    bigram_probability("student", "football")
)
print(
    "Trigram P(student is football) =",
    trigram_probability("student", "is", "football")
)
# --------------------------------------------------
# Simple Evaluation
# --------------------------------------------------
test_sentences = [
    "The student is",
    "The teacher is",
    "Python is",
    "The student is learning"
]
print("\nEvaluation")
print("-" * 40)
correct = 0
total = 0
for sentence in test_sentences:
    words = sentence.lower().split()
    if n == 2 and len(words) >= 1:
        predictions = predict_next(sentence, 2)
        if predictions:
            predicted = predictions[0][0]
            print(sentence, "->", predicted)
            total += 1
    elif n == 3 and len(words) >= 2:
        predictions = predict_next(sentence, 3)
        if predictions:
            predicted = predictions[0][0]
            print(sentence, "->", predicted)
            total += 1
if total > 0:
    print("\nPredictions generated:", total)
# 2 - Smoothing, Backoff and Deleted Interpolation
print("\nQuestion 2 Output: \n")
import re
from collections import Counter
# --------------------------------------------------
# Corpus
# --------------------------------------------------
corpus = """
The student is studying natural language processing.
The student is learning machine learning.
The student is reading a book.
The student is using Python.
The student is writing a program.
The teacher is teaching the student.
The teacher is explaining language models.
The teacher is using Python.
Machine learning is an interesting subject.
Natural language processing is a useful field.
Python is a programming language.
The student is learning Python.
"""
# --------------------------------------------------
# Tokenization
# --------------------------------------------------
def tokenize(text):
    sentences = re.split(r'[.!?]+', text.lower())
    result = []
    for sentence in sentences:
        words = re.findall(r'\b[a-z]+\b', sentence)
        if words:
            result.append(["<s>"] + words + ["</s>"])
    return result
sentences = tokenize(corpus)
# --------------------------------------------------
# Count N-grams
# --------------------------------------------------
uni = Counter()
bi = Counter()
tri = Counter()
for sentence in sentences:
    uni.update(sentence)
    for i in range(len(sentence) - 1):
        bi[(sentence[i], sentence[i + 1])] += 1
    for i in range(len(sentence) - 2):
        tri[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1
total_words = sum(uni.values())
# --------------------------------------------------
# Unsmoothed probabilities
# --------------------------------------------------
def unigram(word):
    return uni[word] / total_words if uni[word] else 0
def bigram(w1, w2):
    if uni[w1] == 0:
        return 0
    return bi[(w1, w2)] / uni[w1]
def trigram(w1, w2, w3):
    if bi[(w1, w2)] == 0:
        return 0
    return tri[(w1, w2, w3)] / bi[(w1, w2)]
# --------------------------------------------------
# Backoff Model
# --------------------------------------------------
def backoff(w1, w2, w3):
    # Try trigram
    if tri[(w1, w2, w3)] > 0:
        return trigram(w1, w2, w3)
    # Back off to bigram
    if bi[(w2, w3)] > 0:
        return bigram(w2, w3)
    # Back off to unigram
    return unigram(w3)
# --------------------------------------------------
# Deleted Interpolation
# --------------------------------------------------
lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5
def interpolation(w1, w2, w3):
    p1 = unigram(w3)
    p2 = bigram(w2, w3)
    p3 = trigram(w1, w2, w3)
    return (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )
# --------------------------------------------------
# Prediction
# --------------------------------------------------
vocabulary = [
    word for word in uni
    if word not in ["<s>", "</s>"]
]
def predict(query):
    words = re.findall(r'\b[a-z]+\b', query.lower())
    if len(words) < 2:
        print("Enter at least two words.")
        return
    w1 = words[-2]
    w2 = words[-1]
    results = []
    for word in vocabulary:
        unsmoothed_probability = trigram(w1, w2, word)
        backoff_probability = backoff(w1, w2, word)
        interpolation_probability = interpolation(w1, w2, word)
        results.append((
            word,
            unsmoothed_probability,
            backoff_probability,
            interpolation_probability
        ))
    results.sort(key=lambda x: x[3], reverse=True)
    print("\nPrediction Results")
    print("-" * 75)
    print(
        f"{'Word':<15}"
        f"{'Unsmoothed':<15}"
        f"{'Backoff':<15}"
        f"{'Interpolation':<15}"
    )
    for result in results[:5]:
        print(
            f"{result[0]:<15}"
            f"{result[1]:<15.4f}"
            f"{result[2]:<15.4f}"
            f"{result[3]:<15.4f}"
        )
# --------------------------------------------------
# User Input
# --------------------------------------------------
print("=" * 70)
print("SMOOTHING AND BACKOFF LANGUAGE MODEL")
print("=" * 70)
query = input("Enter a sentence/query: ")
predict(query)
# 3 - N-gram Evaluation Using Entropy
print("\nQuestion 3 Output: \n")
import re
import math
from collections import Counter
# --------------------------------------------------
# Training Corpus
# --------------------------------------------------
training_corpus = """
The student is studying natural language processing.
The student is learning machine learning.
The student is reading a book.
The student is using Python.
The student is writing a program.
The teacher is teaching the student.
The teacher is explaining language models.
Python is a programming language.
Machine learning is an interesting subject.
Natural language processing is a useful field.
"""
# --------------------------------------------------
# Test Corpus
# --------------------------------------------------
test_corpus = [
    "The student is learning Python.",
    "The teacher is teaching the student.",
    "The cat is playing football.",
    "Natural language processing is useful."
]
# --------------------------------------------------
# Tokenization
# --------------------------------------------------
def tokenize(sentence):
    words = re.findall(r'\b[a-z]+\b', sentence.lower())
    return ["<s>"] + words + ["</s>"]
training_sentences = [
    tokenize(sentence)
    for sentence in re.split(r'[.!?]+', training_corpus)
    if sentence.strip()
]
# --------------------------------------------------
# Build Models
# --------------------------------------------------
unigrams = Counter()
bigrams = Counter()
trigrams = Counter()
for sentence in training_sentences:
    unigrams.update(sentence)
    for i in range(len(sentence) - 1):
        bigrams[(sentence[i], sentence[i + 1])] += 1
    for i in range(len(sentence) - 2):
        trigrams[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1
total = sum(unigrams.values())
# --------------------------------------------------
# Probability Functions
# --------------------------------------------------
def unigram_probability(word):
    return unigrams[word] / total
def bigram_probability(w1, w2):
    if unigrams[w1] == 0:
        return 0
    return bigrams[(w1, w2)] / unigrams[w1]
def trigram_probability(w1, w2, w3):
    if bigrams[(w1, w2)] == 0:
        return 0
    return trigrams[(w1, w2, w3)] / bigrams[(w1, w2)]
# --------------------------------------------------
# Add-One Smoothing
# --------------------------------------------------
vocabulary = set(unigrams.keys())
vocab_size = len(vocabulary)
def smoothed_bigram(w1, w2):
    return (
        bigrams[(w1, w2)] + 1
    ) / (
        unigrams[w1] + vocab_size
    )
# --------------------------------------------------
# Entropy Calculation
# --------------------------------------------------
def calculate_entropy(sentence, model):
    words = tokenize(sentence)
    log_probability = 0
    count = 0
    for i in range(1, len(words)):
        if model == "unigram":
            probability = unigram_probability(words[i])
        elif model == "bigram":
            probability = bigram_probability(
                words[i - 1],
                words[i]
            )
        elif model == "trigram":
            if i < 2:
                continue
            probability = trigram_probability(
                words[i - 2],
                words[i - 1],
                words[i]
            )
        if probability == 0:
            return float("inf")
        log_probability += math.log2(probability)
        count += 1
    return -log_probability / count
# --------------------------------------------------
# Test All Sentences
# --------------------------------------------------
print("=" * 80)
print("N-GRAM ENTROPY EVALUATION")
print("=" * 80)
for sentence in test_corpus:
    print("\nSentence:", sentence)
    for model in ["unigram", "bigram", "trigram"]:
        entropy = calculate_entropy(sentence, model)
        if entropy == float("inf"):
            print(model.capitalize(), "Entropy: Infinity")
        else:
            print(
                model.capitalize(),
                "Entropy:",
                round(entropy, 4)
            )
# --------------------------------------------------
# Smoothed Bigram Entropy
# --------------------------------------------------
def smoothed_entropy(sentence):
    words = tokenize(sentence)
    log_probability = 0
    count = 0
    for i in range(1, len(words)):
        probability = smoothed_bigram(
            words[i - 1],
            words[i]
        )
        log_probability += math.log2(probability)
        count += 1
    return -log_probability / count
print("\n" + "=" * 80)
print("SMOOTHED BIGRAM ENTROPY")
print("=" * 80)
for sentence in test_corpus:
    entropy = smoothed_entropy(sentence)
    print(
        f"{sentence:<55} "
        f"{entropy:.4f}"
    )
# --------------------------------------------------
# High and Low Entropy
# --------------------------------------------------
entropy_values = []
for sentence in test_corpus:
    entropy = smoothed_entropy(sentence)
    entropy_values.append(
        (sentence, entropy)
    )
highest = max(entropy_values, key=lambda x: x[1])
lowest = min(entropy_values, key=lambda x: x[1])
print("\n" + "=" * 80)
print("ENTROPY INTERPRETATION")
print("=" * 80)
print("Highest Entropy Sentence:")
print(highest[0])
print("Entropy:", round(highest[1], 4))
print("\nLowest Entropy Sentence:")
print(lowest[0])
print("Entropy:", round(lowest[1], 4))
# 4 - POS Tagging System
print("\nQuestion 4 Output: \n")
import re
from collections import Counter, defaultdict
# ============================================================
# TRAINING DATA
# ============================================================
training_sentences = [
    [
        ("the", "DT"),
        ("student", "NN"),
        ("is", "VBZ"),
        ("reading", "VBG"),
        ("a", "DT"),
        ("book", "NN")
    ],
    [
        ("the", "DT"),
        ("teacher", "NN"),
        ("is", "VBZ"),
        ("teaching", "VBG"),
        ("the", "DT"),
        ("student", "NN")
    ],
    [
        ("students", "NNS"),
        ("learn", "VB"),
        ("python", "NN")
    ],
    [
        ("the", "DT"),
        ("student", "NN"),
        ("writes", "VBZ"),
        ("code", "NN")
    ],
    [
        ("she", "PRP"),
        ("runs", "VBZ"),
        ("quickly", "RB")
    ],
    [
        ("he", "PRP"),
        ("plays", "VBZ"),
        ("football", "NN")
    ],
    [
        ("the", "DT"),
        ("machine", "NN"),
        ("is", "VBZ"),
        ("powerful", "JJ")
    ]
]
# ============================================================
# LEXICAL DICTIONARIES
# ============================================================
nouns = {
    "student", "teacher", "book", "python",
    "students", "code", "football", "machine"
}
verbs = {
    "read", "reading", "learn", "teaching",
    "write", "writes", "plays", "runs",
    "play", "is"
}
adjectives = {
    "good", "bad", "beautiful", "powerful",
    "interesting", "useful"
}
adverbs = {
    "quickly", "slowly", "carefully"
}
pronouns = {
    "i", "you", "he", "she", "we", "they"
}
determiners = {
    "a", "an", "the", "this", "that"
}
prepositions = {
    "in", "on", "at", "by", "with", "for", "from"
}
conjunctions = {
    "and", "but", "or"
}
auxiliaries = {
    "is", "am", "are", "was", "were",
    "be", "been", "being"
}
# ============================================================
# RULE-BASED POS TAGGER
# ============================================================
def rule_based_tag(word):
    w = word.lower()
    if w in pronouns:
        return "PRP"
    if w in determiners:
        return "DT"
    if w in conjunctions:
        return "CC"
    if w in prepositions:
        return "IN"
    if w in auxiliaries:
        return "VBZ"
    if w in adjectives:
        return "JJ"
    if w in adverbs:
        return "RB"
    if w in nouns:
        if w.endswith("s") and w != "is":
            return "NNS"
        return "NN"
    if w in verbs:
        if w.endswith("ing"):
            return "VBG"
        if w.endswith("s"):
            return "VBZ"
        return "VB"
    # Morphological rules
    if w.endswith("ing"):
        return "VBG"
    if w.endswith("ed"):
        return "VBD"
    if w.endswith("ly"):
        return "RB"
    if w.endswith("ous") or w.endswith("ful"):
        return "JJ"
    if w.endswith("s"):
        return "NNS"
    return "NN"
# ============================================================
# STOCHASTIC POS TAGGER
# ============================================================
# Word-tag counts
word_tag_counts = defaultdict(Counter)
# Tag transition counts
transition_counts = defaultdict(Counter)
# Count word/tag occurrences
for sentence in training_sentences:
    previous_tag = "<START>"
    for word, tag in sentence:
        word_tag_counts[word][tag] += 1
        transition_counts[previous_tag][tag] += 1
        previous_tag = tag
# Calculate emission probability
def emission_probability(word, tag):
    total = sum(word_tag_counts[word].values())
    if total == 0:
        return 0.01
    return word_tag_counts[word][tag] / total
# Calculate transition probability
def transition_probability(previous, current):
    total = sum(transition_counts[previous].values())
    if total == 0:
        return 0.01
    return transition_counts[previous][current] / total
# Obtain all tags
all_tags = set()
for sentence in training_sentences:
    for word, tag in sentence:
        all_tags.add(tag)
# Stochastic tagging
def stochastic_tag(sentence):
    words = sentence.lower().split()
    result = []
    previous_tag = "<START>"
    for word in words:
        scores = {}
        for tag in all_tags:
            emission = emission_probability(word, tag)
            transition = transition_probability(
                previous_tag,
                tag
            )
            scores[tag] = emission * transition
        best_tag = max(scores, key=scores.get)
        result.append((word, best_tag))
        previous_tag = best_tag
    return result
# ============================================================
# TRANSFORMATION-BASED TAGGING
# ============================================================
def transformation_based_tag(sentence):
    # Start with rule-based tags
    tagged = rule_based_tag_sentence(sentence)
    for i in range(len(tagged)):
        word, tag = tagged[i]
        previous_tag = None
        if i > 0:
            previous_tag = tagged[i - 1][1]
        # Rule 1:
        # Pronoun + word ending in common verb forms
        # Example: "They play"
        if previous_tag == "PRP":
            if word.endswith("ing"):
                tagged[i] = (word, "VBG")
            elif word.endswith("ed"):
                tagged[i] = (word, "VBD")
            elif word in verbs:
                tagged[i] = (word, "VB")
        # Rule 2:
        # Auxiliary + ing -> VBG
        if previous_tag == "VBZ" and word.endswith("ing"):
            tagged[i] = (word, "VBG")
        # Rule 3:
        # Determiner + noun
        if previous_tag == "DT" and tag == "NN":
            tagged[i] = (word, "NN")
    return tagged
def rule_based_tag_sentence(sentence):
    words = sentence.lower().split()
    return [
        (word, rule_based_tag(word))
        for word in words
    ]
# ============================================================
# DISPLAY
# ============================================================
def display(title, result):
    print("\n" + title)
    print("-" * 50)
    for word, tag in result:
        print(f"{word:<15} {tag}")
# ============================================================
# MAIN PROGRAM
# ============================================================
print("=" * 70)
print("PART-OF-SPEECH TAGGING SYSTEM")
print("=" * 70)
print("\nPenn Treebank-style POS tags are used.")
while True:
    sentence = input(
        "\nEnter an English sentence "
        "(or type 'exit'): "
    )
    if sentence.lower() == "exit":
        break
    # Rule-Based
    rule_result = rule_based_tag_sentence(sentence)
    # Stochastic
    stochastic_result = stochastic_tag(sentence)
    # Transformation-Based
    transformation_result = transformation_based_tag(sentence)
    display(
        "RULE-BASED TAGGER",
        rule_result
    )
    display(
        "STOCHASTIC TAGGER",
        stochastic_result
    )
    display(
        "TRANSFORMATION-BASED TAGGER",
        transformation_result
    )
