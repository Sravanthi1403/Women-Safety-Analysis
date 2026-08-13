# Women Safety Analysis

A machine learning project for analyzing sentiment in Twitter data related to women's safety and the #MeToo movement.

## Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning techniques to analyze sentiment in Twitter data related to the #MeToo movement.

The main machine learning implementation is provided in **`SentimentAnalysisProject.ipynb`**. The notebook contains the complete workflow, including data exploration, text preprocessing, feature extraction, model training, evaluation, and visualization.

A Django-based web application is also included to provide a user interface for interacting with the sentiment analysis system.

## Main Notebook

### `SentimentAnalysisProject.ipynb`

**This is the main machine learning component of the project.**

The notebook demonstrates the complete sentiment analysis workflow:

- Loading and exploring the Twitter dataset
- Data cleaning and text preprocessing
- Stopword removal
- Stemming and lemmatization
- Feature extraction using TF-IDF
- Training machine learning models
- Sentiment prediction
- Model evaluation
- Accuracy, Precision, Recall and F1-Score evaluation
- Confusion matrix visualization
- Sentiment distribution analysis
- BiLSTM-based sentiment analysis

The notebook contains the main experimentation and analysis performed for the project and can be independently explored using Jupyter Notebook or Google Colab.

## Dataset

The project uses a Twitter dataset related to the **#MeToo movement** for sentiment analysis.

The dataset contains tweet-related information such as:

- Tweet text
- Tweet ID
- Tweet length
- Creation date
- Source
- Favorite count
- Retweet count
- Language

The raw dataset is not included in this repository. It can be obtained from the original public dataset source and loaded into the notebook for reproducing the analysis.

## Machine Learning

The project explores both traditional machine learning and deep learning approaches for sentiment classification.

### Machine Learning Models

- Multinomial Naive Bayes
- Decision Tree
- Random Forest
- BiLSTM

### Feature Extraction

For traditional machine learning models, **TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert text data into numerical features.

The project also uses a **BiLSTM (Bidirectional Long Short-Term Memory)** model for deep learning-based sentiment classification.

## Model Evaluation

The models are evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The notebook also contains visualizations for analyzing model performance and sentiment distribution.

## Web Application

A Django-based web application is included as the application layer of the project.

### Features

- User registration and login
- Sentiment prediction interface
- Sentiment analysis results
- Analytics and visualizations
- Integration with the trained sentiment analysis model

The application currently runs locally using the Django development server.

## Project Structure

```text
Women-Safety-Analysis/
│
├── analyzer/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── models/
│   ├── bilstm_model.h5
│   └── bilstm_tokenizer.pkl
│
├── sentiment_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── analytics.html
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── predict.html
│   └── register.html
│
├── SentimentAnalysisProject.ipynb
├── manage.py
├── .gitignore
└── README.md
```

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Deep Learning:** TensorFlow / Keras
- **NLP:** NLTK
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Feature Extraction:** TF-IDF
- **Web Framework:** Django
- **Database:** SQLite
- **Development Environment:** Jupyter Notebook / Google Colab
- **Version Control:** Git, GitHub

## How to Explore the Machine Learning Notebook

1. Clone or download this repository.
2. Open **`SentimentAnalysisProject.ipynb`** using Jupyter Notebook, JupyterLab, or Google Colab.
3. Obtain the dataset from its original source.
4. Load the dataset in the notebook environment.
5. Install the required Python libraries if necessary.
6. Run the notebook cells sequentially to reproduce the preprocessing, training, evaluation, and visualization workflow.

## How to Run the Django Application

1. Clone the repository.

2. Install the required Python dependencies.

3. Navigate to the project directory.

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the Django development server:

```bash
python manage.py runserver
```

6. Open the local application in a web browser.

## Project Purpose

The project demonstrates how Natural Language Processing, Machine Learning, and Deep Learning techniques can be applied to analyze sentiment in social media discussions related to women's safety and the #MeToo movement.

It combines a machine learning experimentation workflow with a Django-based interface for interacting with the sentiment analysis system.

## Note

This project is developed for educational and research purposes. Sentiment predictions represent model outputs and should not be considered definitive interpretations of individual users' opinions.
