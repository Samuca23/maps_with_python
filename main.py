import folium
import json

mapa = folium.Map(location=[-27.2111, -49.6470], zoom_start=13)

with open('locations.json', 'r') as file:
    bairros = json.load(file)

for bairro, coords in bairros.items():
    icon_color = 'red' if bairro == 'Centro' else 'black'

    for coord in coords:
        lat = coord['latitude']
        lon = coord['longitude']
        cod = coord['number']
        rua = coord['address']
        
        folium.Marker(
            location=[lat, lon],
            popup=f'<strong>Código:</strong> {cod} RUA: {rua}',
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

mapa.save('mapa_com_pontos.html')
