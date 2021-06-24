import random

def guess_word():
    my_list=['hello', 'python', 'testing', 'coding', 'variable', 'function', 'module']
    choice = random.randint(0, len(my_list)-1)
    word = my_list[choice]
    return word

#  Fetching the word and replacing it with '_ _ _ _'
def ans():
    ans=[]
    word = guess_word()
    length = len(word)
    for i in range(length):
        ans.append("_")
    print(' '.join(ans))
    return [ans, word]

def main():
    attempts = 0
    user_ans, word = ans()

    while (user_ans != list(word)) and (attempts < 5):
        guess_letter = input('Enter a letter or the word if you have guessed it:\n')

        if guess_letter == word:
            break

        elif guess_letter in word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(word):
                # This loop is useful if len(guess_letter) > 1 and is in the 'word'
                for i in list(guess_letter): 
                    if l == i:
                        user_ans[position]= i

        else:
            attempts = attempts + 1
            print('Error: Incorrect Input')
        
        print(' '.join(user_ans))

    if attempts >= 5:
        print('Sorry, better luck next time!')
    else:
        print('Yayy, u guessed it right!')

main()