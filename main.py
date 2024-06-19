import folium

mapa = folium.Map(location=[-27.2107, -49.6442], zoom_start=14)

bairros = {
    'Centro': [
        (-27.2157, -49.6452),
        (-27.2150, -49.6460)
    ],
    'Jardim América': [
        (-27.2118, -49.6439),
        (-27.2092, -49.6422),
        (-27.2095, -49.6425),
        (-27.2090, -49.6420)
    ]
}

for bairro, coords in bairros.items():
    if bairro == 'Centro':
        icon_color = 'red'  
    elif bairro == 'Jardim América':
        icon_color = 'blue'  

    for lat, lon in coords:
        folium.Marker(
            location=[lat, lon],
            popup=f'<strong>Bairro:</strong> {bairro}<br><strong>Total:</strong> {len(coords)}',
            icon=folium.Icon(color=icon_color)  
        ).add_to(mapa)

mapa.save('mapa_com_pontos.html')
