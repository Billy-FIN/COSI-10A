# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that makes the positive integer inputted by the user become 1 after some computations

# define the main function
def main():
    operation(int(input("Initial value is: ")))

#define the function to operate specific operations to make the input value become 1 and print the whole process
#requires one positive integer parameter
def operation(num):
    count = 0
    if num < 1:
        print("Error!")
    else:
        while num != 1:                 #when num == 1, quit the while loop
            count += 1
            if num == 2:
                num = num // 2
            elif num % 2 == 0:          #specific computation that makes the value become 1
                num = num // 2
                print("Next value is:", num)
            else:
                num = num * 3 + 1
                print("Next value is:", num)
        print("Final value ", num, ", number of operations performed ", count, sep="")


main()
