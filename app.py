import streamlit as st
import pickle
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Stemming using Porter Stemmer
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    # Joining the cleaned words back into a string
    cleaned_text = ' '.join(words)

    return cleaned_text

vectorizer = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



st.title("Email Spam Detecter")
input_msg = st.text_input("Enter message")

if st.button("Predict"):

# Preprocess
    transform_mail = preprocess_text(input_msg)
    # Vectorize
    vector_input = vectorizer.transform([transform_mail])
    # Predict
    result = -1
    if hasattr(model, 'classes_'):

         result = model.predict(vector_input)[0]

    else:
         st.warning("Model is not fitted!!")



    if result == 1:
           st.header("Spam")
    else:
          st.header("non-spam")