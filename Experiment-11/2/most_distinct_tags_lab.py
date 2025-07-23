# -------------------------------------
# Lab 11(ii): Find the Word with the Most Distinct POS Tags
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import brown
from collections import defaultdict

# Step 1: Load tagged words from the Brown Corpus
tagged_words = brown.tagged_words()

# Step 2: Create a dictionary to map each word to its set of POS tags
word_to_tags = defaultdict(set)

for word, tag in tagged_words:
    word_to_tags[word.lower()].add(tag)  # Convert to lowercase

# Step 3: Find the word with the most distinct POS tags
max_tags = 0
word_with_max_tags = ""
all_tags_for_word = set()

for word, tags in word_to_tags.items():
    if len(tags) > max_tags:
        max_tags = len(tags)
        word_with_max_tags = word
        all_tags_for_word = tags

# Step 4: Display results
print("=== Word with the Greatest Number of Distinct POS Tags ===")
print(f"Word: '{word_with_max_tags}'")
print(f"Number of distinct tags: {max_tags}")
print("\nDistinct POS Tags:")
for tag in sorted(all_tags_for_word):
    print(f" - {tag}")

# Step 5: Manually define common Brown Corpus POS tag meanings
brown_tag_meanings = {
    'CC': 'Coordinating conjunction',
    'CD': 'Cardinal number',
    'DT': 'Determiner',
    'EX': 'Existential there',
    'FW': 'Foreign word',
    'IN': 'Preposition or subordinating conjunction',
    'JJ': 'Adjective',
    'JJR': 'Adjective, comparative',
    'JJS': 'Adjective, superlative',
    'LS': 'List item marker',
    'MD': 'Modal',
    'NN': 'Noun, singular or mass',
    'NNS': 'Noun, plural',
    'NNP': 'Proper noun, singular',
    'NNPS': 'Proper noun, plural',
    'PDT': 'Predeterminer',
    'POS': 'Possessive ending',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun',
    'RB': 'Adverb',
    'RBR': 'Adverb, comparative',
    'RBS': 'Adverb, superlative',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': '"to" as preposition or infinitival',
    'UH': 'Interjection',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non-3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun',
    'WP$': 'Possessive wh-pronoun',
    'WRB': 'Wh-adverb',
    'PUNC': 'Punctuation',
    'CS': 'Conjunction, subordinating',
    'CS*': 'Conjunction, subordinating (wh-)',
    'DTQ': 'Determiner + wh-element',
    'HVD': 'Form of "have" (past tense)',
    'HV': 'Form of "have"',
    'TO': 'Infinitival "to"'
}

# Step 6: Print meanings of the found tags
print("\n Tag Meanings (Simplified):")
for tag in sorted(all_tags_for_word):
    meaning = brown_tag_meanings.get(tag, "Unknown or rare tag")
    print(f"{tag}: {meaning}")