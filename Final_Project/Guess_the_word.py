import random

word=['hello', 'python', 'testing', 'coding', 'variable', 'function', 'module']
word_count= len(word)
choice = random.randint(0, word_count-1)
guess_word = word[choice]
# print(choice)
# print(guess_word)
ans=[]
length = len(guess_word)
for i in range(length):
    ans.append("_")

print(' '.join(ans))

attempts = 0    
while (ans != list(guess_word)) and (attempts < 5):
    guess_letter = input("Enter a letter: ")
    if len(guess_letter) > 1:
        print('Error: You have entered more than 1 letter')
        attempts = attempts + 1
    else:
        if guess_letter in guess_word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(guess_word):
                if l == guess_letter:
                    ans[position]= guess_letter
        else:
            attempts = attempts + 1
    
    print(' '.join(ans))

if attempts >= 5:
    print('Sorry, better luck next time!')
else:
    print('Yayy, u guessed it right!')