import streamlit as st
from prediction import predict, processing

st.title("Healthcare Premium Prediction")
st.subheader("Enter Customer Details")

# -------- Row 1 --------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=0, max_value=100, step=1)

with col2:
    number_of_dependants = st.number_input(
        "Number of Dependants", min_value=0, max_value=20, step=1
    )

with col3:
    income_lakhs = st.number_input(
        "Annual Income (Lakhs)", min_value=1.0, max_value=200.0, step=0.5
    )

# -------- Row 2 --------
col4, col5, col6 = st.columns(3)

with col4:
    Genitical_risk = st.number_input("Genitical risk",  min_value=0, max_value=5, step=1)

with col5:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
    

with col6:
    gender = st.selectbox("Gender", ['Male', 'Female'])
    

# -------- Row 3 --------
col7, col8, col9 = st.columns(3)

with col7:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
    

with col8:
    region = st.selectbox(
        "Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest']
    )
    

with col9:
    bmi_category = st.selectbox(
        "BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight']
    )
    

# -------- Row 4 --------
col10, col11, col12 = st.columns(3)

with col10:
    smoking_status = st.selectbox(
        "Smoking Status", ['No Smoking', 'Regular', 'Occasional']
    )
    

with col11:
    employment_status = st.selectbox(
        "Employment Status", ['Salaried', 'Self-Employed', 'Freelancer']
    )
    

with col12:
    medical_history = st.selectbox(
        "Medical History",
        [
            'No Disease',
            'Diabetes',
            'High blood pressure',
            'Thyroid',
            'Heart disease',
            'Diabetes & High blood pressure',
            'Diabetes & Thyroid',
            'Diabetes & Heart disease',
            'High blood pressure & Heart disease'
        ]
    )


# -------- Collect input --------
input_data = {
    'age': age,
    'number_of_dependants': number_of_dependants,
    'income_lakhs': income_lakhs,
    'Genitical_risk': Genitical_risk,
    'insurance_plan': insurance_plan,
    'gender': gender,
    'marital_status': marital_status,
    'region': region,
    'bmi_category': bmi_category,
    'smoking_status': smoking_status,
    'employment_status': employment_status,
    'medical_history': medical_history
}


if st.button("🔮 Predict Premium"):
    p = predict(input_data)
    st.success(f'Prediction value: {p}')
    

