import streamlit as st
import pandas as pd

# Carga los conjuntos de datos
lesiones_df = pd.read_csv('data/lesiones.csv')
homicidios_df = pd.read_csv('data/homicidios.csv')

# Crea una barra lateral con un botón para seleccionar el conjunto de datos
dataset = st.selectbox(
    'Selecciona un conjunto de datos',
    ('Lesiones', 'Homicidios')
)

# Muestra el conjunto de datos seleccionado
if dataset == 'Lesiones':
    st.write(lesiones_df)
else:
    st.write(homicidios_df)
