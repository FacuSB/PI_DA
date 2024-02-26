import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

    ###########################################################################################################################################################################################################
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

    ###########################################################################################################################################################################################################

    st.markdown('***')
    st.markdown('#### Accidentes por tipo de vehiculo')
        # Establece el tamaño del gráfico
    plt.figure(figsize=(10, 8))

    # Establece el tema de seaborn
    sns.set_theme()

    # Crea una lista con los nombres de las columnas de los vehículos
    columnas_vehiculos = ['moto', 'auto', 'transporte_publico', 'camion', 'ciclista']

    # Cuenta el número de accidentes para cada tipo de vehículo
    conteo_accidentes = [lesiones_df[col].str.contains('x').sum() for col in columnas_vehiculos]

    # Crea un DataFrame con los datos para el gráfico
    df_grafico = pd.DataFrame({
        'Tipo de vehículo': columnas_vehiculos,
        'Número de accidentes': conteo_accidentes
    })

    # Crea el gráfico de barras con seaborn
    ax = sns.barplot(y='Tipo de vehículo', x='Número de accidentes', data=df_grafico, palette=sns.color_palette("flare"))

    # Añade el número total en las barras
    for p in ax.patches:
        width = p.get_width()
        plt.text(width, p.get_y() + p.get_height()/2, int(width), va='center')

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)
    st.markdown('***')
    st.markdown('#### Accidentes por hora')

    ###########################################################################################################################################################################################################

    # Cuenta el número de accidentes en cada hora
    conteo_accidentes = lesiones_df['hora'].value_counts()

    # Crea un DataFrame con los datos para el gráfico
    df_grafico = pd.DataFrame({
        'Franja_Horaria': conteo_accidentes.index.astype(float).astype(int),  # Convierte a flotante y luego a entero
        'Número de accidentes': conteo_accidentes.values
    })

    # Ordena el DataFrame por 'Franja_Horaria'
    df_grafico = df_grafico.sort_values('Franja_Horaria')

    # Establece el tamaño del gráfico
    plt.figure(figsize=(10, 4))

    # Crea el gráfico de línea con seaborn
    sns.lineplot(x='Franja_Horaria', y='Número de accidentes', data=df_grafico)

    # Personaliza las etiquetas del eje x para mostrar todas las horas
    plt.xticks(range(0, 25))

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)
    
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

    ###########################################################################################################################################################################################################

    st.markdown('***')
    st.markdown('#### Victimas y Acusados por Vehiculo')

    # Cuenta el número total de víctimas y acusados por tipo de vehículo
    total_victimas = homicidios_df['victima'].value_counts()
    total_acusados = homicidios_df['acusado'].value_counts()

    # Crea un DataFrame con los datos para el gráfico
    df_victimas = pd.DataFrame({
        'Tipo de vehículo': total_victimas.index,
        'Total': total_victimas.values,
        'Categoría': 'Víctimas'
    })

    df_acusados = pd.DataFrame({
        'Tipo de vehículo': total_acusados.index,
        'Total': total_acusados.values,
        'Categoría': 'Acusados'
    })

    df_grafico = pd.concat([df_victimas, df_acusados])

    # Crea el gráfico de barras con seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(y='Tipo de vehículo', x='Total', hue='Categoría', data=df_grafico)

    plt.ylabel('Tipo de vehículo')
    plt.xlabel('Total')
    plt.title('Número total de víctimas y acusados por tipo de vehículo')
    plt.tight_layout()

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)

    ###########################################################################################################################################################################################################
    
    st.markdown('***')
    st.markdown('#### Accidentes por hora')
    # Filtra los datos para descartar las filas donde 'HH' es 'SD'
    homicidios_df_filtrado = homicidios_df[homicidios_df['hh'] != 'SD']

    # Asegúrate de que 'HH' es de tipo numérico
    homicidios_df_filtrado['hh'] = pd.to_numeric(homicidios_df_filtrado['hh'])

    # Agrupa los datos filtrados por la columna 'HH' y cuenta el número de accidentes
    accidentes_por_hora = homicidios_df_filtrado.groupby('hh').size()

    # Crea el gráfico de línea
    plt.figure(figsize=(15, 4))
    plt.plot(accidentes_por_hora.index, accidentes_por_hora.values)

    # Personaliza las etiquetas del eje x para mostrar cada hora
    plt.xticks(range(1, 25))

    plt.xlabel('Hora del día')
    plt.ylabel('Número de accidentes')
    plt.title('Número de accidentes por hora del día')
    plt.grid(True)

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)

    ###########################################################################################################################################################################################################

    st.markdown('***')
    st.markdown('#### Accidentes por mes de todos los años')
    homicidios_df['fecha'] = pd.to_datetime(homicidios_df['fecha'])

    # Extrae el año, el mes y el día de la fecha
    homicidios_df['Año'] = homicidios_df['fecha'].dt.year
    homicidios_df['Mes'] = homicidios_df['fecha'].dt.month

    # Selecciona el año que deseas visualizar
    # Desde 2016 hasta 2021
    año_seleccionado = 2021

    # Filtra los datos para incluir sólo los homicidios del año seleccionado
    homicidios_año_seleccionado = homicidios_df[homicidios_df['Año'] == año_seleccionado]

    # Cuenta el número de homicidios por mes
    homicidios_por_mes = homicidios_año_seleccionado['Mes'].value_counts().sort_index()

    # Crea un DataFrame con los datos para el gráfico
    df_grafico = pd.DataFrame({
        'Mes': homicidios_por_mes.index,
        'Número de homicidios': homicidios_por_mes.values
    })

    # Establece el tamaño del gráfico
    plt.figure(figsize=(15, 5))

    # Crea el gráfico de línea
    sns.lineplot(x='Mes', y='Número de homicidios', data=df_grafico, palette="rocket")

    plt.xlabel('Mes')
    plt.ylabel('Número de homicidios')
    plt.title(f'Número de homicidios a lo largo de los meses en {año_seleccionado}')
    plt.xticks(range(1, 13), ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], rotation=45)
    plt.tight_layout()

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)
    
    ###########################################################################################################################################################################################################

    st.markdown('***')
    st.markdown('#### Accidente por mes y año')

    homicidios_df['fecha'] = pd.to_datetime(homicidios_df['fecha'])

    # Extrae el año y el mes de la fecha
    homicidios_df['Año'] = homicidios_df['fecha'].dt.year
    homicidios_df['Mes'] = homicidios_df['fecha'].dt.month

    # Crea una lista con todos los años disponibles
    años_disponibles = list(homicidios_df['Año'].unique())

    # Añade la opción de 'Todos' a la lista de años
    años_disponibles.append('Todos')

    # Crea una lista desplegable para seleccionar el año
    año_seleccionado = st.selectbox('Selecciona un año', años_disponibles, index=len(años_disponibles)-1)

    # Crea un DataFrame vacío para almacenar los datos para el gráfico
    df_grafico = pd.DataFrame()

    # Para cada año en el DataFrame
    for año in homicidios_df['Año'].unique():
        # Si el año seleccionado es 'Todos' o el año actual
        if año_seleccionado == 'Todos' or año_seleccionado == año:
            # Filtra los datos para incluir sólo los homicidios del año seleccionado
            homicidios_año_seleccionado = homicidios_df[homicidios_df['Año'] == año]

            # Cuenta el número de homicidios por mes
            homicidios_por_mes = homicidios_año_seleccionado['Mes'].value_counts().sort_index()

            # Crea un DataFrame temporal con los datos para el gráfico
            df_temp = pd.DataFrame({
                'Mes': homicidios_por_mes.index,
                'Número de homicidios': homicidios_por_mes.values,
                'Año': año
            })

            # Añade los datos del año al DataFrame del gráfico
            df_grafico = pd.concat([df_grafico, df_temp])

    # Establece el tamaño del gráfico
    plt.figure(figsize=(15, 5))

    # Crea el gráfico de línea 
    sns.lineplot(x='Mes', y='Número de homicidios', hue='Año', data=df_grafico, palette="tab10")

    plt.xlabel('Mes')
    plt.ylabel('Número de homicidios')
    plt.title('Número de homicidios a lo largo de los meses por año')
    plt.xticks(range(1, 13), ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], rotation=45)
    plt.tight_layout()

    # Mueve la leyenda al exterior del gráfico en la parte superior
    plt.legend(title='Año', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Muestra el gráfico en Streamlit
    st.pyplot(plt)