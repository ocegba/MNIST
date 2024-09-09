import numpy as np
from keras.models import Sequential, load_model, model_from_json
from keras import backend as K

def init(): 
    json_file = open('models/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    
    # Charger les poids dans le nouveau modèle
    loaded_model.load_weights("models/mnist_model.h5")
    print("Modèle chargé à partir du disque")

    # Compiler et évaluer le modèle chargé
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return loaded_model
