import pickle
import json
import numpy as np
from os import path
location_values = None
model = None

def load_saved_attributes():
    global location_values
    global model
    with open("columns.json", "r") as f:
        resp = json.load(f)
        location_values = resp["data_columns"]
    model = pickle.load(open("banglore_home_prices_model.pickle", "rb"))

def get_location_names():
    return location_values

def predict_house_price(location, sqft, bhk, bathrooms):
    try:
        loc_index = location_values.index(location)

    except:
        loc_index = -1

    loc_array = np.zeros(len(location_values))
    if loc_index >=0:
        loc_array[loc_index] = 1
    sample = np.concatenate((np.array([sqft,bathrooms,bhk]), loc_array))

    return model.predict(sample.reshape(1,-1))[0]
if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()