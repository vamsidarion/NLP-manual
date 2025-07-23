# -------------------------------------
# Lab 4(ii): Print Words Starting With a Given Prefix
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize

# Step 1: Sample input text
text = """Natural language processing helps computers understand human language.
Language models help predict what comes next in language."""

# Step 2: Tokenize the text into lowercase words
tokens = word_tokenize(text.lower())  # Convert to lowercase for case-insensitive match

# Step 3: Remove punctuation (optional)
words = [word for word in tokens if word.isalpha()]

# Step 4: Get prefix input from user or define it
prefix = input("Enter prefix to search for words: ").lower()

# Step 5: Find words that start with the given prefix
matching_words = [word for word in words if word.startswith(prefix)]

# Step 6: Print results
if matching_words:
    print(f"\nWords starting with '{prefix}':")
    for word in matching_words:
        print("-", word)
else:
    print(f"\nNo words found starting with '{prefix}'.")