start_day = int(input('Please enter a starting day [Monday 1-7 Sunday]:'))
Num_of_days = int(input('Please enter number of days in the month [28-31] : '))

if start_day in range (1, 8) and Num_of_days in range(28, 32):

    print('Mo\tTu\tWe\tTh\tFr\tSa\tSu\n')

    i=1
    print('\t' * (start_day-1), i, end= '\t')
    for i in range(2, Num_of_days+1):
        if (i + start_day == 9):
            print('\n')
        print(i, end = '\t')
        if (i > 7) and ((i+ start_day-1) % 7) == 0:
            print('\n')
else:
    print('Please enter a valid number')


# for i in range(1, int(Num_of_days)+1):
#     print(i, end= '\t')
#     if i % 7 == 0:
#         print('\n')