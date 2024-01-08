# File that extracts required pokedata from the api

# Imports

import requests as req
import json as jsn  
import pokeobjs as pkobs

# Call constants

url = "https://pokeapi.co/api/v2/pokemon/"
type_key_1 = "type"
type_key_2 = "name"
sprite_key_1 = "sprites"
sprite_key_2 = "front_default"
container_transport = ""

# Call containers

poke_container = {}
type_container = []

# The call

for i in range(1, 1011):
    
    called_data = req.get(f"{url}{i}")

    json_transfer = called_data.json()

    for types in json_transfer['types']:
        type_container.append(types[type_key_1][type_key_2])

    # Object creation:

    poke_container[i] = pkobs.Pokemon(json_transfer['name'],
                                      float(json_transfer['height']),
                                      type_container, 
                                      json_transfer[sprite_key_1][sprite_key_2]).__dict__
    
    type_container = []

# File write 

container_transport = jsn.dumps(poke_container, indent=4)

with open("pokedata/api_data.json", "w") as pokedata:
    jsn.dump(poke_container, pokedata, indent=4)

