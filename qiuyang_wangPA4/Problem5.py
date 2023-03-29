# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program can print the same output displayed in the question by using for loops and string multiplication

#define the main function
def main():
    output5()

#define the function to print the same output
def output5():
    for line in range(6):       #it defines how many lines in this output
        print("\\" * 2 * line, end="")
        print("!" * (- 4 * line + 22), end="")
        print("/" * 2 * line)       #it uses string multiplication to print the structure after calculating the relation between lines and "!" "/" "\\"
                
main()