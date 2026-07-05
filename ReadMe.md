# Document Classifier

## What is this project?

This is a simple Machine Learning project that classifies a piece of text as **Positive** or **Negative**.

For example:

* "I love this product." → Positive
* "Worst product ever." → Negative

The model learns from example sentences and then predicts the category of new text entered by the user.

---

# Tools Used

* Python
* Scikit-learn
* Streamlit

---

# How does it work?

### Step 1: Create training data

First, I created a small dataset with positive and negative sentences.

Example:

* I love this product → Positive
* Excellent quality → Positive
* Worst purchase ever → Negative
* Terrible experience → Negative

---

### Step 2: Convert text into numbers

A computer cannot understand words directly.

So I used **TF-IDF Vectorizer**, which converts text into numbers that the machine learning model can understand.

---

### Step 3: Train the model

I used the **Multinomial Naive Bayes** algorithm.

The model learns patterns from the training data.

---

### Step 4: Predict new text

When a user enters a new sentence, the model predicts whether it is **Positive** or **Negative**.

Example:

Input:

```
I really like this phone.
```

Output:

```
Positive
```

---

# Project Files

* `app.py` – Streamlit application
* `document_classifier.py` – Python program for training the model
* `requirements.txt` – Required Python libraries
* `README.md` – Project explanation

---

# How to Run

1. Install the required libraries:

```
pip install -r requirements.txt
```

2. Run the application:

```
streamlit run app.py
```

3. Open the link shown in the terminal.

4. Type any sentence and click **Classify**.

---

# What I Learned

* What a document classifier is.
* How to train a machine learning model.
* How to convert text into numbers using TF-IDF.
* How to use the Naive Bayes algorithm.
* How to build a simple web app using Streamlit.
* How to upload a project to GitHub.

---

# Conclusion

This project helped me understand the basics of text classification using machine learning. It can be improved further by using a larger dataset and training the model with more examples.
