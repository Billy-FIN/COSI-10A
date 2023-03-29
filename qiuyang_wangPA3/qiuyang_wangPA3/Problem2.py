#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #3
#
#Description: This is a program that can calculate and print the result of the factorial of three positive integer n based on the input of n by users

#define the main function
def main():
    factorial_calculator()

#define the function to calculate n! and then print the results
def factorial_calculator():
    for i in range(0,3):        #make users input integer n for three times
        n = int(input("Enter a number: "))
        result = 1      #set the initial value of result as 1
        for j in range(1, 1 + n):
            result *= j     #enable the program calculate n!
        print(n, end="")        #print the results
        print("! =", result)

main()