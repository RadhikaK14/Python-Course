# Reading txt file
with open('groceries.txt','r') as file:
    file_contents=file.read()
    print(file_contents)

# Reading first line of the txt file
with open('groceries.txt','r') as file:
    file_contents=file.readline()
    print(file_contents)

# Reading txt file and printing each line with capitalised first letter
with open('groceries.txt','r') as file:
    file_contents=file.readlines()
    for i in file_contents:
        print(i.capitalize())

with open('groceries.txt','r') as file:
    file_contents=file.readlines()
    Num = 1
    for i in file_contents:
        print(f'{Num}. {i.capitalize()}')
        Num = Num + 1