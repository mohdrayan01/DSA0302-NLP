# 4.Implement a finite-state machine for morphological parsing. In this example, we'll create a simple machine to generate plural forms of English nouns using python.

def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"
words = ["cat", "bus", "box", "baby", "church"]
for word in words:
    print(word, "->", plural(word))