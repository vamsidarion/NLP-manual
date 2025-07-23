# -------------------------------------
# Lab 7(i): Find All Stop Words in a Given Text
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Step 1: Sample input text
text = """Natural Language Processing is one of the most important fields of artificial intelligence.
It helps computers understand, interpret, and respond to human language in a valuable way."""

# Step 2: Tokenize the text into words (convert to lowercase for matching)
words = word_tokenize(text.lower())

# Step 3: Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Step 4: Find which words in the text are stop words
stop_words_in_text = [word for word in words if word in stop_words]

# Step 5: Print results
print("=== Stop Words Found in the Text ===")
if stop_words_in_text:
    for word in stop_words_in_text:
        print("-", word)
else:
    print("No stop words found in the text.")