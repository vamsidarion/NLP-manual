# -------------------------------------
# Lab 11(iii): List POS Tags in Order of Frequency + Explain Top 20
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import brown
from collections import Counter

# Step 1: Load tagged words from the Brown Corpus
tagged_words = brown.tagged_words()

# Step 2: Count the frequency of each POS tag
tag_counts = Counter(tag for word, tag in tagged_words)

# Step 3: Sort tags by frequency (descending)
sorted_tags = tag_counts.most_common()

# Step 4: Display all tags in decreasing order of frequency
print("=== POS Tags in Decreasing Order of Frequency ===")
for tag, count in sorted_tags:
    print(f"{tag}: {count}")

# Step 5: Display the top 20 most frequent tags
top_n = 20
top_tags = sorted_tags[:top_n]

print(f"\n=== Top {top_n} Most Frequent Tags ===")
print(f"{'Tag':<6} | {'Count':<7} | {'Meaning'}")
print("-" * 50)

# Step 6: Manually define meanings of common Brown POS tags
brown_tag_meanings = {
    'NN': 'Noun, singular',
    'NN-TL': 'Noun, singular, title case',
    'NN-NC': 'Noun, singular, non-capitalized',
    'NNP': 'Proper noun, singular',
    'NNP-NC': 'Proper noun, singular, non-capitalized',
    'NNS': 'Noun, plural',
    'NNS-TL': 'Noun, plural, title case',
    'JJ': 'Adjective',
    'JJR': 'Adjective, comparative',
    'JJS': 'Adjective, superlative',
    'RB': 'Adverb',
    'RBR': 'Adverb, comparative',
    'RBS': 'Adverb, superlative',
    'IN': 'Preposition or subordinating conjunction',
    'DT': 'Determiner',
    'TO': '"to" as preposition or infinitival',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non-3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'MD': 'Modal',
    'CC': 'Coordinating conjunction',
    'CD': 'Cardinal number',
    'EX': 'Existential there',
    'FW': 'Foreign word',
    'LS': 'List item marker',
    'PDT': 'Predeterminer',
    'POS': 'Possessive ending',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'UH': 'Interjection',
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

# Step 7: Print top 20 tags with meanings
for tag, count in top_tags:
    meaning = brown_tag_meanings.get(tag, "Unknown or rare tag")
    print(f"{tag:<6} | {count:<7} | {meaning}")