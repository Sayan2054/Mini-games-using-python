import random

def play_game():
    number = random.randint(1, 100)
    guesses = 0
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        guesses += 1
        if guess == number:
            print("Congratulations, you guessed the number in", guesses, "guesses!")
            break
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

if __name__ == '__main__':
    play_game()
