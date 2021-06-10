# #2a
my_stats = {'Name': 'Radhika',
            'Age' : 32,
            'Gender': 'Female'}
print(my_stats)

# #inserting new values
my_stats['occupation'] = 'Tech'

# # deleting values
del my_stats['Gender']
# print(my_stats)

# #Replacing values
my_stats['Age'] = 31
# print(my_stats)

# #printing a value
print(my_stats['Name'])

my_pokemon = {'pokeman': 'Rapidash',
                 'type': 'Fire',
                 'level': 30}

my_pokemon['move'] = 'Flame Wheel'

print(my_pokemon)

for key in my_pokemon.keys():
     print(key)

for values in my_pokemon.values():
    print('Values : ' + str(values))

# for k,v in my_pokemon.items():
#     print(k + ' : ' + str(v))

my_pokemon['move'] = ['Flame wheel', 'Agility']
# print(my_pokemon)

for moves in my_pokemon['move']:
    print(moves)