# starting_day = input('Please enter a starting day [Monday 1-7 Sunday]:')
Num_of_days = input('Please enter number of days in the month [28-31] : ')

print('Mo\tTu\tWe\tTh\tFr\tSa\tSu\n')

for i in range(1, int(Num_of_days)+1):
    print(i, end= '\t')
    if i % 7 == 0:
        print('\n')
    


