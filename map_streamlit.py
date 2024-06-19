import streamlit as st
import folium
from streamlit_folium import st_folium

# Título da aplicação
st.title('Mapa Interativo com Folium e Streamlit')

# Entradas para latitude e longitude
latitude = st.number_input('Latitude', format="%.6f")
longitude = st.number_input('Longitude', format="%.6f")

# Botão para adicionar o ponto
if st.button('Adicionar Ponto'):
    # Cria um mapa centralizado na última latitude e longitude inserida
    mapa = folium.Map(location=[latitude, longitude], zoom_start=5)
    
    # Adiciona o ponto ao mapa
    folium.Marker(location=[latitude, longitude], popup=f'Latitude: {latitude}, Longitude: {longitude}').add_to(mapa)
    
    # Exibe o mapa
    st_folium(mapa, width=700, height=500)
else:
    # Cria um mapa vazio centralizado em um local padrão
    mapa = folium.Map(location=[-27.2107, -49.6442], zoom_start=14)
    
    # Exibe o mapa
    st_folium(mapa, width=700, height=500)