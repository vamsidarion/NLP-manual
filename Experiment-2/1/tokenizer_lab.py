# -------------------------------------
# Lab 2(i): Word, Sentence, and Paragraph Tokenizer
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Step 1: Sample text input
text = """Natural Language Processing (NLP) is fascinating.
It allows computers to understand human language!
We can do many things like sentiment analysis, question answering, and more."""

# Step 2: Word Tokenization
words = word_tokenize(text)
print("=== Word Tokens ===")
for i, word in enumerate(words):
    print(f"{i+1}. {word}")

# Step 3: Sentence Tokenization
sentences = sent_tokenize(text)
print("\n=== Sentence Tokens ===")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. {sentence}")

# Step 4: Paragraph Tokenization (Manual)
paragraphs = text.strip().split('\n\n')  # Split by double newlines
print("\n=== Paragraph Tokens ===")
for i, paragraph in enumerate(paragraphs):
    print(f"{i+1}.\n{paragraph}\n")