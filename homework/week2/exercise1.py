#1a
for i in range (0,11):
    if(i%3==0):
        continue
    print(i)

#1b
def print_nums():
    for i in range (11):
        if(i%3==0):
            continue
        print(i)

print_nums()

#1c
def print_nums(max):
    for i in range (max+1):
        if(i%3==0):
            continue
        print(i)

print_nums(32)