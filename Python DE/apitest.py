import random

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/M145TA")

print(post_codes_req.json)
#print(post_codes_req.content)
#print(post_codes_req.text)

json_body = json.dumps({"postcodes": ["PR3 0SG", "M14 5TA", "MK176PJ"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers = headers, data=json_body)

print(type(post_multi_req))

#make a pokemon game in the cmd line with the api have a single player mode & 2 player fight with ply

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon?limit=6")
data = pokemon_req.json()
random_pokemon = random.choice(data["results"])
response = requests.get(random_pokemon["url"])
data = response.json()

name = data['name']

print(name)
