# Option 1 - Quiz game
questions=[{"question":"What is the capital of Germany? ",
            "answer":"Berlin"}] 
score=0
for question in questions:
    player_ans=input(question['question'])
    if player_ans.lower()==(question['answer']).lower():
        print('Correct!')
        score+=1
    else:
        print('Incorrect')
print(f"Your score was {score}")