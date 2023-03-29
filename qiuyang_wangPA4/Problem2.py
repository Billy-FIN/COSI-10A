# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program can print the same output displayed in the question only by using nested for loops

#define the main function
def main():
    output()

#define the function to print the output
def output():
    for line in range(1,6):                 #it defines that there are 5 lines in this output
        for asterisk in range(line):        #the pattern shows that the amount of asterisks equals to the line number
            print("*", end=" ")
        print()

main()