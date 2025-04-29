from flask import Flask, request, jsonify, render_template
import json
import pickle

# Load the saved model and vectorizer
model_data = pickle.load(open("sentiment_model.p", "rb"))
vectorizer = model_data["vectorizer"]
model = model_data["logreg"]

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["text"]
    
    # Transform input text
    transformed_text = vectorizer.transform([text])
    
    # Predict sentiment
    prediction = model.predict(transformed_text)[0]
    
    # Map prediction to sentiment with emoji
    sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"

    # Use json.dumps with ensure_ascii=False
    response = json.dumps({"Sentiment": sentiment}, ensure_ascii=False)
    
    return response, 200, {"Content-Type": "application/json; charset=utf-8"}

if __name__ == "__main__":
    app.run(debug=True)
