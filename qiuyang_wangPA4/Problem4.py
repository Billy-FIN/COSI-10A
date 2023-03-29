# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program can print the same output displayed in the question only by using nested for loops

#define the main function
def main():
    output4()

#define the function to print the same output
def output4():
    for line in range(1,6):             #it shows how many lines needed
        for space in range(5-line):     #it shows how many space needed in each line
            print(" ", end=" ")
        for asterisk in range(line):    #it shows how many "*" needed in each line
            print("*", end=" ")
        print()

main()