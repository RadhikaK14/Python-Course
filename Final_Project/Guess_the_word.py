import random

def guess_word():
    my_list=['hello', 'python', 'testing', 'coding', 'variable', 'function', 'module']
    choice = random.randint(0, len(my_list)-1)
    word = my_list[choice]
    return word
    # print(guess_word)

def ans():
    ans=[]
    word = guess_word()
    length = len(word)
    for i in range(length):
        ans.append("_")
    print(' '.join(ans))
    return ans

def main():
    attempts = 0
    user_ans = ans()
    word = guess_word()

    while (user_ans != list(word)) and (attempts < 5):
        guess_letter = input("Enter a letter: ")

        if (len(guess_letter) == 1) and (guess_letter in word):
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(word):
                if l == guess_letter:
                    user_ans[position]= guess_letter

        elif len(guess_letter) > 1:
            attempts = attempts + 1
            print('Error: You have entered more than 1 letter')
        
        else:
            attempts = attempts + 1
        
        print(' '.join(user_ans))

    if attempts >= 5:
        print('Sorry, better luck next time!')
    else:
        print('Yayy, u guessed it right!')

main()