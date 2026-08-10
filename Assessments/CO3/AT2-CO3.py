# 1 — Smart Mobile Keyboard Prediction System

print("\nQuestion 1 Output: \n")
import math
print("="*60)
print("SMART MOBILE KEYBOARD PREDICTION SYSTEM")
print("="*60)

count_data=3
count_data_science=3
count_science=3
count_science_is=2
count_data_science_is=2
total_words=14
count_is=2
count_improves=0

p_science_data=count_data_science/count_data
print("\n1. MLE")
print("P(science|data) =",p_science_data)

print("\n2. BACKOFF")
p_tri=0
p_bi=0
p_uni=count_improves/total_words
print("P(improves|data,science) =",p_tri)
print("P(improves|science) =",p_bi)
print("P(improves) =",p_uni)
print("Final Backoff Probability =",p_uni)

lambda1=0.5
lambda2=0.3
lambda3=0.2

p_trigram=count_data_science_is/count_data_science
p_bigram=count_science_is/count_science
p_unigram=count_is/total_words

interpolation=(lambda1*p_trigram)+(lambda2*p_bigram)+(lambda3*p_unigram)

print("\n3. DELETED INTERPOLATION")
print("Trigram =",p_trigram)
print("Bigram =",p_bigram)
print("Unigram =",p_unigram)
print("Interpolated Probability =",interpolation)

p_is=0.66
p_drives=0.33
entropy=-(p_is*math.log2(p_is)+p_drives*math.log2(p_drives))

print("\n4. ENTROPY")
print("Entropy =",round(entropy,4),"bits")


# 2 — AI-Powered Customer Support Chatbot

print("\nQuestion 2 Output: \n")
print("="*60)
print("AI-POWERED CUSTOMER SUPPORT CHATBOT")
print("="*60)

sentence1=[("Book","VB"),("a","DT"),("flight","NN"),("ticket","NN"),("now","RB")]
sentence2=[("This","DT"),("book","NN"),("is","VBZ"),("interesting","JJ")]

print("\n1. POS TAGGING")
print("\nSentence 1:")
for word,tag in sentence1:
    print(word,"/",tag)

print("\nSentence 2:")
for word,tag in sentence2:
    print(word,"/",tag)

p_book_vb=0.6
p_book_nn=0.4
p_start_vb=0.5
p_start_nn=0.5

prob_vb=p_start_vb*p_book_vb
prob_nn=p_start_nn*p_book_nn

print("\n2. HMM PROBABILITY")
print("P(book,VB) =",prob_vb)
print("P(book,NN) =",prob_nn)

if prob_vb>prob_nn:
    print("Prediction: VB")
else:
    print("Prediction: NN")

print("\n3. TAGGING COMPARISON")
print("Rule-Based: Uses manually defined grammatical rules.")
print("HMM: Uses probabilities learned from training data.")
print("HMM is more suitable for large-scale systems.")

print("\n4. POS TAGSET")
print("VB = Verb")
print("NN = Noun")
print("JJ = Adjective")
print("RB = Adverb")
print("DT = Determiner")
print("VBZ = Third-person singular verb")
print("Standard POS tags improve intent detection and response generation.")


# 3 — News Analytics and POS Tag Correction

print("\nQuestion 3 Output: \n")
import math

print("="*60)
print("NEWS ANALYTICS AND POS TAG CORRECTION")
print("="*60)

sentence=[["economic","JJ"],["growth","NN"],["increases","NNS"],["employment","NN"]]

print("\n1. INITIAL TAGS")
for word,tag in sentence:
    print(word,"/",tag)

for i in range(1,len(sentence)):
    if sentence[i][1]=="NNS" and sentence[i-1][1]=="NN":
        sentence[i][1]="VBZ"

print("\nAFTER TRANSFORMATION")
for word,tag in sentence:
    print(word,"/",tag)

print("\n2. CORRECTION")
print("increases changes from NNS to VBZ because it follows growth/NN.")
print("The singular subject 'growth' requires the singular verb 'increases'.")

frequencies={"economic":120,"growth":450,"increases":210,"employment":380}
total=sum(frequencies.values())

print("\n3. FREQUENCY DISTRIBUTION")
print("Total =",total)

for word,count in frequencies.items():
    probability=count/total
    print(word,"Count =",count,"Probability =",round(probability,4))

def entropy(values):
    h=0
    for p in values:
        if p>0:
            h-=p*math.log2(p)
    return h

before=entropy([0.5,0.5])
after=entropy([0.9,0.1])

print("\n4. ENTROPY")
print("Before Transformation =",round(before,4),"bits")
print("After Transformation =",round(after,4),"bits")

if after<before:
    print("Entropy decreased.")
    print("Tagging uncertainty decreased and confidence increased.")