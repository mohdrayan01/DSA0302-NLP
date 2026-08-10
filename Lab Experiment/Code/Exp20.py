# 20.Implement a basic information retrieval system using TF-IDF (Term Frequency-Inverse Document Frequency) for document ranking using python.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Natural Language Processing is interesting.",
    "Machine Learning is a part of Artificial Intelligence.",
    "Python is widely used for NLP.",
    "Deep Learning improves NLP models."
]
query = ["Python for NLP"]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + query)
similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
scores = similarity.flatten()
for i, score in enumerate(scores):
    print(f"Document {i+1}: {score:.3f}")
best = scores.argmax()
print("\nMost Relevant Document:")
print(documents[best])