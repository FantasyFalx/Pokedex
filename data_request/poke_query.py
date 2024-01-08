# File that is used to extract poke json data for dex builder 

# Imports 

import json as jsn
import urllib.request

# Json conversion 

data = open("pokedata/api_data.json")

pokedata = jsn.load(data)


# Extraction for pokemon data

def poke_grabber(user_input) -> []: 

    poke_container = ["uknown", "unknown", "unknown", "unkown", 
                      urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/3/39/Pokeball.PNG"
                                                                                           ,"pokedata/poke.png")]

    for i in range(1,len(pokedata)):
        if pokedata[str(i)]['name'] == user_input.lower():
            poke_container[0] = i
            poke_container[1] = pokedata[str(i)]['name']
            poke_container[2] = pokedata[str(i)]['height']
            poke_container[3] = ', '.join(pokedata[str(i)]['type'])
            poke_container[4] = urllib.request.urlretrieve(pokedata[str(i)]['sprite_image'], "pokedata/poke.png")

    return poke_container

 
print(type(poke_grabber("mew")[2])) 

