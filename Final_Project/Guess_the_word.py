import random
import json

def load_data():
    with open ('hangman_words.json') as file:
        data = json.load(file)
    return data

def choose_topic():
    print('Choose "word to guess" from the below topic :')
    choice = int(input('1.Easy \n2.Difficult\n3.Random words \n4.Animals \n5.Science/Sciences \n6.Sample data\n'))
    if choice == 1:
        topic = 'Easy'
    elif choice == 2:
        topic = 'Difficult'
    elif choice == 3:
        topic = 'Random'
    elif choice == 4:
        topic = 'Animals'
    elif choice == 5:
        topic = 'Science'
    elif choice == 6:
        topic = 'Sample'
    else:
        print('Invalid Input. Please try again')
        choose_topic()
    return topic

def guess_word(my_list):
    choice = random.randint(0, len(my_list)-1)
    word = my_list[choice]
    return word

#  Fetching the word and replacing it with '_ _ _ _'
def ans(word):
    ans=[]
    length = len(word)
    for i in range(length):
        ans.append("_")
    print(' '.join(ans))
    return ans

def logic(user_ans, word):
    attempts = 0
    while (user_ans != list(word)) and (attempts < 10):
        guess_letter = input('Enter a letter or the word(if you have guessed it) : ')

        if guess_letter == word:
            break
                
        elif guess_letter in user_ans:
            attempts = attempts + 1
            attempts_remaining = 10 - attempts
            print(f'\033[2J')
            print(hang_man[attempts])
            print(f"You have already entered '{guess_letter}'. Try a different one!")
            print(f'{attempts_remaining} attempts remaining.')

        elif guess_letter in word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(word):
                # This loop is useful if len(guess_letter) > 1 and is in the 'word'
                for i in list(guess_letter): 
                    if l == i:
                        user_ans[position]= i
            print(f'\033[2J')
            print(' '.join(user_ans))

        else:
            attempts = attempts + 1
            attempts_remaining = 10 - attempts
            print(f'\033[2J')
            if(attempts<10):
                print(hang_man[attempts])
                print(f'Wrong! Try again. {attempts_remaining} attempts remaining.')
                print(' '.join(user_ans))
        
    return attempts

def main():
    play_game = input('Are you ready to play Hangman? (y/n) : ')
    if play_game.lower() == 'n':
        print('See you later, Bye!')
    else:
        # first_name = input('Please enter your first name : ')
        # last_name = input('Enter your last name : ')
        # name = first_name.capitalize() + ' ' +last_name.capitalize()
        topic = choose_topic()
        quiz_words = load_data()
        # print(f'Hello {name}. Start guessing 🤔' )
        # score = []
        word = guess_word(quiz_words[topic])
        user_ans = ans(word)
        attempts = logic(user_ans, word)

        if attempts >= 10:
            print(hang_man[10])
            print(f"Word is '{word}'")
        else:
            print(hang_man[11])

hang_man= [
'''
      +
=========''',
'''
      +
      |
      |
      |
=========''',  
'''
      +
      |
      |
      |
      |
      |
=========''',
'''
    +-+
      |
      |
      |
      |
      |
=========''',
'''
  +---+
      |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  X   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
GAME OVER
 /|\  |
 / \  |
      |
=========''',
"""
  +---+
  |   |
      |
 \Q/  |
  |   |
 / \  |
=========
=YOU WIN=""",
]

main()