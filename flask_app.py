import flask
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model and vectorizer
with open("sentiment_model.p", "rb") as file:
    data = pickle.load(file)

vectorizer = data['vectorizer']
classifier = data['logreg']

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    sentiment_message = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['text_input']
        if user_input.strip() == "":
            sentiment_message = "⚠️ Please enter some text."
        else:
            transformed_input = vectorizer.transform([user_input])
            prediction = classifier.predict(transformed_input)[0]

            # Determine sentiment label
            if prediction == "Positive":
                sentiment_message = "😊 Positive sentiment detected!"
            elif prediction == "Negative":
                sentiment_message = "😞 Negative sentiment detected!"
            else:
                sentiment_message = "😐 Neutral sentiment detected!"

    return render_template("index.html", prediction=prediction, sentiment_message=sentiment_message, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
