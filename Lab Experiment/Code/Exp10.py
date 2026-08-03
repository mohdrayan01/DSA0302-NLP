# 10.Implement transformation-based tagging using a set of transformation rules, apply a simple rule to tag words using python.

sentence = ["I", "can", "play", "football"]
# Initial Tags
tags = ["PRP", "NN", "NN", "NN"]
print("Before Transformation:")
for w, t in zip(sentence, tags):
    print(w, "->", t)
# Transformation Rule:
# If previous word is "can", tag current word as Verb
for i in range(1, len(sentence)):
    if sentence[i-1].lower() == "can":
        tags[i] = "VB"
print("\nAfter Transformation:")
for w, t in zip(sentence, tags):
    print(w, "->", t)