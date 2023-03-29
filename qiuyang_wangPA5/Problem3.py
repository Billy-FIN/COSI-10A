# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #5
#
# Description: This is the program that can converse Arabic numerals into Roman numerals (less than 4999)

#define the main function
def main():
    romen_numerals_convertor(int(input("Please enter a positive integer that is less than 4999: ")))

#define the function to converse into Roman numerals
def romen_numerals_convertor(num):
    thousand = num // 1000
    hundred = num % 1000 // 100
    ten = num % 100 // 10
    one = num % 10 // 1
#print the thousands numeral
    print("M" * thousand, end="")
#print the hundreds numeral
    if hundred == 9:
        print("CM", end="")
    elif hundred == 4:
        print("CD", end="")
    elif hundred >= 5:
        print("D" + "C" * (hundred - 5), end="")
    else:
        print("C" * hundred, end="")
#print the tens numeral
    if ten == 9:
        print("XC", end="")
    elif ten == 4:
        print("XL", end="")
    elif ten >= 5:
        print("L" + "X" * (ten - 5), end="")
    else:
        print("X" * ten, end="")
#print the units numeral
    if one == 9:
        print("IX", end="")
    elif one == 4:
        print("IV", end="")
    elif one >= 5:
        print("V" + "I" * (one - 5), end="")
    else:
        print("I" * one, end="")


main()