#1a
def print_name(name):
    print(f'Hello {name}')

print_name("Radhika")
print_name(123)
print_name(True)

#1b
def check_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

num1 = 40
is_even = check_even(num1)
print(f'Is {num1} even : {is_even}')