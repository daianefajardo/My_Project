import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\daian\Documents\GitHub\My_Project\vehicles.csv') # Carregar os dados do CSV

st.header('Analise de Dados de Carros') # Cabeçalho do aplicativo

# Botão para criar um histograma
hist_button = st.button('Criar Histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


# Botão para criar um gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para criar um gráfico de dispersão
if st.checkbox('Criar Gráfico de Dispersão'):
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    fig = px.scatter(car_data, x='odometer', y='price', title='Gráfico de Dispersão de Odometer vs Preço')
    
    st.plotly_chart(fig, use_container_width=True)