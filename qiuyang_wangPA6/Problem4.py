# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that can output user's name followed the pig latin rules

#define the main function
def main():
    pig_latin(input("Enter your first name: "), input("Enter your last name: "))

#define the main function to output the new name of user under the pig latin rules
#requires two string values
def pig_latin(first, last):
#convert into lowercase
    first = first.lower()
    last = last.lower()
#convert first name into pig latin
    first_middle = first[2 : len(first)]
    first_tail =  first[0] + "ay"
    first_head_incomplete = first[1]
    first_head = first_head_incomplete.upper()
#convert last name into pig latin
    last_middle = last[2 : len(last)]
    last_tail = last[0] + "ay"
    last_head_incomplete = last[1]
    last_head = last_head_incomplete.upper()
#intergration
    pig_latin_first = first_head + first_middle + first_tail
    pig_latin_last = last_head + last_middle + last_tail
    pig_latin_full_name = pig_latin_first + " " + pig_latin_last
    print(pig_latin_full_name)


main()