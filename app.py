import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('notebooks/vehicles_us.csv')  # leer la data
st.header('Venta de Coches')

# Histograma
# crear una casilla de verificación
hist_build = st.checkbox('Construir histograma')
if hist_build:  # al hacer check
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crea un histograma
    fig = px.histogram(car_data, x="odometer")
    # muestra un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
# crear una casilla de verificación
disp_build = st.checkbox('Construir dispersión')
if disp_build:  # al hacer check
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crea un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    # muestra un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
