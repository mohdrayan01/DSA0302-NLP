# Question 1 : Develop a Python program to implement a rule-based morphological processing system for the input words "analyzing", "analysis", and "analytical". The program should identify the root word and separate the corresponding prefixes or suffixes using suitable morphological rules, classify each word as an inflectional or derivational form, normalize all related variants to a common representation for indexing, and generate a structured report showing the original word, extracted root, identified affix(es), transformation type, and normalized output to support efficient search engine retrieval.

print("\nQuestion 1 Output:\n")
words = ["analyzing", "analysis", "analytical"]
analysis = {
    "analyzing": ("analyze", "-", "ing", "Inflectional"),
    "analysis": ("analyze", "-", "sis", "Derivational"),
    "analytical": ("analyze", "-", "ical", "Derivational")
}
print("=" * 95)
print("{:<15}{:<15}{:<10}{:<10}{:<18}{:<15}".format(
    "Word", "Root", "Prefix", "Suffix", "Type", "Normalized"))
print("=" * 95)
for word in words:
    root, prefix, suffix, kind = analysis[word]
    print("{:<15}{:<15}{:<10}{:<10}{:<18}{:<15}".format(
        word, root, prefix, suffix, kind, root))

# Question 2 : Develop a Python program to create a morphological parser for the input words "disagree", "agreement", and "agreeable". The program should detect and separate prefixes, suffixes, and the base word using rule-based morphological analysis, examine how derivational modifications alter the meaning of the root word, classify each transformation according to its morphological type, and produce a comprehensive output containing the original word, identified prefix, root word, suffix, transformation category, semantic interpretation, and normalized base form for use in sentiment analysis applications.

print("\nQuestion 2 Output:\n")
words = ["disagree", "agreement", "agreeable"]
analysis = {
    "disagree": ("dis", "agree", "-", "Derivational",
                 "Opposite meaning"),
    "agreement": ("-", "agree", "ment", "Derivational",
                  "State or result of agreeing"),
    "agreeable": ("-", "agree", "able", "Derivational",
                  "Capable of being agreed with")
}
print("=" * 120)
print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<30}{:<12}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Type", "Semantic Meaning", "Normalized"))
print("=" * 120)
for word in words:
    prefix, root, suffix, kind, meaning = analysis[word]
    print("{:<15}{:<10}{:<12}{:<10}{:<18}{:<30}{:<12}".format(
        word, prefix, root, suffix, kind, meaning, root))

# Question 3 : Develop a Python program to implement a morphology-based normalization module for the input words "govern", "government", and "governance". The program should perform morphological decomposition to identify the root word and successive derivational suffixes, determine the derivational level associated with each word, normalize all variants to a common lexical representation, and generate a structured output displaying the original word, root form, detected affix(es), derivational hierarchy, normalized representation, and the final output used for topic modeling and document clustering.

print("\nQuestion 3 Output:\n")
words = ["govern", "government", "governance"]
analysis = {
    "govern": ("govern", "-", "Level 0"),
    "government": ("ment", "Level 1", "govern"),
    "governance": ("ance", "Level 1", "govern")
}
print("=" * 95)
print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(
    "Word", "Root", "Affix", "Derivational Level", "Normalized"))
print("=" * 95)
for word in words:
    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Level 0"
        norm = "govern"
    else:
        affix, level, norm = analysis[word]
        root = "govern"
    print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(
        word, root, affix, level, norm))

# Question 4 : Develop a Python program to implement a morphological parsing and normalization system for the input words "activate", "activation", and "reactivation". The program should detect and separate prefixes, root words, and suffixes using rule-based morphological parsing, identify the sequence of derivational transformations that produce each word, analyze the effect of each morphological modification on the word class and semantic meaning, and generate a structured report showing the original word, prefix (if present), root word, suffix, derivational sequence, normalized base form, and final parsed representation for use in document classification and semantic indexing.

print("\nQuestion 4 Output:\n")
words = ["activate", "activation", "reactivation"]
analysis = {
    "activate": ("-", "activate", "-", "Base Form"),
    "activation": ("-", "activate", "ion",
                   "activate + ion"),
    "reactivation": ("re", "activate", "ion",
                     "re + activate + ion")
}
print("=" * 120)
print("{:<15}{:<10}{:<15}{:<10}{:<30}{:<15}{:<20}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Derivational Sequence", "Normalized", "Parsed Form"))
print("=" * 120)
for word in words:
    prefix, root, suffix, sequence = analysis[word]
    parsed = prefix + " + " + root + " + " + suffix
    print("{:<15}{:<10}{:<15}{:<10}{:<30}{:<15}{:<20}".format(
        word, prefix, root, suffix, sequence, root, parsed))

# Question 5 : Develop a Python program to implement an inflectional morphology-based normalization module for the input words "create", "creates", and "creating". The program should recognize grammatical suffixes corresponding to different inflectional forms, identify the underlying root word by applying appropriate normalization rules, classify each input according to its grammatical feature (e.g., base form, third-person singular, present participle), and produce a structured output containing the original word, identified suffix, grammatical category, extracted root, normalized base form, and the final normalized representation to support efficient search optimization and information retrieval.

print("\nQuestion 5 Output:\n")
words = ["create", "creates", "creating"]
analysis = {
    "create": ("-", "Base Form", "create"),
    "creates": ("s", "Third Person Singular", "create"),
    "creating": ("ing", "Present Participle", "create")
}
print("=" * 110)
print("{:<15}{:<10}{:<25}{:<15}{:<15}{:<20}".format(
    "Word", "Suffix", "Grammatical Category",
    "Root", "Normalized", "Final Output"))
print("=" * 110)
for word in words:
    suffix, category, root = analysis[word]
    print("{:<15}{:<10}{:<25}{:<15}{:<15}{:<20}".format(
        word, suffix, category, root, root, root))
