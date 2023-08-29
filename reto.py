
import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import plotly.express as px

# escarga el archivo: Employees.csv y guarda, en un dataframe (employees), para evitar tráfico innecesario construir una función principal donde recuperen n datos (500 por default) para la etapa de pruebas y desarrollo, NOTA: usar el atributo cache


DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    return employees   

data_load_state = st.text('Loading data...')
employees = load_data(500) #para 500 datos
data_load_state.text('Done ! using cache...')

st.dataframe(employees)






