# 16.Implement a Python program using the SpaCy library to perform Named Entity Recognition (NER) on a given text.

# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Elon Musk founded SpaceX in California."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, "->", ent.label_)