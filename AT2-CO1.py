import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# Sample words
words = ["playing", "walked", "teachers", "unhappiness", "running", "studies"]
print("Morphological Analysis\n")
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"Original Word : {word}")
    print(f"Stem          : {stem}")
    print(f"Lemma         : {lemma}")
    print("-" * 30)