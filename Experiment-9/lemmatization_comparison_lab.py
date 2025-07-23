# -------------------------------------
# Lab 9: Implement Various Lemmatization Techniques and Compare Performance
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn  # ✅ Correct import
import spacy
import time
import matplotlib.pyplot as plt

# Step 1: Initialize lemmatizers
nltk_lemmatizer = WordNetLemmatizer()
spacy_model = spacy.load("en_core_web_sm")

# Step 2: Sample list of words for lemmatization
words = [
    "running", "flies", "jumping", "happily", "unhappiness",
    "easily", "quickly", "books", "cats", "children",
    "better", "best", "flying", "played", "walking",
    "processes", "processing", "processor", "processors"
]

# Step 3: Map POS tags to WordNet POS for better NLTK lemmatization
pos_map = {
    'J': wn.ADJ,   # ✅ These will now work
    'V': wn.VERB,
    'N': wn.NOUN,
    'R': wn.ADV
}

def nltk_pos(tag):
    return pos_map.get(tag[0], wn.NOUN)

# Step 4: Function to apply NLTK lemmatizer
def nltk_lemmatize(words_list):
    return [
        nltk_lemmatizer.lemmatize(word, nltk_pos(pos_tag([word])[0][1]))
        for word in words_list
    ]

# Step 5: Function to apply spaCy lemmatizer
def spacy_lemmatize(words_list):
    doc = spacy_model(" ".join(words_list))
    return [token.lemma_ for token in doc]

# Step 6: Measure performance
def measure_performance(func, words_list):
    start_time = time.time()
    result = func(words_list)
    end_time = time.time()
    return result, end_time - start_time

# Step 7: Apply both lemmatizers and record results
nltk_result, nltk_time = measure_performance(nltk_lemmatize, words)
spacy_result, spacy_time = measure_performance(spacy_lemmatize, words)

# Step 8: Display results
print("=== Lemmatization Results ===")
print(f"{'-'*40}")
print(f"{'Word':<15} | {'NLTK':<15} | {'spaCy':<15}")
print(f"{'-'*40}")
for word, nl, sp in zip(words, nltk_result, spacy_result):
    print(f"{word:<15} | {nl:<15} | {sp:<15}")

print(f"\nPerformance Time:")
print(f"NLTK Lemmatizer: {nltk_time:.6f} seconds")
print(f"spaCy Lemmatizer: {spacy_time:.6f} seconds")

# Step 9: Plot performance chart
labels = ['NLTK', 'spaCy']
times = [nltk_time, spacy_time]

plt.figure(figsize=(6, 4))
plt.bar(labels, times, color=['#4E79A7', '#F28E2B'])
plt.title("Lemmatization Performance Comparison")
plt.ylabel("Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()