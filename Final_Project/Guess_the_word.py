import random
import json

# loading data from json file
def load_data():
    with open ('hangman_words.json') as file:
        data = json.load(file)
    return data

# choosing topic for the hangman game
def choose_topic():
    print('Choose a topic from below:')
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

# choosing a random word from the list
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

# logic to match the user's input with the word
def logic(user_ans, word):
    attempts = 0
    # loop for accepting user's input and checking it with the word. 
    while (user_ans != list(word)) and (attempts < 10):
        letter = input('Enter a letter or the word(if you have guessed it) : ')
        guess_letter = letter.lower()

        if guess_letter == word:
            break
                
        elif guess_letter in user_ans: # to check if user is repeating the letters
            attempts = attempts + 1
            attempts_remaining = 10 - attempts
            print(f'\033[2J')   # to clear the screen above
            print(hang_man[attempts])
            print(f"You have already entered '{guess_letter}'. Try a different one!")
            print(f'{attempts_remaining} attempts remaining.')

        elif guess_letter in word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(word):
                for i in list(guess_letter): # This loop is useful if len(guess_letter) > 1 and is in the 'word'
                    if l == i:
                        user_ans[position]= i
            print(f'\033[2J')

        else:
            attempts = attempts + 1
            attempts_remaining = 10 - attempts
            print(f'\033[2J')
            if(attempts<10):
                print(hang_man[attempts])
                print(f'Wrong! Try again. {attempts_remaining} attempts remaining.')
                
        print(' '.join(user_ans)) # join method returns a string 
    return attempts

def main():
    play_game = input('Are you ready to play Hangman? (y/n) : ')
        
    if play_game.lower() == 'y' or play_game.lower() == 'yes':
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
            print(f'\033[2J')
            print(hang_man[10])
        else:
            print(f'\033[2J')
            print(hang_man[11])
        print(f"Word is '{word}'")
    else:
        print('See you later, Bye!')
    

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