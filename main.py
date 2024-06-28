import folium
import json

mapa = folium.Map(location=[-27.2111, -49.6470], zoom_start=13)

with open('locations.json', 'r', encoding='utf-8') as file:
    bairros = json.load(file)

for bairro, coords in bairros.items():
    if bairro == 'Agronômica':
        circle_color = '#351c75'
        icon_color = '#fff'
    elif bairro == 'Albertina':
        circle_color = '#ff6d01'
        icon_color = '#fff'
    elif bairro == 'Barra do Trombudo':
        circle_color = '#34a853'
        icon_color = '#fff'
    elif bairro == 'Barragem':
        circle_color = '#ffd966'
        icon_color = '#000'
    elif bairro == 'Bela Aliança':
        circle_color = '#3c78d8'
        icon_color = '#fff'
    elif bairro == 'Boa Vista':
        circle_color = '#00e0ff'
        icon_color = '#fff'
    elif bairro == 'Bremmer':
        circle_color = '#c00'
        icon_color = '#fff'
    elif bairro == 'Canoas':
        circle_color = '#000'
        icon_color = '#fff'
    elif bairro == 'Canta Galo':
        circle_color = '#5b0f00'
        icon_color = '#fff'
    elif bairro == 'Eugênio Schneider':
        circle_color = '#274e13'
        icon_color = '#fff'
    elif bairro == 'Fundo Canoas':
        circle_color = '#4c1130'
        icon_color = '#fff'
    elif bairro == 'Itoupava':
        circle_color = '#fbbc04'
        icon_color = '#fff'
    elif bairro == 'Jardim América':
        circle_color = '#009764'
        icon_color = '#fff'
    elif bairro == 'Laranjeiras':
        circle_color = '#666'
        icon_color = '#fff'
    elif bairro == 'Laurentino':
        circle_color = '#245151'
        icon_color = '#fff'
    elif bairro == 'Navegantes':
        circle_color = '#e69138'
        icon_color = '#fff'
    elif bairro == 'Pamplona':
        circle_color = '#d5a6bd'
        icon_color = '#fff'
    elif bairro == 'Progresso':
        circle_color = '#d9d9d9'
        icon_color = '#000'
    elif bairro == 'Rainha':
        circle_color = '#4285f4'
        icon_color = '#fff'
    elif bairro == 'Santa Clara':
        circle_color = '#b6d7a8'
        icon_color = '#fff'
    elif bairro == 'Sumaré':
        circle_color = '#8f00ff'
        icon_color = '#fff'

    for coord in coords:
        id = coord['id']
        lat = coord['latitude']
        lon = coord['longitude']
        rua = coord['address']

        html_icon = f"""
        <div style="position: relative; width: 25px; height: 25px; border-radius: 50%; background-color: {circle_color}; display: flex; justify-content: center; align-items: center; color: white; border: 1px solid #6b6b6b">
            <i class="fa fa-map-marker-alt" style="font-size: 14px; color: {icon_color}"></i>
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
