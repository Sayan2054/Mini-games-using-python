import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    position = 0
    while True:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("You rolled a", dice_roll)
        position += dice_roll
        if position > 100:
            position = 100
        print("You are now at position", position)
        if position == 100:
            print("Congratulations, you won!")
            break
        if position == 25:
            print("You landed on a snake! Moving back to position 5.")
            position = 5
        elif position == 55:
            print("You landed on a snake! Moving back to position 20.")
            position = 20
        elif position == 75:
            print("You landed on a snake! Moving back to position 50.")
            position = 50
        elif position == 10:
            print("You landed on a ladder! Moving up to position 30.")
            position = 30
        elif position == 45:
            print("You landed on a ladder! Moving up to position 65.")
            position = 65
        elif position == 80:
            print("You landed on a ladder! Moving up to position 95.")
            position = 95

if __name__ == '__main__':
    play_game()
