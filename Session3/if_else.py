#2a
shopping_cost = float(input('What is the total price of your shopping?\n'))
discount_applicable = input('Do you have a discount code? y/n\n')
shipping = 5

if (shopping_cost > 20.00 and discount_applicable.lower() == 'y'):
    total_cost = shopping_cost * 0.9
elif (shopping_cost >= 100.00):
    total_cost = shopping_cost * 0.95
else:
    total_cost = shopping_cost

if total_cost < 30.00:
    total_cost = total_cost + shipping

print(f'The total cost is {total_cost}')

