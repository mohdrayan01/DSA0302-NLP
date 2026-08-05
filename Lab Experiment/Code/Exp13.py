# 13.Generate a parse tree for a given sentence using a context-free grammar using python program.

import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a' | 'the'
N -> 'boy' | 'ball'
V -> 'kicked'
""")
parser = ChartParser(grammar)
sentence = "the boy kicked a ball".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()