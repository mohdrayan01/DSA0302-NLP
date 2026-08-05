# 11.Implement a simple top-down parser for context-free grammars using python.

import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased'
""")
parser = RecursiveDescentParser(grammar)
sentence = "the cat chased the dog".split()
for tree in parser.parse(sentence):
    print(tree)