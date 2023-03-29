# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program asks users for two integer inputs and print a number of sequence, starting from the minimum to the maximum in the first line
#             and next-higher number in the next line

#define the main function
def main():
    number_sequence_generator()

#define the function to ask for two integer inputs and pass them as parameters to the other function
def number_sequence_generator():
    minimum = int(input("Please enter a minimum integer: "))
    maximum = int(input("Please enter a maximum integer: "))
    number_sequence(minimum, maximum)

#define the function to print the square of lines of increasing numbers
def number_sequence(a, b):
    for line in range(b - a + 1):       #it defines how many lines are needed
        for i in range(a + line, b + 1):        #this part will print the numbers before the maximum, inclusively
            print(i, end="")
        for k in range(line):           #this part will print the numbers after the maximum
                print(a + k, end="")
        print()

main()
