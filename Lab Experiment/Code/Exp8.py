# 8.Implement a simple stochastic part-of-speech tagging algorithm using a basic probabilistic model to assign POS tags using python.

import random
training_data = {
    "book": ["NN", "VB"],
    "run": ["NN", "VB"],
    "dog": ["NN"],
    "is": ["VBZ"],
    "beautiful": ["JJ"]
}
sentence = ["book", "is", "beautiful"]
print("POS Tags:")
for word in sentence:
    if word in training_data:
        tag = random.choice(training_data[word])
    else:
        tag = "NN"
    print(word, "->", tag)