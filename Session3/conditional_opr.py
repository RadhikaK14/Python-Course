#1a
shirt_price = float(input('Please enter the price of the shirt\n'))
shirt_colour = input('What is its colour?\n')
shirt_in_budget = (shirt_price <=25.00 and shirt_colour.lower() == 'yellow')

print(f'Shirt is available within budget and correct colour: {shirt_in_budget}')


