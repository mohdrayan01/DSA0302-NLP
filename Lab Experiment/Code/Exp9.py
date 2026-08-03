# 9.Implement a rule-based part-of-speech tagging system using regular expressions using python.

import nltk
from nltk.tag import RegexpTagger
patterns = [
    (r'.*ing$', 'VBG'),     # Gerunds
    (r'.*ed$', 'VBD'),      # Past tense verbs
    (r'.*es$', 'VBZ'),      # Verbs ending with es
    (r'.*ould$', 'MD'),     # Modals
    (r'.*\'s$', 'NN$'),     # Possessive nouns
    (r'.*s$', 'NNS'),       # Plural nouns
    (r'.*ly$', 'RB'),       # Adverbs
    (r'.*able$', 'JJ'),     # Adjectives
    (r'.*', 'NN')           # Default noun
]
tagger = RegexpTagger(patterns)
sentence = "The dog is running quickly".split()
print(tagger.tag(sentence))