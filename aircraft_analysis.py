from os import listdir
from os.path import join
import pandas as pd
import json

PATH = './2017-01-16/'
AIRBUS_MODELS = [ 'A300', 'A310', 'A320', 'A330', 'A340', 'A350', 'A380' ]
BOEING_MODELS = [ 'B707', 'B717', 'B737', 'B747', 'B757', 'B767', 'B777', 'B787' ]

# Initialize a dictionary with the keys from a dictionary
def initialize_dict(array):
    dictionary = {}
    for item in array:
        dictionary[item] = 0
    return dictionary

def process_json_data(data):
    # Extract the aircrafts
    aircrafts = data['acList']

    # Extract the aircraft types (for those which have it defined)
    models = [aircraft['Type'] for aircraft in aircrafts if 'Type' in aircraft]

    # Initialize Airbus and Boeing dictionaries
    airbus = initialize_dict(AIRBUS_MODELS)
    boeing = initialize_dict(BOEING_MODELS)

    # Process all aircraft models and update the dictionaries
    for model in models:
        for a in AIRBUS_MODELS:
            if a[:3] in model:
                airbus[a] += 1
        for b in BOEING_MODELS:
            if b[:3] in model:
                boeing[b] += 1

    return [airbus, boeing]

def get_column_names():
    files = listdir(PATH)
    names = [filename[12:16] for filename in files]
    return names

# Read files
results = []
for myfile in listdir(PATH):
    with open(join(PATH, myfile), 'r', encoding='utf-8') as json_data:
        print(myfile)
        results.append(process_json_data(json.load(json_data)))

# Create dataframe
df_airbus = pd.DataFrame()
df_boeing = pd.DataFrame()

i = 0
for result in results:
    airbus_column = pd.DataFrame.from_dict(result[0], orient='index')
    df_airbus = pd.concat([df_airbus, airbus_column], axis=1)

    boeing_column = pd.DataFrame.from_dict(result[1], orient='index')
    df_boeing = pd.concat([df_boeing, boeing_column], axis=1)
    i += 1

# Update column names
df_airbus.columns = get_column_names()
df_boeing.columns = get_column_names()

# Save processed data
df_airbus.to_csv('airbus.csv')
df_boeing.to_csv('boeing.csv')
