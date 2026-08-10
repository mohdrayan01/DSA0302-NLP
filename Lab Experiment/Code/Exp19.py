# 19.Create a program for word sense disambiguation using the Lesk algorithm using python.

import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
sentence = "I went to the bank to deposit money."
tokens = word_tokenize(sentence)
sense = lesk(tokens, "bank")
print("Word:", "bank")
print("Sense:", sense)
print("Definition:", sense.definition())