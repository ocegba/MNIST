from flask import Flask, render_template, request
from flask_caching import Cache
import numpy as np
import keras
import re
import sys 
import os
import base64
sys.path.append(os.path.abspath("./models"))
from models.load import * 
import cv2

model = init()

app = Flask(__name__)

cache = Cache(app, config={
    'CACHE_TYPE': 'simple',  # Pour le développement. Utilisez 'redis' ou 'memcached' en production.
    'CACHE_DEFAULT_TIMEOUT': 300  # Temps en secondes
})


@app.route('/')
def index_view():
    return render_template('index.html')

def convert_image(img_data_1):
    try:
        imgstr = re.search(b'base64,(.*)', img_data_1).group(1)
        with open(os.path.join('models', 'output.png'), 'wb') as output:
            output.write(base64.b64decode(imgstr))

    except Exception as e:
        print(f"Erreur lors de la conversion de l'image : {e}")
        raise ValueError("Erreur dans la conversion de l'image")

@cache.memoize()  # Utiliser la mise en cache pour la fonction predict_model
def predict_model(x):
    out = model.predict(x)
    return np.argmax(out, axis=1)

@app.route('/predict/',methods=['GET','POST'])
def predict():
    img_data = request.get_data()
    convert_image(img_data) # On convertit l'image
    x = cv2.imread('models/output.png', cv2.IMREAD_GRAYSCALE)
    x = np.invert(x) # On inverse les couleurs
    x = cv2.resize(x, (28, 28)) # On redimensionne l'image
    x = x.reshape(1, 28, 28, 1) # On redimensionne l'image
    
    try:
        prediction = predict_model(x)
        response = str(prediction)
    except Exception as e:
        print(f"Erreur lors de la prédiction : {e}")
        response = "Erreur lors de la prédiction"
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)