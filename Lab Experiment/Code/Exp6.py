# 6.Implement a basic N-gram model for text generation. For example, generate text using a bigram model using python.

import random
from nltk import bigrams
text = "I love natural language processing because natural language is interesting"
words = text.split()
bg = list(bigrams(words))
model = {}
for w1, w2 in bg:
    model.setdefault(w1, []).append(w2)
word = "natural"
generated = [word]
for i in range(8):
    if word in model:
        word = random.choice(model[word])
        generated.append(word)
    else:
        break
print("Generated Text:")
print(" ".join(generated))