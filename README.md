# ❤️ Heart Stroke Prediction App

A Machine Learning-based web application built with **Python**, **Scikit-learn**, and **Streamlit** to predict heart stroke risk using patient clinical parameters. The application offers a simple and interactive interface for entering health information and receiving instant predictions.

---

## 📌 Overview

This project leverages Machine Learning techniques to analyze patient health data and predict the likelihood of heart stroke. It demonstrates the complete ML workflow, including data preprocessing, model training, serialization, and deployment using Streamlit.

---

## ✨ Features

- Interactive Streamlit web application
- Real-time prediction
- Easy-to-use user interface
- Data preprocessing using a saved scaler
- Pre-trained Machine Learning model
- Fast and lightweight deployment

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
Heart-Stroke-Prediction-App/
│
├── DATA/
│   └── heart.csv
│
├── Frontend/
│   ├── app.py
│   ├── heart_disease_model.pkl
│   ├── scaler.pkl
│   ├── columns.pkl
│
├── NOTEBOOK/
│   └── ANALYSIS.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Anmol20Sharma/Heart-Stroke-Prediction-App.git
```

### Move to the project folder

```bash
cd Heart-Stroke-Prediction-App
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run Frontend/app.py
```

---

## 📊 Input Parameters

The model uses the following clinical parameters:

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

---

## 📈 Output

The application predicts whether a patient is at higher or lower risk based on the entered health parameters.

---

## 🖥️ Application Preview

<img src="images/app.png" width="700">

> Save your application screenshot inside an **images** folder as **image.png**.

---

## 🔮 Future Enhancements

- Improve prediction accuracy
- Compare multiple Machine Learning algorithms
- Add probability/confidence score
- Deploy on Streamlit Community Cloud
- Improve UI/UX
- Add data visualization dashboard

---

## 👩‍💻 Author

**Anmol Sharma**

B.Tech – Artificial Intelligence & Machine Learning

PSIT Kanpur

GitHub: https://github.com/Anmol20Sharma

LinkedIn: https://www.linkedin.com/in/anmol-sharma/

---

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub.
