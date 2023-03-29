# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that operate Rock Paper Scissor game for users.

#import module random
import random

#define the main function
def main():
    console_log(input("Please enter \"Hard\" or \"Normal\" to start this game: "))

#define the function to choose which game mode should operate
#requires one specific string parameter
def console_log(a):
    if a == "Hard":
        hard()
    elif a == "Normal":
        normal()

#define the hard mode. The computer will trace user's decisions and recognize his or her tendency to make next decision
def hard():
    print("Welcome to the Rock Paper Scissor game hard mode!")
    response = int(input("Please enter your decision, 1 for Rock, 2 for Paper, 3 for Scissor (or enter 0 to end and quit this game): "))
    count = 0
    rock = 0
    paper = 0
    scissor = 0
    while response != 0:
        count += 1
        if response == 1:
            output_user_response = "Rock"       #start tracing
            rock += 1
        elif response == 2:
            output_user_response = "Paper"
            paper += 1
        elif response == 3:
            output_user_response = "Scissor"
            scissor += 1
        print("You chose: " + output_user_response)


        if rock / count >= 0.6:             #the threshold is 60%
            computer_response = 2
        elif paper / count >= 0.6:
            computer_response = 3
        elif scissor / count >= 0.6:
            computer_response = 1
        else:
            computer_response = random.randint(1, 3)        #if it does not reach the threshold, computer will random select and keep tracing
        if computer_response == 1:
            output_computer_response = "Rock"
        elif computer_response == 2:
            output_computer_response = "Paper"
        elif computer_response == 3:
            output_computer_response = "Scissor"
        print("Computer chose: " + output_computer_response)
        print()

        if response == computer_response:               #output the game result based on the rules
            print("Oh that's a tie!")
        elif response == 1:
            if computer_response == 2:
                print("You lose!")
            elif computer_response == 3:
                print("You win!")
        elif response == 2:
            if computer_response == 3:
                print("You lose!")
            elif computer_response == 1:
                print("You win!")
        elif response == 3:
            if computer_response == 1:
                print("You lose!")
            elif computer_response == 2:
                print("You win!")
        print()
        response = int(input("Please enter your decision, 1 for Rock, 2 for Paper, 3 for Scissor (or enter 0 to end this game): "))
    print("Thank you for playing my game.")

#define the normal mode. Computer will do the random selection
def normal():
    print("Welcome to the Rock Paper Scissor game normal mode!")
    response = int(input("Please enter your decision, 1 for Rock, 2 for Paper, 3 for Scissor (or enter 0 to end and quit this game): "))
    while response != 0:
        if response == 1:
            output_user_response = "Rock"
        elif response == 2:
            output_user_response = "Paper"
        elif response == 3:
            output_user_response = "Scissor"
        print("You chose: " + output_user_response)
        computer_response = random.randint(1, 3)                #random selection
        if computer_response == 1:
            output_computer_response = "Rock"
        elif computer_response == 2:
            output_computer_response = "Paper"
        elif computer_response == 3:
            output_computer_response = "Scissor"
        print("Computer chose: " + output_computer_response)
        print()

        if response == computer_response:                       #output the game result based on the rules
            print("Oh that's a tie!")
        elif response == 1:
            if computer_response == 2:
                print("You lose!")
            elif computer_response == 3:
                print("You win!")
        elif response == 2:
            if computer_response == 3:
                print("You lose!")
            elif computer_response == 1:
                print("You win!")
        elif response == 3:
            if computer_response == 1:
                print("You lose!")
            elif computer_response == 2:
                print("You win!")
        print()
        response = int(input("Please enter your decision, 1 for Rock, 2 for Paper, 3 for Scissor (or enter 0 to end this game): "))
    print("Thank you for playing my game.")


main()