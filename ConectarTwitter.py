# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

__author__ = 'Grupo08'
import twitter
import io
import json

#Conexión haciendo uso de las credenciales del ejemplo
def oauth_login():
    CONSUMER_KEY = 'vWRIn7cDDPqwNg0jpz9ej8klZ'
    CONSUMER_SECRET = 'UzQznpC8o3ylUfcbYhKwV6Kt3MoDOgnSxu9Jnn3tmEbKTaHRZe'
    OAUTH_TOKEN = '7730092-BvcE6lKJs8455JE8hyEhYHKXHX5g9X05izuuU47qIX'
    OAUTH_TOKEN_SECRET = 'xGzotzBjBImJNDLAogP60jb3GVlRnp3M9jtp3QSFgJDAI'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()

