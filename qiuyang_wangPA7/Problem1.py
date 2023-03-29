# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #7
#
# Description: This is the program that can allow the user to play a game and end it if he wants. The computer will random select a number, the user needs to guess that value.
#              The console will tell the user whether the guess is higher or lower. At the end of this game, an overall statistics will be provided.

import random
MAXIMUM = 100

#define the main function
def main():
    game()

#define the function to start this game and keep the game running as the user wants, and ouput the statistics at the end of the game
def game():
    #introduction
    print("Do you want to play a game? The computer will choose an integer from 1 to", MAXIMUM, "inclusively. And you will need to guess this integer correctly.")
    print("When you guess incorrectly, the computer will tell you whether this integer is higher or lower than your previous guess.")
    print()
    #the first time to play
    delta_guess = playing_process()
    guess_count = delta_guess
    best_game = delta_guess
    game_count = 1
    user_input = input("Do you want to play again? ")
    #users can decide to continue or end the game
    while user_input.startswith("y") or user_input.startswith("Y"):
        print()
        delta_guess = playing_process()
        user_input = input("Do you want to play again? ")
        game_count += 1
        guess_count += delta_guess
        #if the guesses are smaller than best_game, update best_game with it
        if delta_guess < best_game:
            best_game = delta_guess
    print()
    #when the user wants to end this game, then print the overall statistics
    overall_stats(game_count, guess_count, best_game)

#define the function to tell the user whether his or her guess is higher or lower than the computer number - play one game function
def playing_process():
    print("I'm thinking of a number between 1 and", MAXIMUM, "...")
    computer_num = random.randint(1, MAXIMUM)
    user_guess = int(input("Your guess? "))
    count = 1
    while user_guess != computer_num:
        #compare the guess with the computer number and tell the user whether it is higher or lower
        if user_guess > computer_num:
            print("It is higher.")
            count += 1
            user_guess = int(input("Your guess? "))
        elif user_guess < computer_num:
            print("It is lower.")
            count += 1
            user_guess = int(input("Your guess? "))
    #a special case for guessing correctly for the first try
    if count == 1:
        print("You got it right in 1 guess!")
    else:
        print("You got it right in", count, "guesses!")
    return count

#define the function to output the statistics
#requires three integer values as parameters
def overall_stats(a, b, c):
    print("Overall results:")
    print("Total games:", a)
    print("Total guesses:", b)
    print("Guesses/game:", round(b/a, 1))
    print("Best game:", c)


main()