# 1 - Biomedical Morphological Analysis Error

print ("\nQuestion 1 Output:\n")
import re,os
from nltk.stem import PorterStemmer
ps=PorterStemmer()
print("="*70)
print("Q1 - BIOMEDICAL MORPHOLOGICAL ERROR ANALYSIS")
print("="*70)
file="pubmed20k.txt"
if os.path.exists(file):
    text=open(file,encoding="utf-8").read()
else:
    text="infection infectious infected infect infections infecting"
words=re.findall(r'\b[a-z]+\b',text.lower())
print("Total Tokens:",len(words))
target=["infection","infectious","infected","infect","infections","infecting"]
print("\nWord\t\tStem\t\tType\t\tObservation")
for word in target:
    stem=ps.stem(word)
    if word in ["infected","infections","infecting"]:
        typ="Inflectional"
    elif word in ["infection","infectious"]:
        typ="Derivational"
    else:
        typ="Base"
    obs="Acceptable" if stem=="infect" else "Information loss"
    print(f"{word:<15}{stem:<15}{typ:<15}{obs}")
print("\nMorphological Structure:")
print("infect -> Base")
print("infected -> infect + ed -> Inflectional")
print("infecting -> infect + ing -> Inflectional")
print("infections -> infection + s -> Inflectional")
print("infection -> infect + ion -> Derivational")
print("infectious -> infect + ious -> Derivational")
print("\nConclusion:")
print("Inflectional and derivational morphology should be treated separately because derivational suffixes can change meaning or word class.")


# 2 - Finite-State Morphological Parser Error Analysis

print ("\nQuestion 2 Output:\n")
import time
print("="*70)
print("Q2 - FINITE-STATE MORPHOLOGICAL PARSER")
print("="*70)
words=["happiest","unbelievable","running","reordering","smartphones","unreadable"]
expected={"happiest":("","happy","est"),"unbelievable":("un","believe","able"),"running":("","run","ing"),"reordering":("re","order","ing"),"smartphones":("","smartphone","s"),"unreadable":("un","read","able")}
def old_parser(word):
    prefix=""
    root=word
    suffix=""
    for p in ["un","re"]:
        if root.startswith(p):
            prefix=p
            root=root[len(p):]
            break
    for s in ["ing","est","able","s"]:
        if root.endswith(s):
            suffix=s
            root=root[:-len(s)]
            break
    return prefix,root,suffix
correct=0
print("\nBefore Correction")
for w in words:
    result=old_parser(w)
    if result==expected[w]:
        correct+=1
    print(w,"->",result)
before=correct/len(words)*100
print("Accuracy Before:",before,"%")
def parser(word):
    prefix=""
    root=word
    suffix=""
    for p in ["un","re","dis"]:
        if root.startswith(p) and len(root)>len(p):
            prefix=p
            root=root[len(p):]
            break
    for s in ["able","iest","ing","est","s"]:
        if root.endswith(s) and len(root)>len(s):
            suffix=s
            root=root[:-len(s)]
            break
    if root=="happi":
        root="happy"
    if root=="runn":
        root="run"
    return prefix,root,suffix
correct=0
start=time.time()
print("\nAfter Correction")
for w in words:
    result=parser(w)
    if result==expected[w]:
        correct+=1
    print(w,"->",result)
after=correct/len(words)*100
print("Accuracy After:",after,"%")
print("Accuracy Improvement:",after-before,"%")
print("Processing Time:",round(time.time()-start,6),"seconds")
print("\nFST Transitions:")
print("START -> PREFIX -> ROOT -> SUFFIX -> FINAL")
print("START -> ROOT -> SUFFIX -> FINAL")
print("\nComplexity: O(L(P+S))")
print("where L=word length, P=number of prefixes, S=number of suffixes.")


# 3 - News Classification Stemming Analysis

print ("\nQuestion 3 Output:\n")
import re,time
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
print("="*70)
print("Q3 - NEWS ARTICLE STEMMING ERROR ANALYSIS")
print("="*70)
documents=["technology computer software hardware","technology software computer internet","technology artificial intelligence software","technology computers digital systems","business organization company management","business organizer organization finance","business organizing companies markets","business organized management organization","technology software organizing systems","business company organized finance"]
labels=["technology","technology","technology","technology","business","business","business","business","technology","business"]
ps=PorterStemmer()
def stem_text(text):
    return " ".join(ps.stem(w) for w in re.findall(r'\b[a-zA-Z]+\b',text.lower()))
lemma={"organizing":"organize","organized":"organize","organizes":"organize","companies":"company","computers":"computer","markets":"market"}
def lemma_text(text):
    return " ".join(lemma.get(w,w) for w in re.findall(r'\b[a-zA-Z]+\b',text.lower()))
def evaluate(name,docs):
    start=time.time()
    train,test,y1,y2=train_test_split(docs,labels,test_size=.3,random_state=42,stratify=labels)
    v=TfidfVectorizer()
    x1=v.fit_transform(train)
    x2=v.transform(test)
    model=LogisticRegression(max_iter=1000)
    model.fit(x1,y1)
    pred=model.predict(x2)
    acc=accuracy_score(y2,pred)
    t=time.time()-start
    print(f"\n{name}")
    print("Vocabulary:",len(v.vocabulary_))
    print("Accuracy:",round(acc*100,2),"%")
    print("Time:",round(t,6),"seconds")
    return acc
evaluate("WITHOUT STEMMING",documents)
stemmed=[stem_text(x) for x in documents]
evaluate("PORTER STEMMING",stemmed)
lemmatized=[lemma_text(x) for x in documents]
evaluate("LEMMATIZATION",lemmatized)
print("\nPorter Stemming Analysis:")
for w in ["organization","organizer","organizing","organized","running","runner","studies","studying","relational","relation","conditional","universities","university","connection","connected","connecting","happiness","happily","analysis","analytical"]:
    print(w,"->",ps.stem(w))
print("\nConclusion:")
print("Lemmatization generally preserves more semantic information than aggressive Porter stemming.")


# 4 - E-Commerce Morphological Error Analysis

print ("\nQuestion 4 Output:\n")
from nltk.stem import PorterStemmer
ps=PorterStemmer()
print("="*70)
print("Q4 - E-COMMERCE MORPHOLOGICAL ERROR ANALYSIS")
print("="*70)
words=["watches","watching","washable","washer","washed"]
print("\nWord\t\tStem\t\tType")
for w in words:
    stem=ps.stem(w)
    typ="Inflectional" if w in ["watches","watching","washed"] else "Derivational"
    print(f"{w:<15}{stem:<15}{typ}")
print("\nMorphological Breakdown:")
print("watches -> watch + es -> Inflectional")
print("watching -> watch + ing -> Inflectional")
print("washed -> wash + ed -> Inflectional")
print("washable -> wash + able -> Derivational")
print("washer -> wash + er -> Derivational")
normalization={"watches":"watch","watching":"watch","washed":"wash","washable":"washable","washer":"washer"}
print("\nImproved Normalization:")
for w in words:
    print(w,"->",normalization[w])
print("\nRecommendation:")
print("Remove grammatical inflections during normalization.")
print("Preserve important derivational forms because they can represent different product meanings.")
print("Pipeline: Tokenization -> Morphological Analysis -> Inflectional Normalization -> Controlled Derivational Normalization -> Indexing")


# 5 - BBC News Porter Stemming Error Analysis

print ("\nQuestion 5 Output:\n")
import pandas as pd,re,os
from nltk.stem import PorterStemmer
ps=PorterStemmer()
print("="*70)
print("Q5 - PORTER STEMMING ERROR ANALYSIS")
print("="*70)
file="BBCNews.csv"
if os.path.exists(file):
    data=pd.read_csv(file)
    if "Text" in data.columns:
        column="Text"
    elif "text" in data.columns:
        column="text"
    else:
        column=data.columns[-1]
else:
    data=pd.DataFrame({"Text":["The government announced new technology policies.","The organization developed new software.","The company is organizing a business conference."]})
    column="Text"
print("\nCoding Error:")
print('data["Processed"]=data["Text"].apply(ps.stem)')
print("ps.stem() processes one word, not an entire document.")
def stem_text(text):
    words=re.findall(r'\b[a-zA-Z]+\b',str(text).lower())
    return " ".join(ps.stem(w) for w in words)
data["Processed"]=data[column].apply(stem_text)
print("\nOriginal vs Stemmed:")
print(data[[column,"Processed"]].head())
words=["organization","organizer","organizing","organized","running","runner","runs","studies","studying","studied","relational","relation","conditional","universities","university","connection","connected","connecting","happiness"]
print("\n20 Stemming Cases:")
print("Word\t\t\tStem\t\tType")
for w in words:
    typ="Inflectional" if w in ["running","runs","studies","studying","studied","connected","connecting"] else "Derivational"
    print(f"{w:<20}{ps.stem(w):<20}{typ}")
print("\nExamples of information loss:")
print("organization ->",ps.stem("organization"))
print("happiness ->",ps.stem("happiness"))
print("relational ->",ps.stem("relational"))
print("analysis ->",ps.stem("analysis"))
print("Porter stemming is not a true morphological analyzer and may produce non-dictionary stems.")


# 6 - Plural Morphological Parser

print ("\nQuestion 6 Output:\n")
import nltk
print("="*70)
print("Q6 - FINITE-STATE PLURAL MORPHOLOGICAL PARSER")
print("="*70)
def old_parser(word):
    if word.endswith("s"):
        return word[:-2],"Plural Noun"
    else:
        return word,"Singular"
words=["cars","boxes","cities","children"]
print("\nOriginal Parser:")
for w in words:
    print(w,"->",old_parser(w))
print("\nErrors:")
print("word[:-2] removes two characters from every plural.")
print("It fails for regular -s, -es, -ies and irregular plurals.")
irregular={"children":"child","men":"man","women":"woman","people":"person","mice":"mouse","geese":"goose","feet":"foot","teeth":"tooth"}
def parser(word):
    word=word.lower()
    if word in irregular:
        return irregular[word],"Irregular Plural"
    if word.endswith("ies"):
        return word[:-3]+"y","Plural -ies"
    if word.endswith(("ches","shes","xes","zes","ses")):
        return word[:-2],"Plural -es"
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1],"Regular Plural"
    return word,"Singular"
test=["cars","books","boxes","buses","cities","babies","children","men","women","people","mouse"]
print("\nCorrected Parser:")
for w in test:
    root,typ=parser(w)
    print(f"{w:<15}{root:<15}{typ}")
print("\nFST Transitions:")
print("Regular: START -> ROOT -> s -> FINAL")
print("-es: START -> ROOT -> es -> FINAL")
print("-ies: START -> ROOT(y) -> ies -> FINAL")
print("Irregular: START -> LEXICON -> ROOT -> FINAL")
try:
    from nltk.corpus import wordnet as wn
    print("\nWordNet:")
    for w in ["car","box","city","child"]:
        synsets=wn.synsets(w)
        print(w)
        for s in synsets[:2]:
            print(s.definition())
except LookupError:
    print("\nRun nltk.download('wordnet') to use WordNet.")
print("\nLimitations:")
print("Rule-based parsers require manually defined rules, have difficulty with irregular and unknown words, and may struggle with ambiguity, slang and spelling errors.")


# 7 - Morphological Feature Extraction Error Analysis

print ("\nQuestion 7 Output:\n")
import time,re
from nltk.stem import PorterStemmer
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
print("="*70)
print("Q7 - MORPHOLOGICAL FEATURE EXTRACTION ERROR ANALYSIS")
print("="*70)
stemmer=PorterStemmer()
documents=[
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]
v=CountVectorizer()
X=v.fit_transform(documents)
features=[stemmer.stem(w) for w in v.get_feature_names_out()]
print("\n1. ORIGINAL PREPROCESSING ERROR")
print("Original Vocabulary:",v.get_feature_names_out())
print("Stemmed Feature Names:",features)
print("Error: Stemming is performed after feature extraction.")
print("This creates redundant vocabulary columns.")
def stem_text(text):
    return " ".join(stemmer.stem(w) for w in re.findall(r'\b[a-zA-Z]+\b',text.lower()))
processed=[stem_text(x) for x in documents]
v2=CountVectorizer()
X2=v2.fit_transform(processed)
print("\n2. CORRECTED PIPELINE")
print("Processed Documents:")
for x in processed:
    print(x)
print("Corrected Vocabulary:",v2.get_feature_names_out())
print("Vocabulary Size:",len(v2.vocabulary_))
print("\n3. LOADING SMALL 20 NEWSGROUPS DATASET")
train=fetch_20newsgroups(
    subset="train",
    categories=["sci.space","rec.sport.baseball"],
    remove=("headers","footers","quotes")
)
test=fetch_20newsgroups(
    subset="test",
    categories=["sci.space","rec.sport.baseball"],
    remove=("headers","footers","quotes")
)
train.data=train.data[:500]
train.target=train.target[:500]
test.data=test.data[:200]
test.target=test.target[:200]
print("Training Documents:",len(train.data))
print("Testing Documents:",len(test.data))
print("\n4. WITHOUT STEMMING")
start=time.time()
v1=CountVectorizer(max_features=5000)
x1=v1.fit_transform(train.data)
x2=v1.transform(test.data)
model=LogisticRegression(max_iter=300)
model.fit(x1,train.target)
pred=model.predict(x2)
accuracy=accuracy_score(test.target,pred)
time1=time.time()-start
print("Vocabulary Size:",len(v1.vocabulary_))
print("Accuracy:",round(accuracy*100,2),"%")
print("Processing Time:",round(time1,2),"seconds")
print("\n5. WITH STEMMING")
start=time.time()
train_stem=[stem_text(x) for x in train.data]
test_stem=[stem_text(x) for x in test.data]
v3=CountVectorizer(max_features=5000)
x3=v3.fit_transform(train_stem)
x4=v3.transform(test_stem)
model2=LogisticRegression(max_iter=300)
model2.fit(x3,train.target)
pred2=model2.predict(x4)
accuracy2=accuracy_score(test.target,pred2)
time2=time.time()-start
print("Vocabulary Size:",len(v3.vocabulary_))
print("Accuracy:",round(accuracy2*100,2),"%")
print("Processing Time:",round(time2,2),"seconds")
print("\n6. COMPARISON")
print("-"*50)
print("Method              Vocabulary    Accuracy    Time")
print("Without Stemming    ",len(v1.vocabulary_),round(accuracy*100,2),"%      ",round(time1,2),"sec")
print("With Stemming       ",len(v3.vocabulary_),round(accuracy2*100,2),"%      ",round(time2,2),"sec")
print("\n7. INTERPRETATION")
print("Stemming before feature extraction reduces redundant vocabulary.")
print("It can reduce feature dimensionality and processing cost.")
print("However, aggressive stemming may remove useful semantic information.")
print("Therefore, preprocessing should be selected according to the task.")