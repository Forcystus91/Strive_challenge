import streamlit as st
import numpy as np
import pandas as pd

st.title('Nutrition Data')

data = pd.read_csv(r'C:\Users\Emilio\Documents\GitHub\Strive_challenge\data.csv')

# adding bmi and weight status columns to data
def bmi(weight,height):
    return round((weight/(height**2)*10000),1)

data['BMI'] = bmi(data['Weight'],data['Height'])
weight_status = []
for bmi in data['BMI']:
    if bmi < 18.5:
            weight_status.append('Underweight')
    elif 18.5<=bmi<=24.9:
        weight_status.append('Healthy')
    elif 25.0<=bmi<=29.9:
        weight_status.append('Overweight')
    else:
        weight_status.append('Obese')
data['Weight Status'] = weight_status


