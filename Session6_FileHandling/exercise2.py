# # Writing to a txt file. 'w' creates a file if it doesn't exist
with open('pokemon.txt','w')as Pokemon:
    Pokemon.write('Pikachu')

# Adding more info to the existing pokemon.txt file
with open('pokemon.txt','a') as Pokemon:
    Pokemon.write('\nCharizard')

# Adding multiple data at once
# new_names = ['Eevee', 'Squirtle', 'Weedle', 'Raichu']
with open('pokemon.txt','a') as Pokemon:
    Pokemon.writelines(['\nEevee', '\nSquirtle', '\nWeedle', '\nRaichu'])