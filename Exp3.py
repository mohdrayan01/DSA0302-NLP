# 3.Write program demonstrates how to perform morphological analysis using the NLTK library in Python.
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words = ["running", "played", "studies", "better", "cars"]
print("Word\t\tStem\t\tLemma")
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word}\t\t{stem}\t\t{lemma}")
print("\n")