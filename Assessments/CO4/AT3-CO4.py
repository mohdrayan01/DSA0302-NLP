# Question 1: CFG Trees vs Dependency Parsing

print("\nQuestion 1 Output:\n")
sentence=["The","student","reads","a","book"]
print("CFG VS DEPENDENCY PARSING\n")
print("Sentence: The student reads a book.")
print("\nCFG Representation:")
print("S")
print("|-- NP")
print("|   |-- The")
print("|   |-- student")
print("|-- VP")
print("    |-- reads")
print("    |-- NP")
print("        |-- a")
print("        |-- book")
print("\nDependency Representation:")
dependencies=[
("reads","student","subject"),
("reads","book","object"),
("student","The","determiner"),
("book","a","determiner")
]
for head,dependent,relation in dependencies:
    print(head,"->",dependent,"(",relation,")")
print("\nConclusion:")
print("CFG is better for phrase structure.")
print("Dependency parsing is better for direct word relationships.")
print("Dependency parsing is preferred for relation extraction and semantic analysis.")

# Question 2: Top-Down Parsing vs Earley Parsing

print("\nQuestion 2 Output:\n")
sentence="Book a flight to Delhi"

print("TOP-DOWN VS EARLEY PARSING\n")

print("Input:",sentence)

print("\nTop-Down Parsing")
print("1. Start with S")
print("2. Expand S -> NP VP")
print("3. Generate possible grammar structures")
print("4. Match input")
print("5. Backtrack if required")

print("\nEarley Parsing")
print("1. Prediction")
print("2. Scanning")
print("3. Completion")
print("4. Store partial states in chart")
print("5. Continue when more input arrives")

comparison=[
("Ambiguity","Limited","Good"),
("Incomplete Input","Poor","Good"),
("Backtracking","High","Reduced"),
("Memory","Low","Higher"),
("Complex Grammar","Less Suitable","More Suitable")
]

print("\nComparison:")
print("Feature | Top-Down | Earley")

for feature,top,earley in comparison:
    print(feature,"|",top,"|",earley)

print("\nRecommended: Earley Parsing for dynamic and ambiguous input.")

# Question 3: CFG vs PCFG vs Neural Parsing

print("\nQuestion 3 Output:\n")
sentence="She saw the man with a telescope."
print("AMBIGUITY ANALYSIS\n")
print("Sentence:",sentence)
interpretations={
"Interpretation 1":"She used a telescope to see the man.",
"Interpretation 2":"The man had a telescope."
}
print("\nCFG:")
for key,value in interpretations.items():
    print(key,":",value)
print("\nPCFG Probabilities:")
pcfg={
"She used a telescope to see the man.":0.70,
"The man had a telescope.":0.30
}
for interpretation,probability in pcfg.items():
    print(interpretation,"->",probability)
best=max(pcfg,key=pcfg.get)
print("\nPCFG Selected Interpretation:")
print(best)
print("\nNeural Parsing:")
print("Uses contextual representations.")
print("Learns patterns from large datasets.")
print("Uses surrounding words to resolve ambiguity.")
print("\nFinal Comparison:")
print("CFG -> Generates possible parses")
print("PCFG -> Ranks parses using probabilities")
print("Neural -> Uses learned contextual information")
print("\nRecommended for real-world applications: Neural Parsing")

# Question 4: Feature Structures vs Subcategorization Frames

print("\nQuestion 4 Output:\n")
print("FEATURE STRUCTURES VS SUBCATEGORIZATION\n")
print("Example 1: The student reads.")
subject={
"word":"student",
"person":"Third",
"number":"Singular"
}
verb={
"word":"reads",
"person":"Third",
"number":"Singular",
"tense":"Present"
}
print("\nSubject Features:")
print(subject)
print("Verb Features:")
print(verb)
if subject["person"]==verb["person"] and subject["number"]==verb["number"]:
    print("Agreement: Correct")
else:
    print("Agreement: Error")
print("\nExample 2: The students reads.")
if "students"=="students" and "Singular"=="Plural":
    print("Agreement Error")
print("\nSubcategorization Frames:")
frames={
"eat":"eat + NP",
"give":"give + NP + NP",
"depend":"depend + PP",
"prescribe":"prescribe + NP + NP"
}
for verb,frame in frames.items():
    print(verb,"->",frame)
print("\nMedical Example:")
print("Doctor prescribed medicine to patient.")
print("Agent = Doctor")
print("Theme = Medicine")
print("Recipient = Patient")
print("\nConclusion:")
print("Feature Structures -> Agreement and grammatical correctness")
print("Subcategorization -> Verb argument structures")
print("Best approach -> Combine both")

# Question 5: Transition-Based vs Graph-Based Parsing

print("\nQuestion 5 Output:\n")
sentence=["The","student","reads","a","book"]
print("TRANSITION-BASED VS GRAPH-BASED PARSING\n")
print("Sentence:"," ".join(sentence))
print("\nTransition-Based Parsing")
stack=[]
buffer=sentence.copy()
while buffer:
    word=buffer.pop(0)
    stack.append(word)
    print("SHIFT:",word)
print("Final Stack:",stack)
print("\nTransition Actions:")
print("SHIFT")
print("REDUCE")
print("LEFT-ARC")
print("RIGHT-ARC")
print("\nGraph-Based Parsing")
dependencies=[
("reads","student"),
("reads","book"),
("student","The"),
("book","a")
]
print("Possible dependency relationships:")
for head,dependent in dependencies:
    print(head,"->",dependent)
print("\nGlobal Optimization:")
print("The parser evaluates possible dependency trees.")
print("The highest-scoring tree is selected.")
comparison=[
("Decision Making","Local","Global"),
("Speed","Very Fast","Slower"),
("Memory","Low","Higher"),
("Error Propagation","Higher","Lower"),
("Long Distance Relations","Difficult","Better"),
("Large Scale Use","Suitable","More Expensive")
]
print("\nComparison:")
print("Feature | Transition-Based | Graph-Based")
for feature,transition,graph in comparison:
    print(feature,"|",transition,"|",graph)
print("\nRecommendation:")
print("Transition-based parsing is preferred for large-scale and real-time applications.")
print("Graph-based parsing is preferred when global structural accuracy is more important.")