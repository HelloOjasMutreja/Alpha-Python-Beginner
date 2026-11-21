import random

options = ['rock', 'paper', 'scissors']

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    if player == 'rock':
        if computer == 'scissors':
            return "You chose Rock, Computer chose Scissors, You Win"
        elif computer == 'rock': 
            return "You chose Rock, Computer chose Rock, it's a Tie"
        else:
            return "You chose Paper, Computer chose Paper, Computer Wins"
    elif player == 'scissors':
        if computer == 'scissors':
            return "You chose Scissors, Computer chose Scissors, it's a Tie"
        elif computer == 'rock': 
            return "You chose Scissors, Computer chose Rock, Computer Wins"
        else:
            return "You chose Scissors, Computer chose Paper, You Win"
    else:
        if computer == 'scissors':
            return "You chose Paper, Computer chose Scissors, Computer Wins"
        elif computer == 'rock': 
            return "You chose Paper, Computer chose Rock, You Win"
        else:
            return "You chose Paper, Computer chose Paper, it's a Tie"

choices = get_choices()

print(check_win(choices["player"], choices["computer"]))