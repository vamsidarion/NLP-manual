# -------------------------------------
# Lab 14(i): Find Misspelled Words in a Paragraph
# Run this in VS Code
# -------------------------------------

from textblob import TextBlob

# Step 1: Sample paragraph with possible misspellings
paragraph = """
Natural langauge processing is a subfeild of artifical intellegence.
It helps machines to understand, interpret, and generate human language.
With NLP, we can build chatbots, translation tools, and much moree.
"""

# Step 2: Create a TextBlob object
blob = TextBlob(paragraph)

# Step 3: Extract words and check for spelling
words = blob.words
misspelled = []

for word in words:
    if word.correct() != word:
        misspelled.append(word)

# Step 4: Display results
print("=== Misspelled Words ===")
if misspelled:
    for word in misspelled:
        print(f"- '{word}' → Did you mean '{word.correct()}'?")
else:
    print("No misspelled words found.")