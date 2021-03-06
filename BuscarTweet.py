

import twitterAPI
import json
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

# Login para la api de twitter
twitter_api =  twitterAPI.oauth_login()

app = Flask(__name__)
GoogleMaps(app)

# Función que busca 100 tweets que contengan el término que hemos introducido
# y devuelve las coordenadas de estos.
def buscarTweets(termino) :
    search_results = twitter_api.search.tweets(q=termino, count='100', geocode="36.5320510864,-6.2976899147,100km")
    tweets = search_results['statuses']

    coordenadas = []
    for tweet in tweets :
        if tweet['coordinates'] is not None: 
            coordenadas.append([tweet["coordinates"].values()[1][1], tweet["coordinates"].values()[1][0]])
    
    return coordenadas
# ********************************************************************************

# Se marcan en el mapa la coordenadas pasadas como parametro y se devuelve el mapa
def definirMapa(coordenadas):
    mapa = Map(
        identifier="view-side",
        lat=36.5320510864,
        lng=-5.2976899147,
        zoom=8,
        markers=coordenadas,
        style="height:500px;width:800px;margin:0;"
    ) 
    return mapa
# ********************************************************************************

# Vamos a mirar en la barra de direcciones si se ha incluido un término.
# Si es así, se buscarán tweets sobre ese término. Sino, se utilizará
# el término "hola" por defecto.
@app.route('/')
def defecto():
    mapa = definirMapa(buscarTweets("hola"))
    return render_template('localizacion.html', termino="hola", mymap=mapa)
@app.route('/termino/<termino>')
def personalizada(termino):
    mapa = definirMapa(buscarTweets(termino))
    return render_template('localizacion.html', termino=termino, mymap=mapa)

if __name__ == "__main__":
    app.run(debug=True)
