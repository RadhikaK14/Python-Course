#Creating list [0,1,2,3,4]
pokemon = ['Metapod', 'Caterpie', 'Butterfree', 'Weedle', 'Raichu']
print(pokemon)

#Adding values to the list
pokemon.insert(2, 'Pikachu')
print(pokemon)

#removing using value
pokemon.remove('Weedle')
print(pokemon)

#removing using index
pokemon.pop(1)
print(pokemon)

#printing 3rd value in the list
print(pokemon[3])

#1b
my_team = ['Landorus', 'Weedle', 'Spearow', 'Pidgey', 'Gardevoir']

#1c Concatinating List
pokedex = pokemon + my_team
print(pokedex)

#1d adding values
pokedex.insert(3, 'Rattata')
print(pokedex)

#1e finding length of the list
print(len(pokedex))

#1f printing each values in list one by one using 'for'
for i in pokedex:
    print(i)

#1g Checking for a value
for i in pokedex:
    if (i == 'Weedle'):
        print('Weedle is in the Pokedex')

if 'Weedle' in pokedex:
    print('Weedle found using if')
# list.append(value)-additemtoendoflist
# list.insert(index, value)-additematindex
# list.remove(value)-removeitembyvalue
# list.pop(index)-removeitematindex
# list.pop()-removesthelastitem
# list.clear()-emptiesthelist