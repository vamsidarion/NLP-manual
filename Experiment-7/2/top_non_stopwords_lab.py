# -------------------------------------
# Lab 7(ii): Top 50 Frequent Non-Stop Words
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Step 1: Sample input text (or load from a corpus)
text = """Natural Language Processing is one of the most important fields of artificial intelligence.
It helps computers understand, interpret, and respond to human language in a valuable way.
Natural language is processed using various algorithms and models in machine learning."""

# Step 2: Tokenize the text into lowercase words
words = word_tokenize(text.lower())

# Step 3: Get English stop words list
stop_words = set(stopwords.words('english'))

# Step 4: Remove stop words and punctuation
filtered_words = [
    word for word in words
    if word.isalpha() and word not in stop_words
]

# Step 5: Count frequencies of remaining words
word_freq = Counter(filtered_words)

# Step 6: Get top 50 most frequent words
top_words = word_freq.most_common(50)

# Step 7: Print results
print("=== Top 50 Most Frequent Non-Stop Words ===")
for word, freq in top_words:
    print(f"{word}: {freq}")