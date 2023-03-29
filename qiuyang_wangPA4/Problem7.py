# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program will calculate and print [ 1 ] to [ n ] based on the number n that users input

#define the main function
def main():
    output7()

#define the function to print numbers from 1 to n with square brackets inclusively
def output7():
    end_number = int(input("Please enter a positive integer: "))
    for i in range(1, end_number + 1):          #enables the for loop to also print [ n ] inclusively
        print("[", i, "]", end=" ")

main()