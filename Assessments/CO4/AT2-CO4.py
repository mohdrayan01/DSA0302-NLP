# Question 1: Banking Chatbot – CFG, PCFG and Feature Structures

print("\nQuestion 1 Output:\n")
import re
query="Show me the transactions with the card from last month"
print("BANKING CHATBOT SEMANTIC ANALYSIS\n")
print("Query:",query)
grammar={
"S":["VP"],
"VP":["V NP","V NP PP"],
"NP":["Det N","NP PP"],
"PP":["P NP"]
}
print("\nCFG Rules:")
for rule,values in grammar.items():
    for value in values:
        print(rule,"->",value)
print("\nAmbiguity:")
print("PP 'with the card' may attach to the transaction phrase.")
print("PP 'from last month' specifies the time period.")
semantic={
"Intent":"SHOW_TRANSACTIONS",
"Payment_Method":"CARD",
"Time_Period":"LAST_MONTH"
}
print("\nPCFG Ranking:")
parses={
"Transactions + Card + Last Month":0.60,
"Alternative PP attachment":0.40
}
for parse,prob in parses.items():
    print(parse,"=",prob)
best=max(parses,key=parses.get)
print("Selected Interpretation:",best)
print("\nFeature Structure:")
features={
"Person":"Third",
"Number":"Singular",
"Tense":"Present"
}
for feature,value in features.items():
    print(feature,"=",value)
print("\nFinal Semantic Representation:")
for key,value in semantic.items():
    print(key,"=",value)


# Question 2: Voice Assistant – Top-Down vs Earley Parsing

print("\nQuestion 2 Output:\n")
sentence="Book a flight to Delhi with a window seat"
print("VOICE ASSISTANT PARSING\n")
print("Input:",sentence)
print("\nPossible Parse 1:")
print("[Book [a flight to Delhi] [with a window seat]]")
print("\nPossible Parse 2:")
print("[Book [a flight [to Delhi with a window seat]]]")
print("\nTop-Down Parsing:")
print("Starts from S")
print("May require backtracking")
print("Poorer handling of incomplete input")
print("\nEarley Parsing:")
print("Uses chart parsing")
print("Prediction")
print("Scanning")
print("Completion")
print("Maintains multiple hypotheses")
print("\nPerformance Comparison:")
methods={
"Top-Down":{
"Ambiguity":"Limited",
"Partial Input":"Poor",
"Backtracking":"High",
"Memory":"Low"
},
"Earley":{
"Ambiguity":"Good",
"Partial Input":"Good",
"Backtracking":"Reduced",
"Memory":"Higher"
}
}
for method,values in methods.items():
    print("\n",method)
    for key,value in values.items():
        print(key,":",value)
print("\nFinal Interpretation:")
print("Intent = BOOK_FLIGHT")
print("Destination = Delhi")
print("Seat Preference = Window")

# Question 3: Healthcare NLP Architecture

print("\nQuestion 3 Output:\n")
import re
text="The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai."
print("HEALTHCARE NLP SYSTEM\n")
print("Input:",text)
tokens=text.replace(".","").split()
print("\nTokens:")
print(tokens)
entities={
"doctor":"Person/Medical Entity",
"patient":"Medical Entity",
"medication":"Treatment",
"Chennai":"Location"
}
print("\nMedical Entities:")
for entity,category in entities.items():
    print(entity,"->",category)
print("\nCFG Structure:")
print("S -> NP VP")
print("NP -> Det N RelClause")
print("VP -> V GerundPhrase")
print("VP -> VP Conjunction VP")
print("\nFeature Structure:")
print("Doctor -> Number = Singular")
print("Recommends -> Number = Singular")
print("Agreement = Correct")
print("\nSemantic Analysis:")
print("REVIEW(Doctor, Patient, Last_Week)")
print("RECOMMEND(Doctor, Start(Medication))")
print("RECOMMEND(Doctor, Schedule(Follow_Up_Visit))")
print("LOCATION(Follow_Up_Visit, Chennai)")
print("\nStructured Output:")
output={
"Agent":"Doctor",
"Reviewed Entity":"Patient",
"Review Time":"Last Week",
"Main Action":"Recommend",
"Treatment":"Starting Medication",
"Follow-up Action":"Schedule Follow-up Visit",
"Location":"Chennai",
"Diagnosis":"Not Specified"
}
for key,value in output.items():
    print(key,":",value)
print("\nSubcategorization Frames:")
frames={
"RECOMMEND":"Doctor + Treatment/Action",
"PRESCRIBE":"Doctor + Medicine + Patient",
"REVIEW":"Doctor + Patient/Report",
"MONITOR":"Doctor/Nurse + Patient",
"SCHEDULE":"Agent + Appointment",
"DIAGNOSE":"Doctor + Patient + Condition"
}
for verb,frame in frames.items():
    print(verb,"->",frame)
print("\nReal-Time Processing Pipeline:")
print("Input -> Queue -> Preprocessing -> NER/POS -> Parsing -> Semantic Analysis -> Database")

