<h1 align="center">Proyecto Individual DA N°1</h1>
<h2 align="center">Facundo Blanco</h2>
<p align="center">
<img src="https://www.cio.com/wp-content/uploads/2023/05/statistics-stats-big-data-analytics-100613892-orig-4.jpg?quality=50&strip=all"  height=400>
</p>

## Descripcion

En este proyecto, he desarrollado un Análisis de Siniestros Viales en Buenos Aires. En este análisis de datos, exploraremos patrones, tendencias y factores clave relacionados con los accidentes de tráfico en la ciudad de Buenos Aires.

>- [Introducción](#introducción)
>- [Objetivo](#objetivo)
>- [Desarrollo](#desarrollo)
>   - [1 EDA (Análisis Exploratorio de Datos)](#1-eda-análisis-exploratorio-de-datos)
>   - [2 Dashboard Interactivo](#2-dashboard-interactivo)
>   - [3 Dashboard Streamlit](#3-dashboard-streamlit)
>   - [4 Despliegue](#4-despliegue)
>- [Analisis y Conclusiones](#analisis-y-conclusiones)
>- [Fuente de Datos](#fuente-de-datos)
>- [Contacto](#contacto)

## **Introducción**
Los siniestros viales son una preocupación seria en áreas urbanas densamente pobladas, y Buenos Aires no es una excepción. Cada incidente tiene un impacto significativo en la vida de las personas y en la seguridad vial en general. Por eso, voy a sumergirme en los datos para comprender mejor este desafío.

## **Objetivo**

Mi objetivo principal es proporcionar información valiosa que permita a las autoridades locales tomar decisiones informadas. Queremos reducir la cantidad de víctimas fatales en siniestros viales. A través de técnicas de análisis de datos y visualización, buscaremos identificar patrones y tendencias que nos ayuden a prevenir futuros accidentes.

## **Desarrollo**

- ### **1 EDA (Análisis Exploratorio de Datos)**

       Durante la fase de Análisis Exploratorio de Datos (EDA), lleve a cabo las siguientes acciones:

    - **Revisión de Columnas:** Analice las columnas para entender su contenido y tipo de dato.
    - **Normalizaciones:** Realice normalizaciones de datos, corrigiendo nombres de columnas mal escritos, ajustando tipos de datos y normalizando valores en las columnas.
    - **Eliminación de Duplicados y Nulos:** Elimine duplicados y registros nulos que pudieran afectar la calidad de los datos.
    - **Visualizaciones Gráficas:** Cree gráficos para visualizar el comportamiento de los datos y detectar posibles errores o patrones.
    - **Normalizaciones Adicionales:** Realice normalizaciones adicionales después de las visualizaciones para abordar cualquier problema identificado.
    - **Combinación de Datasets:** Combine los datasets en uno solo después de asegurar la coherencia y calidad de los datos.
    - **Exportación de Datos:** Los datos preparados se exportaron en archivos CSV para su uso posterior en las herramientas Power BI y Streamlit.

    [Notebook EDA](EDA.ipynb) ofrece detalles más específicos y los datasets optimizados están listos para ser utilizados en las siguientes etapas del proyecto, incluyendo la construcción de dashboards interactivos.

- ### **2 Dashboard Interactivo**
    Para el diseño del dashboard interactivo, realice análisis divididos en tres partes principales, cada una con su propia página dentro del dashboard:

    1. **Análisis Temporal:**
        - La primera página se centra en el tiempo, distribuyendo los accidentes en diferentes periodos de tiempo. Los gráficos proporcionan una visión clara de cómo la cantidad de accidentes varía a lo largo del tiempo.

    2. **Análisis de Participantes:**
        - La segunda página profundiza en los participantes y víctimas de los accidentes. Los gráficos detallados ofrecen información específica sobre los involucrados en los siniestros viales.

    3. **Análisis Geográfico:**
        - La tercera página se dedica al análisis geográfico de los accidentes. Los mapas y gráficos muestran la distribución geográfica de los incidentes, proporcionando perspectivas valiosas sobre las áreas de mayor concentración.

    4. **KPIs:**
        - La última página del dashboard presenta indicadores clave de rendimiento (KPIs) esenciales.


        Para evaluar el impacto y la gravedad de los siniestros viales, ocupe tres indicadores clave de rendimiento (KPIs):
        1. **Tasa de Homicidios por 100,000 Habitantes:**
            - Este indicador proporciona una perspectiva sobre la gravedad de los siniestros viales en términos de pérdida de vidas humanas, normalizado por la población.

        2. **Tasa de Accidentes Fatales de Motos:**
            - Este KPI se centra en los siniestros que involucran motocicletas, evaluando la gravedad específica de los accidentes de este tipo de vehículo.

        3. **Tasa de Accidentes Fatales en Avenidas:**
            - Este indicador destaca la gravedad de los accidentes que ocurren en avenidas, brindando información crucial sobre la seguridad vial en estas áreas específicas.

        Cada uno de estos KPIs ofrece una medida clave para evaluar aspectos específicos de la seguridad vial. La presentación de estos indicadores se integra en el dashboard, proporcionando a los usuarios una comprensión clara de estos aspectos críticos.

    5. **Diseño:**
    
    El diseño sigue el patrón Z, con el título de la página y datos importantes en la parte superior. El espacio central se ocupa con gráficos de mayor jerarquía, y a la derecha se encuentran los filtros para aplicar al dashboard.

    <p align="center">
    <img src="img/Diseño dashboard.jpg"  height=400>
    </p>

    Este diseño sigue una distribución visual efectiva, facilitando la comprensión de los datos para los usuarios. Además, se proporcionan filtros para permitir una interacción más personalizada con el dashboard.


    [Dashboard Interactivo](dashboard/dashboardv2.pbix) En este enlace se puede ir al Dashboard Interactivo para que puedan explorar los datos por sí mismos.

- ### **3 Dashboard Streamlit**
    Aprovechando la oportunidad decidi explorar nuevas herramientas, decidi utilizar Streamlit para crear un dashboard interactivo. Este dashboard presenta los mismos gráficos generados durante el análisis exploratorio de datos (EDA) utilizando código Python.

    El código utilizado para la herramienta de Streamlit se encuentra en los archivos:
    
    - [`Dashboard.py`](Dashboard.py)
    - [`pages/Datasets.py`](pages/Datasets.py)

    Estos archivos contienen el código necesario para implementar la lógica y la presentación del dashboard. Streamlit facilita la creación de aplicaciones web interactivas a partir de scripts de Python, y esta elección permitió aprovechar los gráficos existentes para crear una experiencia de usuario dinámica e interactiva.

- ### **4 Despliegue**

    Para el despliegue de la aplicación Streamlit, segui la guía paso a paso proporcionada por Streamlit. El despliegue se realizó vinculando directamente este repositorio.

    El proceso de despliegue implicó:

    1. Seguir la guía oficial de despliegue de Streamlit.
    2. Vincular este repositorio a la plataforma de despliegue.
    3. Instalar las dependencias necesarias.
    4. Confirmar y ejecutar el despliegue.

    La aplicación Streamlit ahora está disponible para su acceso público.

    El enlace para acceder a la aplicación desplegada es [aquí](https://facundoblancodeploypida.streamlit.app/), y cualquier actualización en el repositorio se reflejará automáticamente en la aplicación desplegada.

    El proceso de despliegue fue directo y la aplicación ahora está lista para ser utilizada y compartida.


## **Analisis y Conclusiones**
### Problemas Detectados durante las Visualizaciones:

1. **Aumento en Muertes durante Noviembre y Diciembre:**
   Durante estos meses, hay un aumento en las muertes por accidentes, posiblemente relacionado con la celebración de festividades, lo que lleva a una menor precaución por parte de los conductores.

2. **Mayor Número de Víctimas en Horas de la Madrugada:**
   Se registra un aumento en el número de víctimas durante las horas de la madrugada, atribuido a factores como la limitada visibilidad y la fatiga de los conductores.

3. **Impacto en Motociclistas y Peatones:**
   Motociclistas y peatones son los más afectados debido a su mayor vulnerabilidad, ya que carecen de las medidas de seguridad que tienen los conductores de automóviles.

4. **Involucramiento Frecuente de Automóviles en Accidentes:**
   Los automóviles son los más frecuentemente involucrados, posiblemente debido a distracciones al volante y comportamientos arriesgados como el exceso de velocidad.

5. **Mayores Accidentes en Avenidas:**
   La mayoría de los accidentes ocurren en avenidas, posiblemente debido a la congestión vehicular y condiciones de conducción más desafiantes en estas áreas.


### Posibles Soluciones:

1. **Campañas de Concientización:**
   - Implementar campañas educativas durante noviembre y diciembre.
   - Destacar riesgos asociados a la conducción imprudente durante festividades.
   - Mensajes sobre la importancia de mantener la precaución y evitar distracciones.

2. **Refuerzo de Patrullaje Nocturno:**
   - Aumentar la presencia policial en horas de la madrugada.
   - Considerar controles de fatiga para garantizar condiciones óptimas de los conductores.

3. **Infraestructura Segura para Peatones y Motociclistas:**
   - Mejorar cruces peatonales con iluminación.
   - Establecer carriles exclusivos y señalización para motociclistas.

4. **Programas de Conducción Responsable:**
   - Desarrollar programas de concientización.
   - Enfatizar la importancia de evitar distracciones y respetar límites de velocidad.
   - Incluir incentivos para conductores con historial seguro.

5. **Mejora de la Infraestructura Vial en Avenidas:**
   - Evaluar y mejorar infraestructura vial en avenidas.
   - Reducir congestión, mejorar señalización y optimizar flujo de tráfico.


## **Fuente de datos**

Los datos de los siniestros viales fueron tomados de la página oficial del gobierno de Buenos Aires (data.buenosaires)

[Datasets](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales)

## **Contacto**

[<img src="https://cdn-icons-png.flaticon.com/256/174/174857.png" alt="LinkedIn" width="50"/>](https://www.linkedin.com/in/facundo-blanco-a0089024a/)   [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/640px-Gmail_icon_%282020%29.svg.png" alt="Correo Electrónico" width="50"/>](mailto:blancofacundo0@gmail.com)   [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="50"/>](https://github.com/FacuSB)