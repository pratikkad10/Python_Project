import random

def get_choices():
    player_choice=input("Enter a choice (stone,paper,scissor :) ")
    options=["stone", "paper", "scissor"]
    computer_choice=random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices
             
def check_win(player, computer):
    print("you chose " + player , "computer chose " + computer )
    if player=="stone" and computer=="paper":
        return "You Win!"
    elif player=="paper" and computer=="scissor":
        return "You Lose!"
    elif player=="scissor" and computer=="stone":
        return "You Lose!"
    elif player=="stone" and computer=="scissor":
        return "You Win!"
    elif player=="paper" and computer=="stone":
        return "You Win!"
    elif player=="scissor" and computer=="paper":
        return "You Win!"
    elif player=="paper" and computer=="scissor":
        return "You Lose!"
    elif player=="scissor" and computer=="stone":
        return "You Lose!"
    elif player=="stone" and computer=="paper":
        return "You Win!"
    elif player=="paper" and computer=="scissor":
        return "You Lose!"
    elif player=="scissor" and computer=="stone":
        return "You Lose!"
    elif player==computer:
        return "Tie!"
    
choices=get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)