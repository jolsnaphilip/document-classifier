import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training data
documents = [
    "I love this product",
    "This phone is amazing",
    "Excellent quality",
    "Highly recommended",
    "Very good",
    "Fantastic purchase",
    "Worst purchase ever",
    "I hate this item",
    "Terrible experience",
    "Waste of money",
    "Don't buy this product",
    "Very bad quality",
    "Not worth it",
    "Poor performance",
    "Awful product"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

# Train model
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(documents, labels)

# UI
st.title("Document Classifier")

text = st.text_area("Enter text")

if st.button("Classify"):
    prediction = model.predict([text])
    st.success(f"Prediction: {prediction[0]}")