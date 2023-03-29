# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #5
#
# Description: This is a program which allows user to input some numbers and then output the smallest and largest number

#define the main function
def main():
    number_comparison(int(input("How many numbers do you want to enter? ")))

#define the function to print the largest and smallest number based on what the user has inputted
#requires one integer parameter
def number_comparison(num):
    large = 0
    small = 0       #set the initial value as 0
    for i in range(1, num + 1):
        num = int(input("Number " + str(i) + ": "))
        if num >= large:        #compare the input number whether is bigger than the largest
            large = num
        elif num <= small:      #compare the input number whether is less than the smallest
            small = num
    print("Smallest =", small)
    print("Largest =", large)


main()
