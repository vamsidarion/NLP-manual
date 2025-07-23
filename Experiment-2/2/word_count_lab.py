# -------------------------------------
# Lab 2(ii): Count Total and Unique Words in a Corpus
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize

# Step 1: Use sample text or load from a corpus
# For example, use a built-in sample text
text = """Natural Language Processing is fascinating. It allows computers to understand human language!
We can do many things like sentiment analysis, question answering, and more."""

# Step 2: Word Tokenization
words = word_tokenize(text)

# Step 3: Count total number of words
total_words = len(words)

# Step 4: Count distinct (unique) words using set()
distinct_words = set(words)
num_distinct_words = len(distinct_words)

# Step 5: Print results
print("=== Word Count ===")
print("Total Words:", total_words)
print("Distinct Words:", num_distinct_words)
print("\nList of Distinct Words:")
print(sorted(distinct_words))