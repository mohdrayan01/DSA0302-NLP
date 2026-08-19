# Question 1: Coreference Resolution

print("\nQuestion 1 Output:\n")
text="John and Mary went to the park. He brought a ball. She wanted to play with it. The dog chased him excitedly. Finally, they all went home."
entities={"He":"John","She":"Mary","it":"ball","him":"John","they":"John, Mary and the dog"}
print("COREference Resolution")
print("-"*35)
for mention,antecedent in entities.items():
    print(mention,"->",antecedent)
print("\nResolved Paragraph:")
print("John and Mary went to the park. John brought a ball. Mary wanted to play with the ball. The dog chased John excitedly. Finally, John, Mary and the dog all went home.")


# Question 2: Dialog Planning and Response Generation

print("\nQuestion 2 Output:\n")
user="I have an important exam tomorrow but I’m not able to concentrate."
print("User:",user)
print("\nGenerated Responses:")
responses=[
"Because your exam is important, take a short break and then focus on one topic at a time. Stay confident and trust yourself.",
"Since your exam is tomorrow, take a short break if you cannot concentrate, then return and focus on one topic. You can feel confident by preparing step by step.",
"Take a short break if you cannot concentrate, then come back and focus on your exam one topic at a time. Stay confident and remember that you can do your best."
]
for i,r in enumerate(responses,1):
    print("\nResponse",i,":",r)
print("\nBest Response:")
print(responses[1])


# Question 3: Word Sense Disambiguation and Predicate Logic

print("\nQuestion 3 Output:\n")
sentence="The bank by the river flooded after the storm, but it was saved by quick action."
print("Original Sentence:")
print(sentence)
word="bank"
context=["river","flooded","storm"]
if "river" in context and "flooded" in context:
    sense="riverbank"
else:
    sense="financial institution"
print("\nWord Sense:")
print("bank ->",sense)
print("\nPredicate Logic:")
print("RiverBank(b)")
print("By(b,r)")
print("Flood(b)")
print("After(Flood(b),Storm(s))")
print("Saved(b,QuickAction(a))")
print("\nParaphrase:")
print("The riverbank near the river flooded after the storm, but quick action saved it.")