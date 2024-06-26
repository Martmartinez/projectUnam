import streamlit as st
import pandas as pd
import plotly_express as px

car_data=pd.read_csv('vehicles_us.csv')

st.header("Proyecto de despliegue de servidor web con render")
hist_button=st.button('Construir Histograma')

if hist_button:
    #Mostrar menskae
    st.write('Creación de un Histograma para el conjunto de datos')
    fig=px.histogram(car_data,x="odometer")
    st.plotly_chart(fig,use_container_width=True)

#Agregar otro button para construir un gráfico de dispersión cuando se haga clic
dispersion_button=st.button("Construir un gráfico de dispersión con los datos del dataframe actual. ()=>")
if dispersion_button:
    #Mostrar un mensaje
    st.write("Creación de un gráfico de dispersión para el conjunto de datos.")
    #Crear el gráfico de dispersión
    fig=px.scatter(car_data,x="odometer",y="price")
    
    #Mostrar el grafico interactivo
    st.plotly_chart(fig,use_container_width=True)

#Para el reto anexado a la actividad con el checkBox
check_box=st.checkbox("Check para generar el gráfico de dispersión")
if check_box:
    st.write("Generar un gráfico de dispersión de los datos actuales")
     #Crear el gráfico de dispersión
    fig=px.scatter(car_data,x="odometer",y="price")
    
    #Mostrar el grafico interactivo
    st.plotly_chart(fig,use_container_width=True)



