import folium

mapa = folium.Map(location=[-27.2111, -49.6470], zoom_start=13)

bairros = {
    'Centro': [
        (-27.2157, -49.6452, 23),
        (-27.2150, -49.6460, 25)
    ],
    'Jardim América': [
        (-27.2118, -49.6439, 1),
        (-27.2092, -49.6422, 2),
        (-27.2095, -49.6425, 3),
        (-27.2090, -49.6420, 4),
        (-27.219122, -49.645725, 5)
    ]
}

for bairro, coords in bairros.items():
    if bairro == 'Centro':
        icon_color = 'red'  
    elif bairro == 'Jardim América':
        icon_color = 'black'  

    for lat, lon, cod in coords:
        folium.Marker(
            location=[lat, lon],
            popup=f'<strong>Código:</strong>{cod}',
            icon=folium.Icon(color=icon_color)  
        ).add_to(mapa)

legend_html = '''
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; width: 200px; height: 90px; 
     background-color: white; z-index:9999; font-size:14px;
     border:2px solid grey; padding: 10px;">
     <b>Legenda:</b><br>
     <i class="fa fa-map-marker fa-2x" style="color:#cc3b28"></i>&nbsp; Centro<br>
     <i class="fa fa-map-marker fa-2x" style="color:#36a5d7"></i>&nbsp; Jardim América
     </div>
     '''
mapa.get_root().html.add_child(folium.Element(legend_html))

title_html = '''
             <h3 align="center" style="font-size:20px"><b>Mapa de Bairros</b></h3>
             '''
mapa.get_root().html.add_child(folium.Element(title_html))

# Salva o mapa
mapa.save('mapa_com_pontos.html')
