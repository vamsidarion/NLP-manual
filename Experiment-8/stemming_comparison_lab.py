# -------------------------------------
# Lab 8: Implement Various Stemming Techniques and Compare Performance
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer
import time
import matplotlib.pyplot as plt

# Step 1: Initialize stemmers
porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
regexp = RegexpStemmer('ing$|s$|ed$', min=4)

# Step 2: Sample list of words for stemming
words = [
    "running", "flies", "jumping", "happily", "unhappiness",
    "easily", "quickly", "books", "cats", "children",
    "better", "best", "flying", "played", "walking",
    "processes", "processing", "processor", "processors"
]

# Step 3: Function to measure time and apply stemmer
def stem_words(stemmer, words):
    start_time = time.time()
    stemmed = [stemmer.stem(word) for word in words]
    end_time = time.time()
    return stemmed, end_time - start_time

# Step 4: Apply all stemmers and record performance
results = {}

results["Porter"] = stem_words(porter, words)
results["Snowball"] = stem_words(snowball, words)
results["Lancaster"] = stem_words(lancaster, words)
results["Regexp"] = stem_words(regexp, words)

# Step 5: Display results
print("=== Stemming Results ===")
for stemmer_name, (stemmed_words, duration) in results.items():
    print(f"\n{stemmer_name} Stemmer:")
    print("-" * 30)
    for word, stem in zip(words, stemmed_words):
        print(f"{word} → {stemmed_words[words.index(word)]}")
    print(f"Time taken: {duration:.6f} seconds")

# Step 6: Plot performance chart
stemmers = list(results.keys())
times = [results[name][1] for name in stemmers]

plt.figure(figsize=(8, 5))
plt.bar(stemmers, times, color='skyblue')
plt.title("Performance Comparison of Stemming Techniques")
plt.ylabel("Time (seconds)")
plt.xlabel("Stemmer")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()