# Sentiment Analysis Project

This project is a **Sentiment Analysis** application that classifies text data into categories such as positive, negative, or neutral. It leverages natural language processing (NLP) techniques and machine learning algorithms to predict the sentiment of input text.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Technologies](#technologies)
5. [License](#license)

## Installation

To install and run this project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git

2. **Navigate to the project directory:**

    ```bash
    cd sentiment-analysis

3. **Set up a virtual environment and install dependencies:**
    + For Python, create a virtual environment:
        ```bash
        python -m venv venv
        
    + Activate the virtual environment:
        ```bash
        source venv/bin/activate  # On Windows: venv\Scripts\activate
    
    + Install the required dependencies:
        ```bash
        pip install -r requirements.txt

4. If your project uses a specific dataset, make sure to place the dataset in the correct folder.



## Usage

After setting up the project, you can interact with the Sentiment Analysis system using either the **Flask web app** or the **Streamlit app**, depending on your preference.

### 🔹 Option 1: Run with Flask

1. Navigate to the project folder (if not already there):

   ```bash
   cd sentiment-analysis

2. Run the Flask application:

    ```bash
    python app.py

3. Open your browser and go to:

    ```cpp
    http://127.0.0.1:5000/
    
+ You’ll see a web interface where you can enter text, and the app will display the predicted sentiment.

### 🔹 Option 2: Run with Streamlit

1. Navigate to the project folder (if not already there):

   ```bash
   cd sentiment-analysis

2. Run the Streamlit application:

    ```bash
    streamlit run streamlit_app.py

3. Streamlit will automatically open in your default browser. If not, visit:

    ```cpp
    http://localhost:8501/
    
+ You can enter text in the input field and see real-time sentiment predictions with a clean UI.


## Features

+ Text Preprocessing: Includes tokenization, stopword removal, and lemmatization to clean and prepare the text for analysis.
+ Modeling: The sentiment analysis model is built using machine learning algorithms such as Logistic Regression or Naive Bayes.
+ Evaluation: The model is evaluated based on metrics like accuracy, precision, recall, and F1-score to determine its effectiveness.
+ Visualization: Generate plots to visualize sentiment distribution across different texts (optional feature).

## Technologies

This project is built using the following technologies:

+ Programming Language: Python

+ Libraries:
    + pandas for data handling  
    + scikit-learn for machine learning algorithms   
    + nltk for natural language processing 
    + matplotlib for data visualization (optional)

+ Tools:
    + Jupyter Notebook (for experimentation and exploration)
    + VSCode (Integrated Development Environment)

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details.
