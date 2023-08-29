import streamlit as st 
import pandas as pd 

st.title('Streamlit con cache')
DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    return employees   

data_load_state = st.text('Loading data...')
employees = load_data(500)
data_load_state.text('Done ! using cache...')

st.dataframe(employees)
