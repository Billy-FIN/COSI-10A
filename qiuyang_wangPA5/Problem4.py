# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #5
#
# Description: This is the program that allows users input two people's birthday and compare which comes first with the result of remaining days until next birthday

#define the main function
def main():
    birthday_comparison(int(input("Please enter today's month in Arabic numerals (positive integer): ")), int(input("Please enter today's day in Arabic numerals (positive integer): ")))

#define the function to compare which birthday is sooner and hwo many days remain until next birthday
#require two positive integer parameter
def birthday_comparison(x, y):
#input birthdays
    person1_birthday_month = int(input("Please enter the first person's month of birthday in Arabic numerals (positive integer): "))
    person1_birthday_day = int(input("Please enter the first person's day of birthday in Arabic numerals (positive integer): "))
    person2_birthday_month = int(input("Please enter the second person's month of birthday in Arabic numerals (positive integer): "))
    person2_birthday_day = int(input("Please enter the second person's day of birthday in Arabic numerals (positive integer): "))
#calculate which day it is within 365 days of one year
    person1_birthday_days = operation(person1_birthday_month, person1_birthday_day)
    person2_birthday_days = operation(person2_birthday_month, person2_birthday_day)
    today_days = operation(x, y)
#calculate how many days remain until next birthday
    if person1_birthday_days - today_days >= 0:
        days_remain_1 = person1_birthday_days - today_days
    elif person1_birthday_days - today_days < 0:
        days_remain_1 = 365 - today_days + person1_birthday_days
    if person2_birthday_days - today_days >= 0:
        days_remain_2 = person2_birthday_days - today_days
    elif person2_birthday_days - today_days < 0:
        days_remain_2 = 365 - today_days + person2_birthday_days
    print("There are", days_remain_1, "days remain until the first person's birthday.")
    print("There are", days_remain_2, "days remain until the second person's birthday.")
#judge which birthday is sooner
    if days_remain_2 > days_remain_1:
        print("The first person's birthday is sooner.")
    elif days_remain_1 == days_remain_2:
        print("You guys' birthday is on the same day!")
    else:
        print("The second person's birthday is sooner.")

#define the function to calculate which day it is within 365 days in a year
def operation(a,b):
    days = 0
    for month in range(1, a):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:        #these months have 31 days each
            days += 31
        elif month == 2:    #February has 28 days
            days += 28
        else:               #other months have 30 days each
            days += 30
    return days + b


main()