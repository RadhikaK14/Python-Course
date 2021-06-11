# Creating list
my_list = ['Amy', 1, 'Beth', 'Charlie', 6, 'Daisy', 7, 2]
print(my_list)

# Replacing Beth with Sandy
my_list[2]= 'Sandy'
print(my_list)

# for i in my_list:
#     print(i)

# Multiply int by itself. Ex: 6 becomes 36
for i in my_list:
    if type(i) == int:
        # print(my_list.index(i))
        # print(i*i)
        my_list[my_list.index(i)]= i*i
print(my_list)   

# count num of integers over 5
count = 0
for i in my_list:
    if type(i) == int and i > 5:
        count+= 1
print(f'count: {count}')