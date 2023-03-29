#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #3
#
#Description: This is a program that can print the same output descibed in Problem 3

#define the main function
def main():
    pattern_output()

#define the function to print the output
def pattern_output():
    for line in range(1, 7):        #enable the program to operate 6 times because the output has 6 lines
        for asterisk in range(6 - line):        #print the first part of asterisk for each line
            print("*", end="")
        for space in range(line):       #print the first part of space
            print(" ", end="")
        for slash in range(12 - 2 * line):          #print slash for each line
            print("/", end="")
        for backslash in range(10 - 12 + 2 * line):         #print backslash for each line
            print("\\", end="")
        for space in range(line):       #print the second part of space
            print(" ", end="")
        for asterisk in range(6 - line):        #print the second part of asterisk for each line
            print("*", end="")
        print()

main()