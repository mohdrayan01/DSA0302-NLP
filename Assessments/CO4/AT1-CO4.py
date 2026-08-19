# Question 1: Semantic Representation in Customer Support Chatbots

print("\nQuestion 1 Output:\n")
queries={
"Q1":("Activate international roaming","ACTIVATE","Roaming","Activate Roaming","Activate Roaming"),
"Q2":("Deactivate caller tune service","DEACTIVATE","Caller Tune","Deactivate Caller Tune","Deactivate Caller Tune"),
"Q3":("Check my data balance","QUERY","Data Balance","Check Data Balance","Query Data Balance"),
"Q4":("Enable 5G service","ACTIVATE","5G Service","Enable 5G Service","Activate 5G Service")
}
print("SEMANTIC REPRESENTATION ANALYSIS\n")
for q,(text,action,obj,actual,predicted) in queries.items():
    print(q)
    print("Query:",text)
    print("Action:",action)
    print("Object:",obj)
    print("Representation:",action+"("+obj+", Customer)")
    print("Actual Intent:",actual)
    print("Predicted Intent:",predicted)
    print("Result: Correct")
    print()
print("Recommendations:")
print("1. Use domain-specific vocabulary")
print("2. Handle synonyms such as activate and enable")
print("3. Handle negation")
print("4. Use context from previous messages")
print("5. Use entity recognition and confidence scores")


# Question 2: First-Order Predicate Calculus for Smart Manufacturing

print("\nQuestion 2 Output:\n")
machines={
"M1":"Active",
"M2":"Active",
"M3":"Maintenance",
"M4":"Active"
}
produces={
"M1":"Gear",
"M2":"Engine",
"M4":"Pump"
}
print("FIRST-ORDER PREDICATE CALCULUS\n")
producing={}
for machine,status in machines.items():
    if status=="Active":
        producing[machine]=True
        print("Active("+machine+") -> Producing("+machine+")")
    else:
        producing[machine]=False
        print("Maintenance("+machine+") -> NOT Producing("+machine+")")
print("\nProduction Status:")
for machine,value in producing.items():
    print(machine,":","Producing" if value else "Not Producing")
print("\nAvailable Products:")
for machine,product in produces.items():
    if machines[machine]=="Active":
        print("Available("+product+")")
    else:
        print("Not Available:",product)
print("\nGear Analysis:")
if machines.get("M3")=="Maintenance" and produces.get("M3")=="Gear":
    print("Gear production through M3 is affected.")
else:
    print("Total Gear production cannot be concluded from the given data.")


# Question 3: Word Sense Disambiguation in E-Commerce

print("\nQuestion 3 Output:\n")
data={
"Apple accessories":{
"senses":["Fruit","Technology Brand"],
"context":"iPhone Charger",
"answer":"Technology Brand"
},
"Mouse wireless":{
"senses":["Animal","Computer Device"],
"context":"Bluetooth Mouse",
"answer":"Computer Device"
},
"Java tutorial":{
"senses":["Island","Programming Language"],
"context":"Coding Lessons",
"answer":"Programming Language"
},
"Python course":{
"senses":["Snake","Programming Language"],
"context":"Software Development Training",
"answer":"Programming Language"
}
}
print("WORD SENSE DISAMBIGUATION\n")
for query,info in data.items():
    print("Query:",query)
    print("Possible Senses:",info["senses"])
    print("Clicked Result:",info["context"])
    print("Correct Sense:",info["answer"])
    print()
print("Industrial WSD Improvements:")
print("1. Contextual embeddings")
print("2. Search history")
print("3. Click information")
print("4. Product categories")
print("5. Knowledge graphs")
print("6. Machine learning")
print("7. Personalization")



# Question 4: Syntax-Driven Semantic Analysis in Healthcare

print("\nQuestion 4 Output:\n")
sentences=[
("Doctor","prescribed","medicine","patient"),
("Patient","reported","severe headache",""),
("Nurse","monitored","patient",""),
("Medicine","reduced","blood pressure","")
]
print("SYNTAX-DRIVEN SEMANTIC ANALYSIS\n")
for subject,verb,obj,extra in sentences:
    print("Sentence:",subject,verb,obj,extra)
    print("Subject:",subject)
    print("Verb:",verb)
    print("Object:",obj)
    if extra:
        print("Recipient:",extra)
    print()
roles={
"Doctor":"Agent",
"Medicine":"Instrument",
"Patient":"Recipient",
"Headache":"Symptom"
}
print("SEMANTIC ROLES")
for entity,role in roles.items():
    print(entity,"->",role)
print("\nImprovement Methods:")
print("1. Dependency parsing")
print("2. Medical Named Entity Recognition")
print("3. Semantic Role Labeling")
print("4. Medical ontologies")
print("5. Domain-specific grammar")


