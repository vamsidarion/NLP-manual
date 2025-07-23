# -------------------------------------
# Lab 14(ii): Frequency Table of Misspelled Words
# Run this in VS Code
# -------------------------------------

from textblob import TextBlob
from collections import Counter
import pandas as pd

# Step 1: Sample text with possible misspellings
text = """
Natural langauge processing is a subfeild of artifical intellegence.
It helps machines to understand, interpret, and generate human language.
With NLP, we can build chatbots, translation tools, and muche.
Langauge is very important for NLP. Subfeild is not spelled correctly.
"""

# Step 2: Create a TextBlob object
blob = TextBlob(text)

# Step 3: Tokenize and detect misspelled words
words = blob.words
misspelled_words = []

for word in words:
    if word.correct() != word:
        misspelled_words.append(word)

# Step 4: Count frequency of each misspelled word
misspelled_counter = Counter(misspelled_words)

# Step 5: Create a DataFrame for tabular output
df = pd.DataFrame(misspelled_counter.items(), columns=['Misspelled Word', 'Frequency'])

# Step 6: Add a column for suggested correction
df['Suggested Correction'] = df['Misspelled Word'].apply(lambda word: word.correct())

# Step 7: Sort by frequency (descending)
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Step 8: Display the table
print("=== Frequency Table of Misspelled Words ===")
print(df.to_string(index=False))