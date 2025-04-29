import streamlit as st
import pickle

# Load the dictionary
with open("sentiment_model.p", "rb") as file:
    data = pickle.load(file)

# Correctly extract
vectorizer = data['vectorizer']
classifier = data['logreg']


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

        # Display raw prediction and classifier classes
        st.write(f"Predicted output: {prediction}")

        # Use string comparison for sentiment labels
        if prediction == "Positive":
            st.success("😊 Positive sentiment detected!")
        elif prediction == "Negative":
            st.error("😞 Negative sentiment detected!")
        else:
            st.warning("😐 Neutral sentiment detected!")