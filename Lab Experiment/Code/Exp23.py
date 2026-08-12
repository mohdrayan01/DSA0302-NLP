# 23.Develop a python program that evaluates the coherence of a given text.

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
text = """
Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand human language.
NLP is used in chatbots, translation, and speech recognition.
"""
sentences = sent_tokenize(text)
print("Number of Sentences:", len(sentences))
total_words = 0
for sentence in sentences:
    words = word_tokenize(sentence)
    total_words += len(words)
average = total_words / len(sentences)
print("Average words per sentence:", round(average, 2))
if average >= 5:
    print("Text appears coherent.")
else:
    print("Text may not be coherent.")