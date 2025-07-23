# -------------------------------------
# Lab 11(iv): Identify Tags That Commonly Precede Nouns
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import brown
from collections import Counter

# Step 1: Load tagged words from the Brown Corpus
tagged_words = brown.tagged_words()

# Step 2: Find word-tag pairs that are followed by a noun
noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']  # Singular/plural and proper nouns

# Step 3: Create a list of (previous_tag, noun_tag) pairs
prev_tags_before_noun = []

for i in range(1, len(tagged_words) - 1):
    prev_word, prev_tag = tagged_words[i - 1]
    curr_word, curr_tag = tagged_words[i]

    if curr_tag in noun_tags:
        prev_tags_before_noun.append((prev_tag, curr_tag))

# Step 4: Count frequency of each preceding tag
prev_tag_counts = Counter(tag for tag, noun_tag in prev_tags_before_noun)

# Step 5: Show top 20 most frequent preceding tags
top_n = 20
top_tags = prev_tag_counts.most_common(top_n)

print("=== Tags That Commonly Precede Nouns ===")
print(f"{'Tag':<6} | {'Count':<7} | {'Meaning'}")
print("-" * 50)

# Step 6: Manually define meanings of common Brown POS tags
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
    'WRB': 'Wh-adverb'
}

# Step 7: Print top tags with meanings
for tag, count in top_tags:
    meaning = brown_tag_meanings.get(tag, "Unknown or rare tag")
    print(f"{tag:<6} | {count:<7} | {meaning}")