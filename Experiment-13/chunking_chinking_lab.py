# -------------------------------------
# Lab 13: Chunking and Chinking using NLTK
# Run this in VS Code
# -------------------------------------

import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import ne_chunk

# Step 1: Sample text input
text = """Natural language processing helps computers understand human language.
It is a field of artificial intelligence that is growing rapidly."""

# Step 2: Tokenize and POS tag the text
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

# Step 3: Define grammar for Chunking (Noun Phrases)
chunk_grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>}  
    """  # Optional: Add more rules for VP, PP, etc.

# Step 4: Create parser with chunk grammar
chunk_parser = RegexpParser(chunk_grammar)

# Step 5: Apply chunking
chunked = chunk_parser.parse(pos_tags)

# Step 6: Display chunked tree
print("=== Chunked Tree ===")
print(chunked)

# Step 7: Draw chunked tree
print("\n[INFO] Drawing chunked parse tree...")
chunked.pretty_print()
# You can also visualize with NLTK's draw() method
# from nltk.tree import Tree
# chunked.pretty_print()

# Step 8: Chinking - Remove prepositions and determiners from chunks
chink_grammar = r"""
    NP:
        {<.*>+}          # Chunk everything
        }<IN|DT|CC|TO>{  # Chink (remove) prepositions, determiners, etc.
    """
chink_parser = RegexpParser(chink_grammar)

# Step 9: Apply chinking
chinked = chink_parser.parse(pos_tags)

# Step 10: Display chinked tree
print("\n=== Chinked Tree ===")
print(chinked)

# Optional: Draw chinked tree
print("\n[INFO] Drawing chinked parse tree...")
chinked.pretty_print()

# Step 11: Extract noun phrases from chunked tree
def extract_noun_phrases(tree):
    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            words = [word for word, tag in subtree.leaves()]
            noun_phrases.append(' '.join(words))
    return noun_phrases

print("\n=== Extracted Noun Phrases ===")
noun_phrases = extract_noun_phrases(chunked)
for phrase in noun_phrases:
    print("-", phrase)