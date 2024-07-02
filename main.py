import folium
import json

mapa = folium.Map(location=[-27.2111, -49.6470], zoom_start=13)

with open('locations.json', 'r', encoding='utf-8') as file:
    bairros = json.load(file)

for bairro, coords in bairros.items():
    if bairro == 'Agronômica':
        circle_color = '#351c75'
    elif bairro == 'Albertina':
        circle_color = '#ff6d01'
    elif bairro == 'Barra do Trombudo':
        circle_color = '#34a853'
    elif bairro == 'Barragem':
        circle_color = '#ffd966'
    elif bairro == 'Bela Aliança':
        circle_color = '#3c78d8'
    elif bairro == 'Boa Vista':
        circle_color = '#00e0ff'
    elif bairro == 'Bremer':
        circle_color = '#c00'
    elif bairro == 'Budag':
        circle_color = '#f005ff'
    elif bairro == 'Canoas':
        circle_color = '#000'
    elif bairro == 'Canta Galo':
        circle_color = '#5b0f00'
    elif bairro == 'Eugênio Schneider':
        circle_color = '#274e13'
    elif bairro == 'Fundo Canoas':
        circle_color = '#57c1ff'
    elif bairro == 'Itoupava':
        circle_color = '#fbbc04'
    elif bairro == 'Jardim América':
        circle_color = '#009764'
    elif bairro == 'Laranjeiras':
        circle_color = '#666'
    elif bairro == 'Laurentino':
        circle_color = '#245151'
    elif bairro == 'Navegantes':
        circle_color = '#e69138'
    elif bairro == 'Pamplona':
        circle_color = '#d5a6bd'
    elif bairro == 'Progresso':
        circle_color = '#d9d9d9'
    elif bairro == 'Rainha':
        circle_color = '#4285f4'
    elif bairro == 'Santa Clara':
        circle_color = '#b6d7a8'
    elif bairro == 'Sumaré':
        circle_color = '#8f00ff'

    for coord in coords:
        id = coord['id']
        lat = coord['latitude']
        lon = coord['longitude']
        rua = coord['address']

        html_icon = f"""
        <div style="position: relative; width: 25px; height: 25px; border-radius: 50%; background-color: {circle_color}; display: flex; justify-content: center; align-items: center; color: white; border: 1px solid #6b6b6b">
            <i class="fa fa-map-marker-alt" style="font-size: 14px; color: #fff"></i>
        </div>
        """

        folium.Marker(
            location=[lat, lon],
            popup=f'<strong>Inscrição: </strong>{id}<br/><strong>Endereço: </strong>{rua}',
            icon=folium.DivIcon(html=html_icon)
        ).add_to(mapa)

legend_html = '''
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; width: 200px; height: 90px; 
     background-color: white; z-index:9999; font-size:14px;
     border:2px solid grey; padding: 10px;">
     <b>Legenda:</b>
     <p>Centro</p>
     <p>Jardim América</p>
     </div>
     '''
mapa.get_root().html.add_child(folium.Element(legend_html))

title_html = '''
             <h3 align="center" style="font-size:20px"><b>Mapa de Bairros</b></h3>
             '''
mapa.get_root().html.add_child(folium.Element(title_html))

mapa.save('mapa_com_pontos.html')
