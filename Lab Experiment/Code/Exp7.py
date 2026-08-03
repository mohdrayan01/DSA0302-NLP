# 7.Write program using the NLTK library to perform part-of-speech tagging on a text.

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
print(tags)