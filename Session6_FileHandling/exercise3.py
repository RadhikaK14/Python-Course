import csv

# Reading csv file
with open('scoreboard.csv', 'r') as file:
    csvreader = csv.reader(file)
    for items in csvreader:
        print(items)

with open('scoreboard.csv', 'r') as file:
    csvreader = csv.reader(file)
    for items in csvreader:
        print(f'{items[0].capitalize()} has a high score of {items[1]}')

# Writing to the csv file. writerow takes single list, writerows takes list of lists
with open('scoreboard.csv', 'a') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['Brock', '2'])