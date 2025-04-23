# ❤️ Heart Disease Prediction Web App

This is a simple and interactive web application for predicting the **risk of heart disease** using basic health-related input factors. The prediction is powered by a **Machine Learning model (Logistic Regression)** trained on a real-world dataset. The app is built using **Python**, **Flask**, **HTML/CSS**, and deployed locally.

---

## 🚀 Features

- 🩺 User-friendly interface to input key health indicators
- 🔍 Predicts 10-year risk of coronary heart disease
- 📊 Trained with Logistic Regression and accuracy around **85%**
- 🎨 Custom-designed background themed on heart health

---

## 🧠 Input Fields

The following user inputs are taken for prediction:

- Age
- Cigarettes per day
- Total Cholesterol (totChol)
- Systolic Blood Pressure (sysBP)
- Glucose Level

---

## 🔧 Technologies Used

- Python 3
- Scikit-learn
- Pandas, NumPy
- Flask (Web framework)
- HTML, CSS
- Git & GitHub

---

## 📁 Project Structure
train_model_code                   #code to train the model 
heart_disease_app/
├── static/
│   └── heart_bg.jpg               # Background image related to heart
│
├── templates/
│   └── index.html                 # HTML frontend form and results display
│
├── app.py                         # Main Flask application (connects model to web)
├── train_model.py                 # Trains Logistic Regression model, saves model & scaler
├── model.pkl                      # Saved machine learning model
├── scaler.pkl                     # Saved scaler (used for input normalization)
├── heart.csv                      # Dataset (Framingham Heart Study)
├── requirements.txt               # All Python packages used
└── README.md                      # Project documentation
