# -------------------------------------
# Lab 10(i): Implement Conditional Frequency Distribution (CFD)
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import gutenberg
from nltk import ConditionalFreqDist, FreqDist

# Step 1: Define the list of texts and authors
# Format: 'author-text_name'
text_names = [
    'austen-emma.txt',
    'austen-sense.txt',
    'melville-moby_dick.txt',
    'shakespeare-hamlet.txt'
]

# Step 2: Create a Conditional Frequency Distribution
cfd = ConditionalFreqDist()

for file_id in text_names:
    # Get author name from file_id
    author = file_id.split('-')[0].title()

    # Load and tokenize words
    words = gutenberg.words(file_id)
    
    # Filter alphabetic and lowercase
    words = [word.lower() for word in words if word.isalpha()]

    # Add top 100 words to CFD
    for word in words[:5000]:  # Limiting to 5000 words for faster processing
        cfd[author][word] += 1

# Step 3: Display top N words for each author
top_n = 10
print(f"=== Top {top_n} Words by Author ===")

for author in cfd.conditions():
    print(f"\n{author}:")
    most_common = cfd[author].most_common(top_n)
    for word, count in most_common:
        print(f" - {word}: {count}")