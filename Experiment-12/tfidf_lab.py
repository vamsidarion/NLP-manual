# -------------------------------------
# Lab 12: Implement TF-IDF for a Corpus with Visualization
# Run this in VS Code
# -------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Define a sample corpus
corpus = [
    'Natural language processing helps computers understand human language',
    'Language models help predict what comes next in language',
    'Machine learning is a part of artificial intelligence',
    'Deep learning is a subset of machine learning',
    'Artificial intelligence helps in natural language processing'
]

# Step 2: Create TF-IDF Vectorizer object
vectorizer = TfidfVectorizer()

# Step 3: Fit and transform the corpus
tfidf_matrix = vectorizer.fit_transform(corpus)

# Step 4: Get feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Step 5: Create a DataFrame for visualization
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Step 6: Display the TF-IDF matrix
print("=== TF-IDF Matrix ===")
print(df.round(3))

# Step 7: Plot the TF-IDF matrix as a heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df, annot=True, cmap='YlGnBu', xticklabels=feature_names, yticklabels=[f"Doc {i+1}" for i in range(len(corpus))])
plt.title("TF-IDF Matrix Heatmap")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Step 8: Plot top words in the first document
doc_index = 0
top_words = df.iloc[doc_index].sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_words.plot(kind='barh', color='teal')
plt.title(f"Top Words in Document {doc_index + 1} (TF-IDF Scores)")
plt.xlabel("TF-IDF Score")
plt.ylabel("Word")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()