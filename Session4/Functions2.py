#2a 
def shopping_calculator(cost, discount):
        shipping = 5
        if (cost > 20.00 and discount.lower() == 'y'):
            total_cost = cost * 0.9
        elif (cost >= 100.00):
            total_cost = cost * 0.95
        else:
            total_cost = cost

        if total_cost < 30.00:
            total_cost = total_cost + shipping
        return total_cost

total_shopping_cost = shopping_calculator(30, 'y')
print(f'The total shopping cost is £{total_shopping_cost}')

#2b
def shopping_calculator(cost, discount):
        shipping = 5
        if cost < 30.00:
            total_cost = cost + shipping

        if (cost > 20.00 and discount == True):
            total_cost = cost * 0.9
        elif (cost >= 100.00):
            total_cost = cost * 0.95
        else:
            total_cost = cost

        return total_cost

total_shopping_cost = shopping_calculator(32, True)
print(f'The total shopping cost is £{total_shopping_cost}')

