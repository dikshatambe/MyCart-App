import json

def get_config(filename): 
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    return data
   
