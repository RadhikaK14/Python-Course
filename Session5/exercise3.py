my_poke = {'pokemon' : 'Bulbasaur',
            'type': 'Grass',
            'Level': 5}

my_poke['moves'] = ['vine whip', 'razor leaf', 'growl', 'cut']

print(my_poke)

my_poke['Level'] = 10
print(my_poke)

for move in my_poke['moves']:
    if move == 'cut':
        print(f'{move} move exists')
