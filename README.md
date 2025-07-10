# 💼 AI-Powered Salary Predictor

An interactive and intelligent web application to **predict salaries** for professionals based on key career attributes like experience, role, company, education level, work mode, and more — built using **Ensemble Learning (Random Forest)** and **Streamlit**.

---

## 🚀 Features

- 📈 **Predict salary** based on realistic professional inputs  
- 🔢 Uses **Random Forest Regressor**, a powerful ensemble model  
- 📊 **Visual salary comparison** across departments  
- 📌 Shows **average, minimum, and maximum salaries** for a given role  
- 🏆 Tells users where they stand: *“You’re in the top 25%!”*  
- 🌐 Clean and responsive GUI built using **Streamlit**  

---

## 🧠 Problem Statement

> Help professionals and job-seekers make better career decisions by accurately predicting their expected salary using machine learning and visual analytics, based on multiple real-world job attributes.

---

## 📂 Dataset Description

The dataset (adapted & enhanced) contains the following columns:

| Column Name        | Description                          |
|--------------------|--------------------------------------|
| PAST EXP           | Years of professional experience     |
| DESIGNATION        | Job role or department               |
| SALARY             | Current salary in ₹                  |
| RATINGS            | Performance or appraisal ratings     |
| Company Name       | Mocked company names (TCS, Google…)  |
| Location           | Office location                      |
| Education Level    | Highest qualification                |
| Job Level          | Junior / Mid / Senior                |
| Work Mode          | Remote / Onsite / Hybrid             |
| Years in Company   | Time spent in current company        |
| Company Rating     | Employer's rating out of 5           |

---

## 🧼 Data Preprocessing

1. Renamed and selected relevant columns  
2. Cleaned missing or invalid data  
3. Added mock company info, job level, education, etc.  
4. Converted numerical columns to appropriate types  
5. Removed outliers (e.g., negative salary or ratings)  
6. Encoded categorical features using `OneHotEncoder`

---

## 🤖 Model Details

- **Model Type:** `RandomForestRegressor`  
- **Library:** `scikit-learn`  
- **Training/Test Split:** 80/20  
- **Evaluation Metric:** R² Score  
- **Train Score:** ~0.99 
- **Test Score:** ~0.96  
---

## 💻 App Functionality

The GUI is developed using `Streamlit`. Users can:

- Input:
  - Years of experience
  - Job designation
  - Education level
  - Job level
  - Work mode
  - Company & location
  - Ratings and more
- Get:
  - 📊 Predicted salary in ₹
  - 📉 Average, min, max salary for the role
  - 🥇 Percentile position of their salary
  - 📊 Horizontal bar chart comparing their salary with department-wide stats

---

## 📦 Installation & Usage

1. **Clone the Repository**

   Clone the project to your local machine using:

   ```bash
   git clone https://github.com/your-username/salary-prediction-app.git
   cd salary-prediction-app

2. **Install required dependencies**
  Make sure you have Python installed (preferably Python 3.9+), then install the necessary libraries:
  pip install streamlit pandas numpy scikit-learn

3. **Run the Streamlit Application**
  Launch the app using:
  streamlit run app.py

