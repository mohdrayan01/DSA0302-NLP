# 22.Create a python program that performs reference resolution within a text.

import nltk
text = "John went to school. He studied well."
sentences = nltk.sent_tokenize(text)
previous_noun = None
pronouns = ["he", "she", "him", "her", "they"]
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    for word, tag in tags:
        if tag == "NNP":
            previous_noun = word
        elif word.lower() in pronouns:
            print(f"{word} -> refers to {previous_noun}")