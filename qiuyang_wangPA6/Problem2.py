# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that can repeat each character of a string several times based on the input of the user

#define the main function
def main():
    string_multiplier(input("Please enter a String: "), int(input("Please enter a multiplier for each character to repeat: ")))

#define the function to 
#requires two parameters, one is string value, the other is integer value
def string_multiplier(str_a, int_b):
    print("I got: ", end="")
    for character in str_a:                 #let each character in the string repeat inside this for loop
        print(character * int_b, end="")

main()
