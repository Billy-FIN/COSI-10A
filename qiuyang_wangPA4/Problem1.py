# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program calculates and prints the first 12 Fibonacci numbers

#define the main function and use the patameter
def main():
    fibonacci(12)

#define the function to calculate and print any Fibonacci numbers in one line
def fibonacci(k):
    a = 1
    b = 1       #set the first and second Fibonacci numbers as 1
    print("The first 12 Fibonacci numbers are:", a, b, end=" ")
    for i in range(k - 2):
        c = a + b
        a = b       #pass the value to the next one
        b = c
        print(b, end=" ")

main()
