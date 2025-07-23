# -------------------------------------
# Lab 6(ii): Find Hyponymy, Homonymy, and Polysemy
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import wordnet as wn

# Step 1: Get word input from user
word = input("Enter a word to explore its lexical relations: ").strip().lower()

# Step 2: Get all synsets for the word (to find homonyms and polysemy)
synsets = wn.synsets(word)

# Step 3: Display synsets and their definitions (shows polysemy)
print("\n=== Polysemy: Different Meanings of '{}' ===".format(word))
if synsets:
    for i, syn in enumerate(synsets):
        print(f"{i+1}. {syn.name()} - {syn.definition()}")
else:
    print("No meanings found for this word.")

# Step 4: Find homonyms (same word, different meanings)
# Homonyms are already captured in different synsets of the same word
print("\n=== Homonymy: '{}' has {} distinct meanings ===".format(word, len(synsets)))
if synsets:
    print("Each meaning is shown above.")

# Step 5: Find hyponyms (specific instances of the word)
print("\n=== Hyponymy: Specific Instances of '{}' ===".format(word))
hyponyms_found = False
for i, syn in enumerate(synsets):
    hyponyms = syn.hyponyms()
    if hyponyms:
        print(f"\nMeaning {i+1}: {syn.name()}")
        for h in hyponyms[:5]:  # Show up to 5 hyponyms
            print(" -", h.name().replace('_', ' '))
        hyponyms_found = True

if not hyponyms_found:
    print("No hyponyms found for this word.")