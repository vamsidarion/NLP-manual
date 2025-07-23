# -------------------------------------
# Lab 4(iii): Print Words Longer Than 4 Characters
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.tokenize import word_tokenize

# Step 1: Sample input text
text = """Natural language processing helps computers understand human language.
Language models help predict what comes next in language."""

# Step 2: Tokenize the text into lowercase words
tokens = word_tokenize(text.lower())

# Step 3: Remove punctuation and keep only alphabetic words
words = [word for word in tokens if word.isalpha()]

# Step 4: Filter words longer than 4 characters
long_words = [word for word in words if len(word) > 4]

# Step 5: Print results
print("=== Words Longer Than 4 Characters ===")
for word in long_words:
    print("-", word)