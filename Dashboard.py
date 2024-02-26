import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

st.title('Siniestros Viales')

# Carga los conjuntos de datos
lesiones_df = pd.read_csv('data/lesiones.csv')
homicidios_df = pd.read_csv('data/homicidios.csv')

# Convierte las columnas 'latitud' y 'longitud' a números
homicidios_df['latitud'] = pd.to_numeric(homicidios_df['latitud'], errors='coerce')
homicidios_df['longitud'] = pd.to_numeric(homicidios_df['longitud'], errors='coerce')

# Elimina las filas con valores NaN en 'latitud' y 'longitud'
homicidios_df = homicidios_df.dropna(subset=['latitud', 'longitud'])


# Crea una barra lateral con un botón para seleccionar el conjunto de datos
dataset = st.selectbox(
    'Selecciona un conjunto de datos',
    ('Lesiones', 'Homicidios')
)

# Muestra el conjunto de datos seleccionado
if dataset == 'Lesiones':
    st.markdown('***')
    st.markdown('### Lesiones')
    st.markdown('#### Mapa de siniestros viales no fatales')
    # Crea un mapa centrado en una ubicación inicial
    mapa = folium.Map(location=[lesiones_df['latitud'].mean(), lesiones_df['longitud'].mean()], zoom_start=13)

    # Crea un grupo de marcadores
    marker_cluster = MarkerCluster().add_to(mapa)

    # Añade un marcador para cada punto al grupo de marcadores
    for idx, row in lesiones_df.iterrows():
        folium.Marker(location=[row['latitud'], row['longitud']]).add_to(marker_cluster)

    # Muestra el mapa
    folium_static(mapa)
    
else:
    st.markdown('***')
    st.markdown('### Homicidios')
    st.markdown('#### Mapa de siniestros viales fatales')
    # Crea un mapa centrado en una ubicación inicial
    mapa = folium.Map(location=[homicidios_df['latitud'].mean(), homicidios_df['longitud'].mean()], zoom_start=13)

    # Crea un grupo de marcadores
    marker_cluster = MarkerCluster().add_to(mapa)

    # Añade un marcador para cada punto al grupo de marcadores
    for idx, row in homicidios_df.iterrows():
        folium.Marker(location=[row['latitud'], row['longitud']]).add_to(marker_cluster)

    # Muestra el mapa
    folium_static(mapa)
    st.markdown('***')