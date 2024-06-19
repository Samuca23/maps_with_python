from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Cria um mapa centralizado em uma localização padrão
    mapa = folium.Map(location=[-15.7942, -47.8822], zoom_start=5)
    
    if request.method == 'POST':
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])
        folium.Marker(location=[lat, lon], popup=f'Latitude: {lat}, Longitude: {lon}').add_to(mapa)
    
    mapa.save('templates/mapa.html')
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run(debug=True)