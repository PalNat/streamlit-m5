import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import plotly.express as px

#Crear título de la aplicación, encabezados y texto de descripción del proyecto
# escarga el archivo: Employees.csv y guarda, en un dataframe (employees), para evitar tráfico innecesario construir una función principal donde recuperen n datos (500 por default) para la etapa de pruebas y desarrollo, NOTA: usar el atributo cache


DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(DATA_URL, nrows=nrows)
    return employees   

data_load_state = st.text('Loading data...')
employees = load_data(500) #para 500 datos
data_load_state.text('Done ! using cache...')



#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


st.title("Reto de apliacion")

st.header("Información sobre el Conjunto de Datos")

st.header("Descripción de los datos")
st.write("""
Esta aplicacion se crea un buscador de empleados y sus respectiovas ciudades

""")
   #crear sidebar y checkbox      
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")


st.sidebar.header('Opciones')
#elected_option = st.sidebar.radio('Seleccione una opción', ['Tabla de Datos'] )
show_dataframe = st.sidebar.checkbox('Mostrar DataFrame Completo', value=True)

# Sidebar con checkbox
st.sidebar.header('Opciones')



st.header('Tabla de Datos')
if show_dataframe:
    st.dataframe(employees)
else:
    st.write("Utiliza el checkbox para mostrar el DataFrame completo.")



#Crear un buscador de empleados con cajas de texto y botones de comando
def buscar_empleados(Employee_ID, Hometown, Unit):
    resultados = employees[(employees['Employee_ID'] == Employee_ID) |
                      (employees['Hometown'] == Hometown) |
                      (employees['Unit'] == Unit)]
    return resultados

Employee_ID = st.text_input('Employee_ID', '')
Hometown = st.text_input('Hometown', '')
Unit = st.text_input('Unit', '')

# Botón de búsqueda
if st.button('Buscar'):
    resultados = buscar_empleados(Employee_ID, Hometown, Unit)
    
    # Mostrar resultados encontrados
    st.subheader('Resultados Encontrados')
    st.dataframe(resultados)
    
    # Mostrar total de empleados encontrados
    total_encontrados = resultados.shape[0]
    st.write(f'Total de Empleados Encontrados: {total_encontrados}')



#--------------------------------------------------------------------
#crear selectedbox para nivel educativo y hometown

st.sidebar.header('Filtrar por Nivel Educativo')
nivel_educativo_options = employees['Education_Level'].unique()
selected_nivel_educativo = st.sidebar.selectbox('Selecciona un Nivel Educativo', nivel_educativo_options)

# Filtrar empleados por Nivel Educativo seleccionado
empleados_por_Education_Level = employees[employees['Education_Level'] == selected_nivel_educativo]

# Mostrar empleados por Nivel Educativo seleccionado en un dataframe
st.subheader(f'Empleados en {selected_nivel_educativo}')
st.dataframe(empleados_por_Education_Level)

# Mostrar total de empleados en Nivel Educativo seleccionado
total_empleados_Education_Level = empleados_por_Education_Level.shape[0]
st.write(f'Total de Empleados del nivel {selected_nivel_educativo}: {total_empleados_Education_Level}')  


# Sidebar con selectbox para filtrar por Hometown
st.sidebar.header('Filtrar por Ciudad')
hometown_options = employees['Hometown'].unique()
selected_hometown = st.sidebar.selectbox('Selecciona una Hometown', hometown_options)

empleados_por_hometown = employees[employees['Hometown'] == selected_hometown]
st.subheader(f'Empleados en {selected_hometown}')
st.dataframe(empleados_por_hometown)

# Mostrar total de empleados en Hometown seleccionada
total_empleados_hometown = empleados_por_hometown.shape[0]
st.write(f'Total de Empleados en {selected_hometown}: {total_empleados_hometown}')

# Sidebar con selectbox para filtrar por unidad
st.sidebar.header('Filtrar por unidad')
unit_options = employees['Unit'].unique()
selected_unit = st.sidebar.selectbox('Selecciona una unidad', unit_options)

empleados_por_unit = employees[employees['Unit'] == selected_unit]
st.subheader(f'Empleados en {selected_unit}')
st.dataframe(empleados_por_unit)

# Mostrar total de empleados en Hometown seleccionada
total_empleados_unit = empleados_por_unit.shape[0]
st.write(f'Total de Empleados en {selected_unit}: {total_empleados_unit}')


# Crear un histograma
st.header('Histograma de Empleados')
fig = px.histogram(employees, x='Age', nbins=20, title='Histograma de Edades')
st.plotly_chart(fig)

# Crear una gráfica de frecuencias 
st.header('Gráfica de Frecuencias por Unidad Funcional')
fig = px.histogram(employees, x='Unit', title='Frecuencia de Unidades Funcionales')
st.plotly_chart(fig)

# Calcular el índice de deserción por ciudad (Hometown)
desercion = employees.groupby('Hometown')['Attrition_rate'].mean().reset_index()

# Ordenar las ciudades por el índice de deserción de mayor a menor
desercion = desercion.sort_values(by='Attrition_rate', ascending=False)

# Crear una gráfica para observar el índice de deserción por ciudad
st.header('Índice de Deserción por Ciudad')
fig = px.bar(desercion, x='Hometown', y='Attrition_rate', title='Índice de Deserción por Ciudad')
fig.update_xaxes(categoryorder='total descending')  # Ordenar las ciudades de mayor a menor deserción
st.plotly_chart(fig)

