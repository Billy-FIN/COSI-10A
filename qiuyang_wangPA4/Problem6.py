# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: this program uses a constant value HEIGHT, which is equal to 4, to print the figure

#define a constant value
HEIGHT = 4

#define the main function and uses a parameter
def main():
    output6(HEIGHT)

#define the function to print the figure of height 4
def output6(a):
    for line in range(1, a + 1):        #it defines how many lines are needed
        for slash in range(2 * (line - 1)):
            print("\\", end="")
        for exclaimation_mark in range(-4 * line + HEIGHT * 4 + 2):         #it shows the relation between HEIGHT and line and amount of "!"
            print("!", end="")
        for backslash in range(2 * (line - 1)):
            print("/", end="")
        print()    

main()

