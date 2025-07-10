import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model and encoder
with open('model.pkl', 'rb') as f:
    model, encoder = pickle.load(f)

# Load dataset for stats
df = pd.read_csv('data/salaries.csv')

# Rename columns to match training
df = df.rename(columns={
    'PAST EXP': 'YearsExperience',
    'DESIGNATION': 'Department',
    'SALARY': 'Salary',
    'RATINGS': 'Ratings'
})

# Add mock columns again (same as training)
np.random.seed(42)
companies = ['TCS', 'Infosys', 'Microsoft', 'Google', 'Amazon', 'Accenture', 'Wipro', 'IBM']
locations = ['Bangalore', 'Mumbai', 'Pune', 'Hyderabad', 'Delhi', 'Chennai', 'Remote', 'USA']
education_levels = ["Bachelor's", "Master's", "PhD"]
job_levels = ['Junior', 'Mid', 'Senior']
modes = ['Remote', 'Onsite', 'Hybrid']

df['Company Name'] = np.random.choice(companies, size=len(df))
df['Location'] = np.random.choice(locations, size=len(df))
df['Education Level'] = np.random.choice(education_levels, size=len(df), p=[0.6, 0.3, 0.1])
df['Job Level'] = np.random.choice(job_levels, size=len(df), p=[0.5, 0.3, 0.2])
df['Work Mode'] = np.random.choice(modes, size=len(df))
df['Years in Company'] = np.round(np.random.uniform(0.5, 10.0, size=len(df)), 1)
df['Company Rating'] = np.round(np.random.uniform(2.5, 5.0, size=len(df)), 1)

# Set up Streamlit app
st.set_page_config(page_title="💰 Salary Predictor", layout="centered")
st.title("💼 Salary Prediction App")
st.markdown("### Know your worth. Get data-driven salary insights in seconds.")
st.write("Predict your salary based on your department, experience, company, and more!")

# Inputs
years_exp = st.slider("Years of Experience", 0.0, 40.0, 2.0, 0.5)
department = st.selectbox("Department", sorted(df['Department'].unique()))
rating = st.slider("Performance Rating", 1.0, 5.0, 3.5, 0.1)
company = st.selectbox("Company", sorted(df['Company Name'].unique()))
location = st.selectbox("Location", sorted(df['Location'].unique()))
education = st.selectbox("Education Level", sorted(df['Education Level'].unique()))
job_level = st.selectbox("Job Level", sorted(df['Job Level'].unique()))
work_mode = st.selectbox("Work Mode", sorted(df['Work Mode'].unique()))
years_in_company = st.slider("Years in Current Company", 0.0, 15.0, 2.0, 0.5)
company_rating = st.slider("Company Rating", 2.5, 5.0, 4.0, 0.1)

# Prediction
if st.button("🚀 Predict Salary"):
    input_data = pd.DataFrame([{
        'YearsExperience': years_exp,
        'Department': department,
        'Ratings': rating,
        'Company Name': company,
        'Location': location,
        'Education Level': education,
        'Job Level': job_level,
        'Work Mode': work_mode,
        'Years in Company': years_in_company,
        'Company Rating': company_rating
    }])

    # Encode categorical features
    X_cat = encoder.transform(input_data[['Department', 'Company Name', 'Location',
                                          'Education Level', 'Job Level', 'Work Mode']])
    X_num = input_data[['YearsExperience', 'Ratings', 'Years in Company', 'Company Rating']].values
    X_final = np.concatenate([X_num, X_cat], axis=1)

    # Predict
    predicted_salary = model.predict([X_final[0]])[0]
    st.success(f"🎯 Predicted Salary: ₹{predicted_salary:,.2f}")

    # Show stats for selected department
    dept_data = df[df['Department'] == department]
    avg_salary = dept_data['Salary'].mean()
    min_salary = dept_data['Salary'].min()
    max_salary = dept_data['Salary'].max()

    st.write(f"**📊 Department Stats – {department}**")
    st.write(f"- Average Salary: ₹{avg_salary:,.2f}")
    st.write(f"- Min Salary: ₹{min_salary:,.2f}")
    st.write(f"- Max Salary: ₹{max_salary:,.2f}")

    # Comparison
    percentile = (dept_data['Salary'] < predicted_salary).mean() * 100
    st.info(f"📈 Your predicted salary is in the **top {percentile:.1f}%** of this department.")

    # Horizontal bar chart to compare salaries
    st.subheader("📊 Salary Comparison Chart")

    salary_labels = ['Minimum', 'Average', 'Maximum', 'Your Prediction']
    salary_values = [min_salary, avg_salary, max_salary, predicted_salary]

    fig, ax = plt.subplots()
    colors = ['gray', 'blue', 'green', 'orange']
    ax.barh(salary_labels, salary_values, color=colors)
    ax.set_xlabel("Salary")
    for index, value in enumerate(salary_values):
        ax.text(value + 5000, index, f"₹{value:,.0f}", va='center')

    st.pyplot(fig)

    st.markdown("---")
    st.caption("Made with ❤️ by Darshna Ujwal | Powered by Random Forests 🌲")