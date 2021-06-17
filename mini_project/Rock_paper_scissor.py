# user inputs
def user_input():
    choices = ['r','p','s']
    incorrect_user_input = True
    move = -1
    try:
        while incorrect_user_input:
            user_choice = input("Rock, Paper, or Scissors?[r/p/s]: ")
            if user_choice.lower().startswith('r'):
                incorrect_user_input = False
                move = 0
            elif user_choice.lower().startswith('p'):
                incorrect_user_input = False
                move = 1
            elif user_choice.lower().startswith('s'):
                incorrect_user_input = False
                move = 2
            else:
                print('incorrect input')
            if not incorrect_user_input:
                print(f"Your choice: {move}")
                return move
    except:
        return False

# computer input
def computer_choice():
    from random import randint
    ai_choice = randint(0,2)
    print(f'Computer choice : {ai_choice}')
    return ai_choice

# logic
def logic(user,computer):
    # first value: user ;; second value: computer
    # R P S
    score_matrix = {
        0:{0:  0   ,1: -1   ,2:  1  },
        1:{0:  1   ,1:  0   ,2: -1  },
        2:{0: -1   ,1:  1   ,2:  0  }
    }
    game_result = score_matrix[user][computer]
    return game_result

def main():
    # score
    score = 0
    final_score = 0
    # 3 games:
    for game_number in range(3):
        user = user_input()
        ai = computer_choice()
        score = logic(user,ai)
        final_score = final_score + score
        #Pretty-fying the game
        print()
        # This helps us print out whether we win/draw/lose the current game
        if score == 0:
            win_draw_lose = 'Draw'
        elif score == -1:
            win_draw_lose = 'Lose'
        elif score == 1:
            win_draw_lose = 'Win'
        print(f"Game number #{game_number+1} - Current score is: {score}")
        print()
        # This helps us write out in full the game move, words are better than numbers when displaying
        choice = ['Rock','Paper','Scissors']
        choice_emoji = ["🪨","📃","✂️"]
        print(f"{choice[user]} vs {choice[ai]} - {win_draw_lose}")
        print(f"\t{choice_emoji[user]} vs \t{choice_emoji[ai]} - {win_draw_lose}")
        print()
        print(f'Final Score : {final_score}')
        print('-'*41)
        #######################
    # This prints out a little delimiter to show that the game is over.        
    print("-="*20+'-')
    print()
    # This will write out the final statements depending on the final score
    if final_score > 0:
        print(f"You Win!")
    elif final_score < 0:
        print(f"You Lose!")
    else:
        print(f"You Drew (Draw? Drawn?.. Anyway.. You didn't win or lose.. )")
# This starts the game
main()