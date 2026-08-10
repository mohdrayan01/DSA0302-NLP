# 17.Write program demonstrates how to access WordNet, a lexical database, to retrieve synsets and explore word meanings in python.

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
word = "bank"
synsets = wordnet.synsets(word)
for syn in synsets:
    print("Synset :", syn.name())
    print("Meaning:", syn.definition())
    print()