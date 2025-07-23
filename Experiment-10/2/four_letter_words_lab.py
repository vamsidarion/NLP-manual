# -------------------------------------
# Lab 10(ii): Find Four-letter Words and Show Frequency Distribution
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import gutenberg
from nltk import FreqDist

# Step 1: Load text from a corpus (e.g., 'austen-emma.txt')
file_id = 'austen-emma.txt'
raw_text = gutenberg.raw(file_id)

# Step 2: Tokenize the text into lowercase words
words = [word.lower() for word in gutenberg.words(file_id) if word.isalpha()]

# Step 3: Filter only four-letter words
four_letter_words = [word for word in words if len(word) == 4]

# Step 4: Build frequency distribution
freq_dist = FreqDist(four_letter_words)

# Step 5: Display the 30 most common four-letter words
print("=== Top 30 Four-letter Words (Descending Order of Frequency) ===")
for word, freq in freq_dist.most_common(30):
    print(f"{word}: {freq}")