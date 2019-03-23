"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game(high_score):
    num_answer = random.randrange(1,10)
    attempt = 1
    accepted_range = (1,10)

    welcome_note = "Welcome to the Number Guessing Game!"
    s = len(welcome_note)
    print("-"*s)
    print(welcome_note)
    print("-"*s)

    print("The HIGHSCORE is {} tries. Can you do fewer tries than this? Let's see!".format(high_score))


    while True:

        guess = input("Pick a number between 1 and 10: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Input should be a valid number. Please try again.")
            continue
        if guess < accepted_range[0] or guess > accepted_range[1]:
            print("Out of range. Input should be 1-10.")
            continue
        else:
            if guess == num_answer:
                 print("\nYou got it! It took you {} tries.".format(attempt))
                 if attempt < high_score:
                    high_score = attempt
                 break
            elif guess < num_answer:
                print("It is higher!")
                attempt+=1
                continue
            elif guess > num_answer:
                print("It is lower!")
                attempt+=1
                continue

    print("Thanks for playing")
    play_again = input("Would you like to play again? [y]es or [n]o: ")
    if play_again.lower() == "yes" or play_again.lower() == 'y':
        start_game(high_score)
    else:
        print("Closing game! See you next time!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game(10)
