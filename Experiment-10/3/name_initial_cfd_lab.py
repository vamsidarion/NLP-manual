# -------------------------------------
# Lab 10(iii): CFD of Initial Letters in Names (Male vs. Female)
# With Visualization
# Run this in VS Code
# -------------------------------------

import nltk
from nltk.corpus import names
from nltk import ConditionalFreqDist
import matplotlib.pyplot as plt

# Step 1: Load male and female names
male_names = [(name, 'Male') for name in names.words('male.txt')]
female_names = [(name, 'Female') for name in names.words('female.txt')]

# Step 2: Function to extract the first letter of a name
def get_initial(name):
    return name[0].upper()  # Return first letter (uppercase)

# Step 3: Build Conditional Frequency Distribution
cfd = ConditionalFreqDist()

for name, gender in male_names + female_names:
    initial = get_initial(name)
    cfd[gender][initial] += 1

# Step 4: Display frequency of initial letters for both genders
print("=== Initial Letter Frequencies: Male vs. Female ===")
print(f"{'Letter':<7} | {'Male':<7} | {'Female':<7}")
print("-" * 25)

# Get all letters that appear in either gender
all_letters = sorted(set(cfd['Male'].keys()) | set(cfd['Female'].keys()))

for letter in all_letters:
    male_count = cfd['Male'].get(letter, 0)
    female_count = cfd['Female'].get(letter, 0)
    print(f"{letter:<7} | {male_count:<7} | {female_count:<7}")

# Step 5: Visualize top N initial letters
top_n = 10

male_top = cfd['Male'].most_common(top_n)
female_top = cfd['Female'].most_common(top_n)

male_letters, male_counts = zip(*male_top)
female_letters, female_counts = zip(*female_top)

x_indexes = range(len(male_letters))

plt.figure(figsize=(12, 6))
bar_width = 0.4

# Plot bars
plt.bar(x_indexes, male_counts, width=bar_width, label='Male', color='#4E79A7')
plt.bar([i + bar_width for i in x_indexes], female_counts, width=bar_width, label='Female', color='#F28E2B')

# Customize plot
plt.title("Top {} Initial Letters in Male vs. Female Names".format(top_n))
plt.xlabel("Initial Letter")
plt.ylabel("Frequency")
plt.xticks([i + bar_width / 2 for i in x_indexes], male_letters)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()