# 📝 Sentiment Analysis on Amazon Product Reviews

This project utilizes **Natural Language Processing (NLP)** and **Machine Learning** to analyze customer reviews from Amazon and classify them as **positive**, **negative**, or **neutral**.

It offers two front-end interfaces for interacting with the sentiment prediction system:

- **Streamlit App**: A Streamlit app for quick prototyping and user-friendly interaction.
- **Flask Web App**: A Flask web app for more customizable web deployment.

The system uses a trained machine learning model (pickled) and includes a Jupyter Notebook that handles data preprocessing, feature extraction, model training, and evaluation.


---

## 🚀 Features

- 🧹 **Text Preprocessing**: Lowercasing, stopword removal, and stemming.  
- 🔍 **Feature Extraction**: Text-to-vector conversion using **TF-IDF vectorization**.  
- 🤖 **Sentiment Classification**: Trained using a supervised ML algorithm (e.g., Naive Bayes or Logistic Regression).  
- 🧠 **Model Persistence**: Pickled `.p` model file enables reuse without retraining.  
- 🌐 **Dual Interface**:  
  - **Streamlit**: Lightweight and interactive front end for sentiment testing. 
  - **Flask**: Web backend with form-based input and sentiment response.

---

## 🗂️ Project Structure
```
Sentiment Analysis/
├── Amazon_Product_Sentiment Analysis.ipynb   # Jupyter notebook with training & evaluation
├── app.py                                    # Streamlit app
├── flask_app.py                              # Flask app
├── sentiment_model.p                         # Pickled trained model
├── requirements.txt                          # Python dependencies
├── README.md                                 # Project documentation
├── .gitignore
└── .git/                                     # Git metadata (if version controlled)
```

---

## ⚙️ Setup Instructions

1. **🔄 Clone the Repository**

   ```bash
    git clone https://github.com/helipatel12/Sentiment-Analysis.git
    cd Sentiment-Analysis
    ```

2. **🧪 Create and Activate Virtual Environment (Recommended):**
    ```bash
        python -m venv env
        source env/bin/activate          # On Windows: env\\Scripts\\activate
    ```

3. **📦 Install Required Python Packages:**
    ```bash
        pip install -r requirements.txt
    ```

4. **🚀 Run the Apps:**
▶️ To launch the Streamlit App:
    ```bash
        streamlit run app.py
    ```
This will open a browser window where you can enter review text and get a sentiment prediction.

🌐 To launch the Flask App:
    ```bash
        python flask_app.py
    ```
Then go to http://127.0.0.1:5000/ in your browser.

---

## **📊 Model Training and Evaluation:**

To understand how the model is trained:

    + Open Amazon_Product_Sentiment Analysis.ipynb in Jupyter Notebook or Google Colab.
    + Follow steps for data cleaning, text vectorization, model training, and performance evaluation. 

You can retrain the model and update sentiment_model.p as needed.

---

## 💡 Example Use Case

Here are some example reviews and their corresponding sentiment outputs:

- **Input**: “This product is amazing! Highly recommended.”  
  **→ Output**: *Positive*

- **Input**: “The item was damaged and arrived late.”  
  **→ Output**: *Negative*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Heli Patel**  
🔗 [GitHub Profile](https://github.com/helipatel12)