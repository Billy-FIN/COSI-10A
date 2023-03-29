#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #3
#
#Description: This is a program that can print a mitrix of rows * columns based on the input by users

#define the main function
def main():
    matrix()

#define the function to print the matrix
def matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for line in range(1, 1 + rows):         #enable the program to operate enough times to produce enough rows
        for i in range(0, columns):         #ensure the matrix will have enough columns
            print(rows * i + line, end="\t")          #calculate and print the numbers of each row which will also form into an arithmetic sequence
        print()       #to seperate lines

main()