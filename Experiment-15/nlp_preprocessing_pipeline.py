# -------------------------------------
# Lab 15: NLP Preprocessing Pipeline
# Run this in VS Code
# -------------------------------------

import nltk
import spacy
import string
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import word_tokenize, sent_tokenize

# Load English model for spaCy
nlp = spacy.load("en_core_web_sm")

# Step 1: Sample input text
text = """Natural Language Processing helps computers understand human language.
It is a field of artificial intelligence that is growing rapidly.
With NLP, we can build chatbots, translation tools, and more!
Natural language is very important for machine understanding."""

# Step 2: Basic Text Cleaning
def clean_text(text):
    # Remove newline characters
    text = text.replace('\n', ' ')
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Step 3: Tokenization
def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    return sentences, words

# Step 4: Lowercasing
def lowercase_words(words):
    return [word.lower() for word in words]

# Step 5: Remove stopwords
def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

# Step 6: Remove punctuation
def remove_punctuation(words):
    return [word for word in words if word not in string.punctuation]

# Step 7: Stemming
def apply_stemming(words):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in words]

# Step 8: Lemmatization
def apply_lemmatization(words):
    lemmatizer = WordNetLemmatizer()
    # Map POS tags to WordNet POS for better lemmatization
    def get_wordnet_pos(tag):
        if tag.startswith('J'):
            return nltk.corpus.wordnet.ADJ
        elif tag.startswith('V'):
            return nltk.corpus.wordnet.VERB
        elif tag.startswith('N'):
            return nltk.corpus.wordnet.NOUN
        elif tag.startswith('R'):
            return nltk.corpus.wordnet.ADV
        else:
            return nltk.corpus.wordnet.NOUN

    pos_tags = nltk.pos_tag(words)
    return [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]

# Step 9: Final Preprocessing Pipeline
def preprocess_text(text):
    print("Original Text:\n", text)
    
    print("\n1. Cleaning Text...")
    cleaned_text = clean_text(text)
    print(cleaned_text)

    print("\n2. Tokenizing...")
    sentences, words = tokenize_text(cleaned_text)
    print("Sentences:", sentences)
    print("Words:", words)

    print("\n3. Lowercasing...")
    words_lower = lowercase_words(words)
    print("Lowercased Words:", words_lower)

    print("\n4. Removing Stopwords...")
    words_no_stopwords = remove_stopwords(words_lower)
    print("Words without Stopwords:", words_no_stopwords)

    print("\n5. Removing Punctuation...")
    words_clean = remove_punctuation(words_no_stopwords)
    print("Words after Removing Punctuation:", words_clean)

    print("\n6. Stemming...")
    words_stemmed = apply_stemming(words_clean)
    print("Stemmed Words:", words_stemmed)

    print("\n7. Lemmatization...")
    words_lemmatized = apply_lemmatization(words_clean)
    print("Lemmatized Words:", words_lemmatized)

    return {
        "cleaned_text": cleaned_text,
        "tokenized_words": words_clean,
        "stemmed_words": words_stemmed,
        "lemmatized_words": words_lemmatized
    }

# Step 10: Run the pipeline
processed = preprocess_text(text)

# Optional: Output final result
print("\n Final Preprocessed Words (Lemmatized):")
print(processed['lemmatized_words'])