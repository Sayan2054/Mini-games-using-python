import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    player_choice = input("Choose rock, paper, or scissors: ")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("You win! Rock beats scissors.")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You win! Paper beats rock.")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You win! Scissors beat paper.")
    else:
        print("You lose! " + computer_choice.capitalize() + " beats " + player_choice + ".")

if __name__ == '__main__':
    play_game()
