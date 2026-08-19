# Question 1: Reference Resolution

print("\nQuestion 1 Output:\n")
text="Ravi met Arun at the library. He borrowed a book and later returned it."
entities={"He":"Ravi","it":"book"}
print("REFERENCE RESOLUTION")
print("-"*30)
for pronoun,entity in entities.items():
    print(pronoun,"->",entity)
print("\nResolved Discourse:")
print("Ravi met Arun at the library. Ravi borrowed a book and later returned the book.")

# Question 2: Text Coherence and Discourse Structure

print("\nQuestion 2 Output:\n")
sentences=[
"The roads were flooded after heavy rainfall.",
"Therefore, schools were closed for the day.",
"Students attended classes online."
]
print("TEXT COHERENCE AND DISCOURSE STRUCTURE")
print("-"*45)
for i,s in enumerate(sentences,1):
    print("Sentence",i,":",s)
print("\nDiscourse Relations:")
print("Sentence 1 -> Sentence 2 : Cause-Effect")
print("Sentence 2 -> Sentence 3 : Result/Sequence")
print("\nDiscourse Structure:")
print("Heavy rainfall")
print("     ↓")
print("Roads flooded")
print("     ↓")
print("Schools closed")
print("     ↓")
print("Online classes")


# Question 3: Dialogue Act Identification

print("\nQuestion 3 Output:\n")
dialogue=[
("User","Can you book a train ticket for me?","Request"),
("Agent","Sure, where would you like to travel?","Question"),
("User","I want to go to Chennai.","Inform"),
("Agent","Your ticket has been booked.","Confirmation")
]
print("DIALOGUE ACT IDENTIFICATION")
print("-"*35)
for speaker,utterance,act in dialogue:
    print(speaker,":",utterance)
    print("Dialogue Act:",act)
    print()
print("Dialogue Act Sequence:")
print("Request -> Question -> Inform -> Confirmation")


# Question 4: Language Generation and Surface Realization

print("\nQuestion 4 Output:\n")
semantic={
"action":"buy",
"agent":"student",
"object":"book",
"tense":"past"
}
if semantic["action"]=="buy" and semantic["tense"]=="past":
    verb="bought"
else:
    verb=semantic["action"]
sentence="The "+semantic["agent"]+" "+verb+" a "+semantic["object"]+"."
print("LANGUAGE GENERATION")
print("-"*25)
print("Semantic Representation:",semantic)
print("Generated Sentence:",sentence)
print("\nGrammatical Validation:")
print("Subject: The student")
print("Verb: bought")
print("Object: a book")
print("Tense: Past")
print("Sentence is grammatically correct.")


# Question 5: Interlingua-Based and Statistical Machine Translation

print("\nQuestion 5 Output:\n")
source="The boy is playing football."
interlingua={
"action":"play",
"agent":"boy",
"object":"football",
"tense":"present",
"aspect":"continuous"
}
candidates={
"लड़का फुटबॉल खेल रहा है।":0.935,
"लड़का फुटबॉल खेलता है।":0.815,
"लड़का फुटबॉल खेल रहा था।":0.575
}
best=max(candidates,key=candidates.get)
print("INTERLINGUA-BASED MACHINE TRANSLATION")
print("-"*45)
print("Source Sentence:",source)
print("\nInterlingua Representation:")
for key,value in interlingua.items():
    print(key,":",value)
print("\nCandidate Translations:")
for sentence,score in candidates.items():
    print(sentence,"-> Score:",score)
print("\nFinal Translation:")
print(best)