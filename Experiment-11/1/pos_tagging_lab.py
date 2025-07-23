# -------------------------------------
# Lab 11(i): Part-of-Speech (POS) Tagging using NLTK and spaCy
# Run this in VS Code
# -------------------------------------

import nltk
from nltk import pos_tag, word_tokenize
import spacy

# Step 1: Sample input text
text = """Natural Language Processing helps computers understand human language.
Language models help predict what comes next in language."""

# Step 2: NLTK POS Tagging
print("=== POS Tagging using NLTK ===")
tokens = word_tokenize(text.lower())
nltk_tags = pos_tag(tokens)

print("{:<15} {:<15}".format("Word", "POS Tag"))
print("-" * 30)
for word, tag in nltk_tags:
    print("{:<15} {:<15}".format(word, tag))

# Step 3: spaCy POS Tagging
print("\n=== POS Tagging using spaCy ===")

# Load English model
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("{:<15} {:<15} {:<15}".format("Word", "POS Tag", "Tag Explanation"))
print("-" * 50)
for token in doc:
    print("{:<15} {:<15} {:<15}".format(token.text, token.pos_, token.tag_))

# Optional: POS explanation
print("\n📌 Explanation:")
print("- POS Tag: Simplified part-of-speech (e.g., NOUN, VERB)")
print("- Tag: Detailed tag with context (e.g., VBD = Verb, past tense)")