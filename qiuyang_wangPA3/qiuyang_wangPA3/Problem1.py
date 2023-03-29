#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #3
#
#Description: This is a program that can calculate and print the result of 2^0 up to 2^n based on the input of n by users

#define the main function
def main():
    exponent_calculator()

#define the function to calculate 2^0 up to 2^n and then print the results
def exponent_calculator():
    for n in range(1 + int(input("Enter a number for exponent: "))):        #enable the program operates n+1 times to calculate 2^0 up to 2^n inclusively
        print(2**n)     #calculate 2 to the power of i

main()