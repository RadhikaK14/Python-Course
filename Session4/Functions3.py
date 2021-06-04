def my_maths_function(num1, num2, opr):
    if opr.lower() == 'add':
        print(num1 + num2)
    elif opr.lower() == 'subtract':
        print(num1 - num2)
    elif opr.lower() == 'multiply':
        print(num1 * num2)
    elif opr.lower() == 'divide':
        print(num1 / num2)
    else:
        print('Invalid operation entered')

my_maths_function(10, 4, 'add')