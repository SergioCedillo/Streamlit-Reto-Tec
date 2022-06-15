import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="", page_icon=":robot_face:") #El código que permita desplegar el logotipo de la empresa en la aplicación web.
st.subheader("Análisis del desempeño de los colaboradores de Socialize your Knowledge")
# El código que contenga las instrucciones para el despliegue de un título y una breve descripción de la aplicación web.

def load_data():
    data = pd.read_csv(
        "employee_data.csv", 
        header = 0,  
        parse_dates=[
            "birth_date"
        ],  
    )

    return data


data = load_data()
gender_selected_string=''
selected_gender = st.radio("Select Gender", data['gender'].unique()) #El código que permita desplegar un control para seleccionar el género del empleado.
st.write("Selected Gender:", selected_gender)

if (selected_gender.__contains__('M')):
    
   gender_selected_string = 'Male Employees'

else:
   gender_selected_string = 'Female Employees'

gender_data = data[(data["gender"] == selected_gender)] #El código que permita desplegar un control para seleccionar un rango del puntaje de desempeño del empleado.
optionals = st.expander("Select Performance Score Range: ", True)
range_select = optionals.slider("Select Range: ", min_value=int(gender_data['performance_score'].min()),max_value=int(gender_data['performance_score'].max())) 
subset_scores = gender_data[(gender_data['performance_score']>=range_select)]


gender_subset_data= gender_data[(gender_data['performance_score']>=range_select)]

selected_marital = st.radio("Select Marital Status", data['marital_status'].unique()) #El código que permita desplegar un control para seleccionar el estado civil del empleado.
st.write("Selected Marital Status:", selected_marital)



gsm_data = gender_subset_data[(gender_subset_data['marital_status']==selected_marital)]
st.write(f"Number of {selected_marital} {gender_selected_string} With this Score of {range_select} or more:  {gsm_data.shape[0]}")
gsm_data

#El código que permita mostrar un gráfico en donde se visualice la distribución de los puntajes de desempeño.
st.write("Performance Score Distribution")
source=pd.DataFrame({
    'Name': gsm_data["name_employee"],
    'Score': gsm_data["performance_score"]
})

st.altair_chart(alt.Chart(source).mark_bar().encode(
    x='Name',
    y='Score'
))
#El código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado.




average_male_hours=sum(data[data["gender"] == 'M ']['average_work_hours'])/data[data["gender"] == 'M ']['average_work_hours'].shape[0]
average_female_hours=sum(data[data["gender"] == 'F']['average_work_hours'])/data[data["gender"] == 'F']['average_work_hours'].shape[0]
st.write("Average Work Hours By Gender")
source_hours=pd.DataFrame({
    'Average Work Hours': [average_male_hours,average_female_hours],
    'Gender': ["Male", "Female"]
})

st.altair_chart(alt.Chart(source_hours).mark_bar().encode(
    x='Average Work Hours',
    y='Gender'
))
#El código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de estos.
age_arr= data['age']
salary_arr = data['salary']
st.write("Age Vs Salary")
source_hours=pd.DataFrame({
    'Salary': salary_arr,
    'Age': age_arr
})

st.altair_chart(alt.Chart(source_hours).mark_point(filled=True).encode(
    alt.X('Age'),
    alt.Y('Salary'),
    alt.Size('Salary'),
    alt.Color('Age'),
    alt.OpacityValue(0.7)
))
#El código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
work_hours_arr= data['average_work_hours']
performance_arr = data['performance_score']
st.write("Average Work Hours Vs Performance Score")
source_performance=pd.DataFrame({
    'Average Work Hours': work_hours_arr,
    'Performance Score': performance_arr,
    'Salary': salary_arr,
    'Age': age_arr,
})

st.altair_chart(alt.Chart(source_performance).mark_point(filled=True).encode(
    alt.Y('Average Work Hours'),
    alt.X('Performance Score'),
    alt.Size('Salary'),
    alt.Color('Age'),
    alt.OpacityValue(0.7)
))
#El código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web.
"CONCLUSION:"
"Streamlit me parece una herramienta muy flexible que reduce la redudndancia con la que un desarollador de frontend se puede llgar a topar al utilizar otras herramientas de diseno de interfaces como REact o Angular"
"Me parece ques es una herramienta muy facil de usar ya que te permite el dataframe de Pandas y programar con python."