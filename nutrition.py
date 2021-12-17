import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

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



gender_count = data.groupby(["Gender"]).count()

status_group = data.groupby(["Weight Status", "Gender"]).count()

data_male = data.loc[data['Gender']=='Male']
data_female = data.loc[data['Gender']=='Female']

status_group_male = data_male.groupby(["Weight Status"]).count()

status_count_male = [status_group_male["Gender"]]

status_values = np.array(status_count_male)

list1 = status_values.tolist()
status_value_list = []
for x in list1[0]:
    status_value_list.append(x)


# pie chart
labels = ["Healthy", "Obese", "Overweight", "Underweight"]
fig1, ax1 = plt.subplots()
ax1.pie(status_value_list, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')
st.write('Weight Status of members')
st.pyplot(fig1)




status_group_female = data_female.groupby(["Weight Status"]).count()
status_count_female = [status_group_female["Gender"]]
status_values_female = np.array(status_count_female)
list_fem = status_values_female.tolist()
status_value_list_fem = []
for x in list_fem[0]:
    status_value_list_fem.append(x)

labels = ["Healthy", "Obese", "Overweight", "Underweight"]
fig2, ax2 = plt.subplots()
ax2.pie(status_value_list_fem, labels=labels, autopct='%1.1f%%')
st.write('Female Weight Status')
st.pyplot(fig2)



