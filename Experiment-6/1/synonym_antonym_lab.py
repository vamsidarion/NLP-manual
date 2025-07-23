# -------------------------------------
# Lab 6(i): Identify Synonyms and Antonyms of a Word
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag

# Step 1: Define function to get POS tag
def get_word_pos(word):
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {
        'J': wn.ADJ,
        'N': wn.NOUN,
        'V': wn.VERB,
        'R': wn.ADV
    }
    return tag_dict.get(tag, wn.NOUN)  # Default to noun

# Step 2: Get word input from user
word = input("Enter a word to find synonyms and antonyms: ").strip().lower()

# Step 3: Get POS tag for better results
pos = get_word_pos(word)

# Step 4: Get synonyms from WordNet
synonyms = set()
for syn in wn.synsets(word, pos=pos):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

# Step 5: Get antonyms from WordNet
antonyms = set()
for syn in wn.synsets(word, pos=pos):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

# Step 6: Print results
print("\n=== Synonyms of '{}' ===".format(word))
if synonyms:
    print(", ".join(synonyms))
else:
    print("No synonyms found.")

print("\n=== Antonyms of '{}' ===".format(word))
if antonyms:
    print(", ".join(antonyms))
else:
    print("No antonyms found.")