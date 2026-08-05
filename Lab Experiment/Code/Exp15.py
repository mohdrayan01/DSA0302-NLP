# 15.Implement probabilistic context-free grammar parsing for a sentence using python.

import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'chased' [1.0]
""")
parser = ViterbiParser(grammar)
sentence = "John chased the dog".split()
for tree in parser.parse(sentence):
    print(tree)