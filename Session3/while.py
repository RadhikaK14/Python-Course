#3a
counter = 0
total_sum = 0

while counter <=100:
    total_sum = total_sum + counter
    counter = counter +1

print(f'The sum of all numbers between 1 and 100 is {total_sum}')

#3b
counter = 1
total_sum = 0

while counter <=500:
    if counter % 3 == 0:
        total_sum = total_sum + counter
    counter = counter + 1

print(f'The sum of all numbers between 1 and 500 which are multiples of 3 is {total_sum}')