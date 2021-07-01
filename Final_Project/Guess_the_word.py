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
    return ans, length

# logic to match the user's input with the word
def logic(user_ans, guess_word):
    attempts = 0
    count = 0 # to calculate score
    user_input = [] # to display user's input
    # loop for accepting user's input and checking it with the word. 
    while (''.join(user_ans) != guess_word) and (attempts < 10):
        letter = input('Enter a letter or the word(if you have guessed it) : ')
        guess_letter = letter.lower()
        word = guess_word.lower()

        if guess_letter in word:
            # enumerate function assigns each letter with an index. Ex: enumerate['h','e','l','l','o']= (0 h, 1 e, 2 l, 3 l, 4 o)
            for position,l in enumerate(word):
                for i in list(guess_letter): # This loop is useful if len(guess_letter) > 1 and is in the 'word'
                    if l == i:
                        user_ans[position]= i
                        count += 1
            print(f'\033[2J') # clears above screen

        else:
            attempts = attempts + 1
            attempts_remaining = 10 - attempts
            print(f'\033[2J')
            if guess_letter in user_input:
                print(f"You have already entered '{guess_letter}'. Try a different one!")
            else:
                print('Wrong! Try again.')
            if(attempts<10):
                print(f'{attempts_remaining} attempts remaining.')
                print(hang_man[attempts])
        
        user_input.append(letter)
        print(f'You have entered : {user_input}\n')       
        print(' '.join(user_ans)) # join method returns a string 
    return attempts, count

# assigning scores and a message to print
def scoring(word_count, len_word):

    if word_count == len_word:
        user_score = 20
        message = 'High score. Well done!'
    elif word_count >= (0.75 * len_word):
        user_score = 15
        message = 'Good score. Keep trying!'
    elif word_count >= (0.5 * len_word):
        user_score = 10
        message = 'You can do better!'
    elif word_count >= (0.25 * len_word):
        user_score = 5
        message = 'Low score, try again!'
    else:
        user_score = 0
        message = 'Sorry, Better luck next time!'
    
    return user_score, message

def main():
    play = True
    quiz_words = load_data()
    while(play == True):
        play_game = input('Do you want to play Hangman? (y/n) : ')
            
        if play_game.lower() == 'y' or play_game.lower() == 'yes':
           
            topic = choose_topic()
            print(quiz_words[topic])
            word = guess_word(quiz_words[topic])
            user_ans, length_word = ans(word)
            attempts, userword_count = logic(user_ans, word)

            if attempts >= 10:
                print(f'\033[2J')
                print(hang_man[10])
            else:
                print(f'\033[2J')
                print(hang_man[11])
                userword_count = length_word

            print(f"Word is '{word}'")

            score, message = scoring(userword_count, length_word)
            print(f'Your score is : {score} - {message}')

            for val in quiz_words.values(): # to delete guess word from dict
                if (word in val):
                    val.remove(word)

        else:
            play = False
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