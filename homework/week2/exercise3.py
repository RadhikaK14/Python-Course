def adding_num():
    output = 0
    while True:
        num = input("Enter a number to add (hit enter if you don't want to add more numbers):")
        if num == '':
            break
        else:
            output = output + float(num)
    print(f'Sum of numbers: {output}')
    

adding_num()

# def number_adder():
#     sum = 0
#     while True:
#         number_to_add = input("Enter a number to add (hit enter if you don't want to add any more numbers): ")
#         if number_to_add == "":
#             break
#         else:
#             sum = sum + float(number_to_add)
#     print(sum)
    
# number_adder()