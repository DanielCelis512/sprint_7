import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st
import random

# Agregar encabezado.
st.header("Análisis de Anuncios de Venta de Carros.")

# Leer los datos del archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Agregar nueva columna para el uso adecuado de los datos.
car_data["manufacturer"] = car_data["model"].str.split().str[0]

# Mostrar los datos a trabajar.
st.subheader("Vizulalización de Datos.")
st.dataframe(car_data)

# Crear un botón para filtrar tipos de vehículo por fabricante.
bar_button = st.button("Construir Gráfica y Filtrar.")

# Filtrar por tipo de Vehículos.
tipos = car_data["type"].unique()
seleccion = st.multiselect("Selecciona tipos de vehículo:", tipos)

# Lógica a ejecutar cuando se hace clic.
if bar_button:
    # Mensaje de la aplicación.
    st.write("Creación de una Gráfica de Barras para filtrar Fabricantes por Tipo de Vehículos.")
    

    # Mostrar información con y sin filtro.
    if len(seleccion) == 0:
        car_filtrado = car_data
    else:
        car_filtrado = car_data[car_data["type"].isin(seleccion)]
    
    # Variable de conteo para la cráfica.
    conteo = car_filtrado['manufacturer'].value_counts()
    
    # Generador de colores aleatorios para cada tipo de vehículo.
    colores = []
    for color in conteo.index:
        color_rdm = "#"+"".join(random.choice("0123456789ABCDEF") for _ in range(6))
        colores.append(color_rdm)

    # Crear el gráfico de barras.
    fig = go.Figure(data=[go.Bar(x=conteo.index, y=conteo.values, marker_color=colores)])

    # Título de la gráfica.
    fig.update_layout(title_text='Tipo de Vehículo por Fabricante.')

    # Mostrar el gráfico.
    st.plotly_chart(fig, width="stretch")

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir Histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un Histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure()

    # Ciclo for para definir la información del histograma.
    for condition in car_data["condition"].unique():
        fig.add_trace(go.Histogram(
            x=car_data[car_data["condition"]==condition]["model_year"],
            name=condition
        ))

    # Título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Condición con respecto al Año del Modelo')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, width="stretch")

# Crear otro botón para otro gráfico.
scatter_button = st.button("Construir Gráfico de Dispersión")

# Cuando se oprime el nuevo botón.
if scatter_button:
    # Escribe un mensaje explicativo de lo que hace.
    st.write("Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches")

    # Crear un gráfico de dispersión.
    fig = go.Figure(data=[go.Scatter(x=car_data['model_year'], y=car_data["price"], mode="markers", marker_color="rgba(255, 0, 0, 0.3)")])

    # Título del gráfico.
    fig.update_layout(title_text='Dispersión del Odómetro por Precio')
    
    # Mostrar el gráfico interactivo.
    st.plotly_chart(fig, width="stretch")

