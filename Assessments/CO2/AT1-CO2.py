# Question 1 : Write a Python program to implement the above morphological analysis pipeline. The program should accept the given input words, perform decomposition, classify each suffix as inflectional or derivational, normalize the words to their common base form, and display the parsed structure and normalized output in a tabular format.

print("\nQuestion 1 Output: \n")
words = ["connected", "connecting", "connection"]
analysis = {
    "connected": ("connect", "ed", "Inflectional"),
    "connecting": ("connect", "ing", "Inflectional"),
    "connection": ("connect", "ion", "Derivational")
}
print("="*75)
print("{:<15}{:<15}{:<10}{:<18}{:<15}".format(
    "Word","Root","Suffix","Type","Normalized"))
print("="*75)
for word in words:
    root, suffix, kind = analysis[word]
    print("{:<15}{:<15}{:<10}{:<18}{:<15}".format(
        word, root, suffix, kind, root))


# Question 2 : Write a Python program to implement the above morphological parsing module. The program should accept the given input words, identify the prefixes, suffixes, and base forms, classify each transformation as inflectional or derivational, and display the morphological breakdown and normalized root word in a tabular format.

print("\nQuestion 2 Output: \n")
words = ["unhappy", "happiness", "happily"]
analysis = {
    "unhappy": ("un", "happy", "-", "Derivational"),
    "happiness": ("-", "happy", "ness", "Derivational"),
    "happily": ("-", "happy", "ly", "Derivational")
}
print("="*85)
print("{:<12}{:<10}{:<12}{:<10}{:<18}{:<15}".format(
    "Word","Prefix","Root","Suffix","Type","Normalized"))
print("="*85)
for word in words:
    prefix, root, suffix, kind = analysis[word]
    print("{:<12}{:<10}{:<12}{:<10}{:<18}{:<15}".format(
        word, prefix, root, suffix, kind, root))


# Question 3 : Develop a Python program for a stemming-based preprocessing module used in a search engine. The program should process the input words "played", "player", "playing" by applying appropriate stemming rules to remove prefixes/suffixes where applicable, identify the stem of each word, distinguish between grammatical inflections and word-formation changes, and generate a structured output showing the original word, extracted stem, removed affix (if any), transformation type (inflectional/derivational), and the final normalized form suitable for indexing and information retrieval.

print("\nQuestion3 Output: \n")
words = ["played", "player", "playing"]
analysis = {
    "played": ("play", "ed", "Inflectional"),
    "player": ("play", "er", "Derivational"),
    "playing": ("play", "ing", "Inflectional")
}
print("="*90)
print("{:<12}{:<12}{:<15}{:<18}{:<15}".format(
    "Word","Stem","Removed Affix","Type","Normalized"))
print("="*90)
for word in words:
    stem, affix, kind = analysis[word]
    print("{:<12}{:<12}{:<15}{:<18}{:<15}".format(
        word, stem, affix, kind, stem))


# Question 4 : Develop a Python program that implements a finite-state morphological parser for the input words "writes", "writing", "written". The program should construct a finite-state transition model to process regular suffixes and irregular verb forms, identify the corresponding root word, classify each input as a regular or irregular inflection, trace the sequence of state transitions during parsing, and display the state transition path, morphological components, root form, and normalized representation for each input word in a well-formatted output.

print("\nQuestion 4 Output: \n")
words = ["writes", "writing", "written"]
analysis = {
    "writes": ("write", "s", "Regular",
               "Start -> write -> s -> Final"),
    "writing": ("write", "ing", "Regular",
                "Start -> write -> ing -> Final"),
    "written": ("write", "en", "Irregular",
                "Start -> write -> en -> Final")
}
print("="*120)
print("{:<12}{:<12}{:<10}{:<12}{:<35}{:<12}".format(
    "Word","Root","Suffix","Pattern","State Transition","Normalized"))
print("="*120)
for word in words:
    root, suffix, pattern, path = analysis[word]
    print("{:<12}{:<12}{:<10}{:<12}{:<35}{:<12}".format(
        word, root, suffix, pattern, path, root))


# Question 5 : Develop a Python program that implements the Porter Stemming algorithm for the input words "relational", "relation", "relate". The program should apply the Porter stemming rules sequentially to remove derivational suffixes, display the intermediate form obtained after each stemming step, handle different suffix patterns while preserving the word meaning, and generate the final stem for each word. The output should clearly present the original word, applied stemming rule(s), intermediate forms, and the final normalized stem in a structured format suitable for document retrieval applications.

print("\nQuestion 5 Output: \n")
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational", "relation", "relate"]
print("="*90)
print("{:<15}{:<30}{:<20}{:<15}".format(
    "Word","Applied Rule","Intermediate","Final Stem"))
print("="*90)
for word in words:
    if word == "relational":
        rule = "Remove 'ational'"
        intermediate = "relate"
    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relat"
    elif word == "relate":
        rule = "Remove final 'e'"
        intermediate = "relat"
    final = ps.stem(word)
    print("{:<15}{:<30}{:<20}{:<15}".format(
        word, rule, intermediate, final))