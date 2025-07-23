# -------------------------------------
# Lab 5(i): Identify Mathematical Expressions in a Sentence
# Run this in VS Code
# -------------------------------------

import re

# Step 1: Sample input sentence
sentence = "The sum of 2 + 3 is 5, and 10 ÷ 2 equals 5. Also, 4*2=8 and 100 - 50 = 50."

# Optional: Take input from user
# sentence = input("Enter a sentence: ")

# Step 2: Define regex pattern for matching mathematical expressions
# Supports: numbers, +, -, *, /, =, ÷, ×
pattern = r'(\d+\s*[+−−÷×*]\s*\d+\s*[=]?\s*\d*)+'

# Step 3: Find all matches in the sentence
expressions = re.findall(pattern, sentence)

# Step 4: Print results
print("=== Mathematical Expressions Found ===")
if expressions:
    for expr in expressions:
        print("-", expr)
else:
    print("No mathematical expressions found.")