# converting string to list
ques = 'question'
print(list(ques))

# Function to find and print the largest sum in the list
my_list = [[5,3,2], [1,3,2,1], [3,2,4], [10,1,5], [6,7,5]]
new_list =[]
my_dict = {}

def find_sum(list):
    sum=0
    max_sum =0
    for i in list:
        sum = sum_list(i)
        new_list.append(sum)
        my_dict[sum] = i
    max_sum = max(new_list)
    print(f'The list with the largest sum is {my_dict[max_sum]}, sum = {max_sum}')

def sum_list(num):
    sum=0
    for i in num:
        sum = sum+i
    return sum

find_sum(my_list)

# dict with shopping list and its price
item_price = {'apple': 0.50,
                "banana" : 0.10,
                "mango" : 1.20,
                "pasta" : 0.75,
                "bread" : 1.00,
                "milk" : 0.80,
                "lettuce" : 0.90,
                "egg" : 0.15,
                "chicken" : 2.10 }

my_shopping = {'apple': 6,
                'mango': 2,
                'bread' : 8,
                'egg': 5,
                'chicken': 2}

def calculate_price(shopping, price):
    item_price = 0
    sum = 0
    for list, qty in shopping.items():
        if list in price.keys():
            cost = price[list]
            item_price = qty * cost
            sum = sum + item_price
    return sum

my_bill = calculate_price(my_shopping, item_price)
print(f'The total cost of my grocery is : {my_bill}')

# user inputs the qty of shopping
my_list = {}
for i in item_price.keys():
    shopping_list = input(f'Please enter the qty required for {i} : ')
    if shopping_list is '':
        shopping_list = 0
    my_list[i] = int(shopping_list)

print(my_list)
bill = calculate_price(my_list, item_price)
print(f'Your shopping will cost : {bill}')