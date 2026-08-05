# 12.Implement an Earley parser for context-free grammars using a simple python program.

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased'
""")
parser = EarleyChartParser(grammar)
sentence = "the cat chased the dog".split()
for tree in parser.parse(sentence):
    print(tree)