import pandas as pd
import streamlit as st
from joblib import load


model_rest = load('artifacts/model_rest.joblib')
model_young = load('artifacts/model_young.joblib')
scaler_rest = load('artifacts/scaler_rest.joblib')
scaler_young = load('artifacts/scaler_young.joblib')

def processing(input_dict):
    
    risk_scores = {
        'Diabetes': 6,
        'High blood pressure': 6,
        'No Disease': 0,
        'Thyroid': 5,
        'Heart disease': 8
    }
    def calculate_risk_score(medical_history):
        diseases = medical_history.split('&')
        return sum(risk_scores.get(d.strip(), 0) for d in diseases)
    
    # -----------------------------
    # NUMERICAL FEATURES
    # -----------------------------
    insurance_plan_map = {
        'Bronze': 1,
        'Silver': 2,
        'Gold': 3
    }
    
    data = {
        'age': input_dict['age'],
        'number_of_dependants': input_dict['number_of_dependants'],
        'income_lakhs': input_dict['income_lakhs'],
        'insurance_plan' : insurance_plan_map[input_dict['insurance_plan']],
        'genetical_risk': input_dict['Genitical_risk'],
        'total_risk_score_scaled': calculate_risk_score(input_dict['medical_history'])
    }
    

    # -----------------------------
    # ORDINAL ENCODING
    # -----------------------------
    
    data

    # -----------------------------
    # ONE-HOT ENCODING
    # -----------------------------
    one_hot_columns = [
        'gender_Male',
        'region_Northwest',
        'region_Southeast',
        'region_Southwest',
        'marital_status_Unmarried',
        'bmi_category_Obesity',
        'bmi_category_Overweight',
        'bmi_category_Underweight',
        'smoking_status_Occasional',
        'smoking_status_Regular',
        'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    # initialize all as 0
    for col in one_hot_columns:
        data[col] = 0

    # set 1 based on input
    if input_dict['gender'] == 'Male':
        data['gender_Male'] = 1

    if input_dict['region'] in ['Northwest', 'Southeast', 'Southwest']:
        data[f"region_{input_dict['region']}"] = 1

    if input_dict['marital_status'] == 'Unmarried':
        data['marital_status_Unmarried'] = 1

    if input_dict['bmi_category'] in ['Obesity', 'Overweight', 'Underweight']:
        data[f"bmi_category_{input_dict['bmi_category']}"] = 1

    if input_dict['smoking_status'] in ['Occasional', 'Regular']:
        data[f"smoking_status_{input_dict['smoking_status']}"] = 1

    if input_dict['employment_status'] in ['Salaried', 'Self-Employed']:
        data[f"employment_status_{input_dict['employment_status']}"] = 1

    # -----------------------------
    # CREATE DATAFRAME
    # -----------------------------
    df = pd.DataFrame([data])
    
    df = scaler(df)
    return df
    

def scaler(df):
    # extract scalar age
    age = df.loc[0, 'age']

    # choose scaler
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    scaler = scaler_object['scaler']
    scale_col = scaler_object['scale_col']

    # scale the actual columns
    df['income_level'] = 0
    df[scale_col] = scaler.transform(df[scale_col])
    df = df.drop(columns=['income_level'], errors='ignore')
    
    

    return df
            
def predict(input_dict):
    input_df = processing(input_dict)

    if input_dict['age']<=25:
        prediction = model_young.predict(input_df)
    
    else:
        prediction = model_rest.predict(input_df)
        
    return prediction
        
    
    
        