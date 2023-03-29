# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program can print the same output displayed in the question only by using nested for loops

#define the main function
def main():
    output3()

#define the function to print the output
def output3():
    for line in range(1,6):                 #it defines that there are five lines
        for asterisk in range(6-line):      #the amount of asterisks keeps decreasing respected to the decrement of line number
            print("*", end=" ")
        print()

main()