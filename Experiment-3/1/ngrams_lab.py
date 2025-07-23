# -------------------------------------
# Lab 3(i): Generate Uni-grams, Bi-grams, Tri-grams, N-grams
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Sample text input
text = """Natural Language Processing allows computers to understand human language.
It makes machines talk like humans do."""

# Tokenize the text into words
tokens = word_tokenize(text)

# -------------------------------
# (a) User-defined Functions
# -------------------------------

def generate_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

print("=== Using User-defined Functions ===")

uni_grams = generate_ngrams(tokens, 1)
bi_grams = generate_ngrams(tokens, 2)
tri_grams = generate_ngrams(tokens, 3)
n_grams = generate_ngrams(tokens, 4)

print("\n(a) Uni-grams:")
print(uni_grams)

print("\n(b) Bi-grams:")
print(bi_grams)

print("\n(c) Tri-grams:")
print(tri_grams)

print("\n(d) N-grams (e.g., 4-grams):")
print(n_grams)

# -------------------------------
# (b) Pre-defined Functions (using NLTK)
# -------------------------------

print("\n=== Using NLTK Built-in Functions ===")

def nltk_ngrams(tokens, n):
    return list(ngrams(tokens, n))

print("\n(a) Uni-grams (NLTK):")
print(nltk_ngrams(tokens, 1))

print("\n(b) Bi-grams (NLTK):")
print(nltk_ngrams(tokens, 2))

print("\n(c) Tri-grams (NLTK):")
print(nltk_ngrams(tokens, 3))

print("\n(d) N-grams (NLTK):")
print(nltk_ngrams(tokens, 4))