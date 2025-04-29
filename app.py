import streamlit as st
import pickle

# Load the dictionary
with open("sentiment_model.p", "rb") as file:
    data = pickle.load(file)

# Correctly extract
vectorizer = data['vectorizer']
classifier = data['logreg']

# Mapping function
def get_sentiment_label(pred):
    if pred == 0:
        return "Negative 😠"
    elif pred == 1:
        return "Neutral 😐"
    else:
        return "Positive 😊"

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis", layout="centered")
st.title("🧠 Sentiment Analysis App")
st.write("Enter your text below:")

user_input = st.text_area("Enter Text Here", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        transformed_input = vectorizer.transform([user_input])
        prediction = classifier.predict(transformed_input)[0]
        sentiment = get_sentiment_label(prediction)
        st.success(f"🎯 Sentiment: **{sentiment}**")
