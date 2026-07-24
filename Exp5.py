# 5.Use the Porter Stemmer algorithm to perform word stemming on a list of words using python libraries.

import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["playing", "running", "studies", "happiness", "easily"]
for word in words:
    print(word, "->", stemmer.stem(word))