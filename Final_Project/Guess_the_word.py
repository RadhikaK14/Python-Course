word=list("hello")
ans=[]
length=len(word)
for i in range(length):
    ans.append("_")

print(' '.join(ans))

count = 0    
while ans != word:
    guess_letter = input("Enter a letter: ")
    if len(guess_letter) > 1:
        print('Error: You have entered more than 1 letter')
    else:
        count = count + 1
        if guess_letter in word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o
            for position,l in enumerate(word):
                if l == guess_letter:
                    ans[position]=guess_letter
    
    print(' '.join(ans))
print(f'No of attempts needed: {count}')