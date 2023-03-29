# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #5
#
# Description: This is the program that makes the positive integer inputted by the user become 1 after some computations

#define the main function
def main():
    operation(int(input("Initial value is: ")))

#define the function to operate specific operations to make the input value become 1 and print the whole process
#requires one positive integer parameter
def operation(num):
    if num < 1:             #the input vlaue cannot less than 1
        print("Error!")
    else:
        for i in range(0, 200):
            if num == 1:          #the final result should be 1
                print("Final value ", num, ", number of operations performed ", i, sep="")
                return num
            elif num == 2:
                num = num // 2
            elif num % 2 == 0:      #specific computation that makes the value become 1
                num = num // 2
                print("Next value is:", num)
            else:
                num = num * 3 + 1
                print("Next value is:", num)


main()
