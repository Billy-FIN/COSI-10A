# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program will ask the users to input two integers and print from n^0 to n^i inclusively

#define the main function
def main():
    power_generator()

#define the function to calculate and print power of the base inclusively from base^0
def power_generator():
    base = int(input("Please enter an integer indicating the base: "))
    for i in range(1 + int(input("Please enter a positive integer indicating the exponent: "))):        #enable the for loop to operate inclusively
        print(base ** i, end=" ")           #calculate the result and print

main()
