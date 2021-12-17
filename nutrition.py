import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns

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
st.markdown('Weight Status of members')
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


#male dist graph
fig9 = plt.figure()
plt.legend(loc='lower right')
sns.distplot(data_male["BMI"])
st.write('Male BMI Distribution')
st.pyplot(fig9)

#female dist graph
fig10 = plt.figure()
plt.legend(loc='lower right')
sns.distplot(data_female["BMI"])
st.write('Female BMI distribution')
st.pyplot(fig10)


#scatter plot
healthy_ppl = data_male.loc[data_male["Weight Status"] == "Healthy"]
obese_ppl = data_male.loc[data_male["Weight Status"] == "Obese"]
fig3 = plt.figure()
sns.scatterplot(x="Height",y="Weight",data=data_male,size="BMI")
plt.legend(loc='lower right')
st.write('All BMIs distributed')
st.pyplot(fig3)


#scatter plot 2
fig4 = plt.figure()
sns.scatterplot(x="Height",y="Weight",data=obese_ppl,size="BMI")
plt.legend(loc='lower right')
st.write('Obese scatterplot')
st.pyplot(fig4)


#scatter plot 5
fig5 = plt.figure()
sns.scatterplot(x="Height",y="Weight",data=healthy_ppl,size="BMI")
plt.legend(loc='lower right')
st.write('Healthy people bmis')
st.pyplot(fig5)



# Female plots

healthy_ppl_fem = data_female.loc[data_female["Weight Status"] == "Healthy"]
obese_ppl_fem = data_female.loc[data_female["Weight Status"] == "Obese"]

#scatter plot 6
fig6 = plt.figure()
plt.legend(loc='lower right')
sns.scatterplot(x="Height",y="Weight",data=data_female,size="BMI")
st.pyplot(fig6)


#scatter plot 7
fig7 = plt.figure()
plt.legend(loc='lower right')
sns.scatterplot(x="Height",y="Weight",data=obese_ppl_fem,size="BMI")
st.pyplot(fig7)

#scatter plot 8
fig8 = plt.figure()
plt.legend(loc='lower right')
sns.scatterplot(x="Height",y="Weight",data=healthy_ppl_fem,size="BMI")
st.pyplot(fig8)






