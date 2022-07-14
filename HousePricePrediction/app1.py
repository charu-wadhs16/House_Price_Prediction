import pickle
import json
import numpy as np
from os import path
model = None
vect=None

def load_saved_attributes():
    global model
    global vect
    model = pickle.load(open("model.pickle", "rb"))
    vect=pickle.load(open('vectorizer.pickle', 'rb'))

def predict(data):
    return model.predict(vect.transform([data]).toarray())[0]