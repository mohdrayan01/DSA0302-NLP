# 14.Create a program in python to check for agreement in sentences based on a context-free grammar's rules.

subjects = {
    "he": "is",
    "she": "is",
    "it": "is",
    "i": "am",
    "you": "are",
    "we": "are",
    "they": "are"
}
sentence = input("Enter a sentence: ").lower().split()
if len(sentence) >= 2:
    subject = sentence[0]
    verb = sentence[1]
    if subject in subjects:
        if subjects[subject] == verb:
            print("Sentence Agreement: Correct")
        else:
            print("Sentence Agreement: Incorrect")
    else:
        print("Unknown Subject")
else:
    print("Invalid Sentence")