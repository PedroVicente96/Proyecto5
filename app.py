import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Conjunto de venta de autos')
hist_checkbox = st.checkbox('Construir histograma')  # crear un botón
scatt_checkbox = st.checkbox('Construir diagrama de dispersión')
pie_checkbox = st.checkbox('Contruir un diagrama de pastel')
bar_checkbox = st.checkbox('Contruir un diagrama de barras')

if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Millas recorridas",
                       labels={'odometer': 'Odómetro', 'count': 'Conteo'},
                       )
    fig.update_xaxes(title_text='Odómetro')
    fig.update_yaxes(title_text='Conteo')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatt_checkbox:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='type', y='cylinders',
                     title='Cilindros por tipo de vehículo',
                     labels={'type': 'Tipo de vehículo',
                             'cylinders': 'No. de cilindros'},
                     )
    fig.update_xaxes(title_text='Tipo de vehículo')
    fig.update_yaxes(title_text='No. de cilindros')
    st.plotly_chart(fig, use_container_width=True)

if pie_checkbox:
    st.write(
        'Creación de un diagrama de pastel para el conjunto de datos de anuncions de venta de coches')
    fig = px.pie(car_data, names='condition', title='Condición de los coches',
                 )
    fig.update_layout(
        xaxis_title='Condición',
        yaxis_title='Porcentaje',
        showlegend=True
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if bar_checkbox:
    fig = px.bar(car_data, y='price', x='model_year',
                 title='Rango de Precios de los Coches por año')
    fig.update_layout(yaxis_title='Precio')
    fig.update_layout(xaxis_title='Año')
    st.plotly_chart(fig, use_container_width=True)
