# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #7
#
# Description: This is the program which can tell the user whether his or her input of list is sorted or not

#define the main function
def main():
    list1 = [1.5, 4.3, 7.0, 19.5, 25.1, 45.2]
    output(is_sorted(list1))

#define the function to judge the list is sorted or not
#requires a list of numbers as a parameter
#will return True or False
def is_sorted(a):
    count = 0
    #if the list only has one element, it is sorted
    if len(a) == 1:                  
        return True
    elif len(a) > 1:
        while count != len(a) - 1:
            #the condition is that every value in the list should be nondecreasing
            if a[count] <= a[count + 1]:      
                count += 1
            else:
                return False
        return True

#define the function to print a final message on the console to announce the user the result
#requires one boolen value as a parameter
def output(result):
    if result:
        print("It is sorted!")
    else:
        print("It is not sorted!")


main()