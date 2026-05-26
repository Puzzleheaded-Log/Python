""" 
Write a Python script that:
  - uses the PokeAPI
  - takes a Pokémon type as a command-line argument (e.g. fire, water)
  - fetches data for that type
  - prints the names of the first 20 Pokémon of that type.   """

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://pokeapi.co/api/v2/type/" + sys.argv[1])
data = response.json()

for result in data["pokemon"][:20]:
    print(result["pokemon"]["name"])
