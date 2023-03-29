# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that can tell whether the string is a palindrome

#define the main function
def main():
    output(validation(input("Please enter a string to see if it is a palindrome: ")))

#define the function to judge if the string is a palindrome and return a boolen value
#requires one string parameter
def validation(str):
    str_new = str.lower()
    count = 0     
    while str_new[count] == str_new[len(str_new) - 1 - count]:          #when respective values are not equal, quit the while loop
        if count == len(str_new) - 1:
            return True
        count += 1
    return False

#define the function to output the result after receiving the boolen value
def output(a):
    if a:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")

main()
        
