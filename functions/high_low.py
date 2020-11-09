import random

# a game called "High Low"

# rules:
# - the computer generates a random number
# - the program then asks the user to enter a guess
# - if the number guessed is higher than the computer's
# - the output will display "Go Lower"
# - if the number guessed is lower than the computer's
# - the output will display "Go Higher"
# - the user has 10 guesses to guess correctly
# - in order to win the game

MAX_NUMBERS = {"level 1": 100, "level 2": 1000, "level 3": 1000000}


def generate_secret(start=1, end=MAX_NUMBERS["level 1"], level=1):
    if level != 1:
        key = "level " + str(level)
        end = MAX_NUMBERS[key]
    return random.randint(start, end)


def check_guess(guess, secret):
    if guess > secret:
        return "Go Lower"
    elif guess < secret:
        return "Go Higher"
    else:
        return "You Guessed It!"


MAX_GUESSES = 10

difficulty_level = 1

want_to_play = True
while want_to_play:
    number_guesses = MAX_GUESSES
    secret_number = generate_secret(level=difficulty_level)

    guess_input = 0
    while number_guesses > 0 and guess_input != secret_number:
        guess_input = int(input("Guess my number: "))
        number_guesses -= 1

        result = check_guess(guess_input, secret_number)
        print(result)

    if number_guesses == 0 and guess_input != secret_number:
        print("You ran out of guesses and LOST!")
    else:
        if difficulty_level < 3:
            difficulty_level += 1
        else:
            print("You win the game!!")

    while True:
        play_again = input("Do you want to play again (Y/N)? ").upper()
        if play_again in ["Y","N"]:
            break
        else:
            print("You didn't type a Y or N...")

    want_to_play = (play_again == "Y")
