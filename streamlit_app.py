import streamlit as st
import pickle
import json
import numpy as np

# Load the saved model and vectorizer
model_data = pickle.load(open("sentiment_model.p", "rb"))
vectorizer = model_data["vectorizer"]
model = model_data["logreg"]

# Streamlit App UI
st.title("Sentiment Analysis App 😊😞")

st.write("Enter a sentence below to analyze its sentiment:")

# Input text box
text = st.text_area("Enter your text here", "")

if st.button("Analyze Sentiment"):
    if text.strip():
        # Transform input text
        transformed_text = vectorizer.transform([text])
        
        # Predict sentiment
        prediction = model.predict(transformed_text)[0]
        
        # Map prediction to sentiment with emoji
        sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"

        # Display result
        st.success(f"**Sentiment:** {sentiment}")

    else:
        st.warning("⚠️ Please enter some text to analyze.")
