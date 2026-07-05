from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training data
documents = [
    "I love this product",
    "This phone is amazing",
    "Worst purchase ever",
    "I hate this item",
    "Excellent quality",
    "Terrible experience"
]

labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Positive",
    "Negative"
]

# Create and train the classifier
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(documents, labels)

# Test the classifier
test_document = ["The product is fantastic"]

prediction = model.predict(test_document)

print("Prediction:", prediction[0])