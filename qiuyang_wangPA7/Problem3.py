# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #7
#
# Description: The is the program which can give the user a new list of integers with the sum of each pair of integers from the original list based on the user's input

#define the main function
def main():
    list1 = [1, 2, 3, 4, 5]
    collapse(list1)

#define the function to calculate the sum of each pair of integers and consititute a new list
#requires a list of integers as a parameter
def collapse(a):
    if len(a) == 0:
        print("Error!")
    else:
        #need to variables to represent the index of the pair of integers in the list
        pair_part1 = 0          
        pair_part2 = 1
        #create a new and empty list
        list2 = []             
        while pair_part2 <= len(a) - 1:
            insert_value = a[pair_part1] + a[pair_part2]
            #append the sum to the new list
            list2.append(insert_value)              
            pair_part1 += 2
            pair_part2 += 2
        #if the original list contains odd elements and cannot calculate the final pair, append the final element to the new list
        if pair_part2 == len(a):                 
            list2.append(a[len(a) - 1])
        print(list2)


main()