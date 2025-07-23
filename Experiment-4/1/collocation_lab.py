# -------------------------------------
# Lab 4(i): Identify Word Collocations
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import word_tokenize

# Step 1: Sample input text
text = """Natural language processing helps computers understand human language.
Language models help predict what comes next in language. 
Processing large amounts of data is essential for learning patterns in language."""

# Step 2: Tokenize the text into lowercase words
tokens = word_tokenize(text.lower())

# Step 3: Create a BigramCollocationFinder object
bigram_finder = BigramCollocationFinder.from_words(tokens)

# Step 4: Apply frequency filter (optional)
# Only consider bigrams that appear at least N times
bigram_finder.apply_freq_filter(2)  # Keep only bigrams that occur at least 2 times

# Step 5: Get top N collocations using PMI (Pointwise Mutual Information)
top_collocations = bigram_finder.nbest(BigramAssocMeasures().pmi, 10)

# Step 6: Print results
print("=== Top Collocations ===")
for collocation in top_collocations:
    print(collocation)