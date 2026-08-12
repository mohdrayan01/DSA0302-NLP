# 21.Create a python program that performs syntax-driven semantic analysis by extracting noun phrases and their meanings from a sentence.

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
sentence = "The intelligent student solved the difficult problem."
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(tags)
print(tree)
print("\nNoun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase)