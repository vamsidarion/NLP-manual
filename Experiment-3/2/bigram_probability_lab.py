# -------------------------------------
# Lab 3(ii): Calculate Probability of Word w2 after w1
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import defaultdict, Counter

# Step 1: Sample input text
text = """Natural language processing helps computers understand human language.
Language models help predict what comes next in language."""

# Step 2: Tokenize the text into words
tokens = word_tokenize(text.lower())  # Use lowercase for consistency

# Step 3: Generate bi-grams
bigrams = list(ngrams(tokens, 2))

# Step 4: Count frequency of each word and each bi-gram
word_counts = Counter()
bigram_counts = Counter()

for w1, w2 in bigrams:
    word_counts[w1] += 1
    bigram_counts[(w1, w2)] += 1

# Step 5: Function to calculate P(w2 | w1)
def get_probability(w1, w2):
    if word_counts[w1] == 0:
        return 0.0
    return bigram_counts.get((w1, w2), 0) / word_counts[w1]

# Step 6: Get user input or test with sample words
test_pairs = [("language", "processing"), ("help", "computers"), ("language", "models")]

print("=== Bi-gram Probabilities ===")
for w1, w2 in test_pairs:
    prob = get_probability(w1, w2)
    print(f"P({w2} | {w1}) = {prob:.2f}")