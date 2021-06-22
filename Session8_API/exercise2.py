import requests
import pprint

response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemon_stats = response.json()
# pprint.pprint(pokemon_stats)

print(pokemon_stats["weight"])

print(len(pokemon_stats["abilities"]))

ability_names = []
for names in pokemon_stats["abilities"]:
    ability_names.append(names["ability"]["name"])

print(ability_names)