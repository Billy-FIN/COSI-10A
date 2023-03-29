# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #4
#
#Description: This program can calculate the compound amount for users accumulated the number of years that they want to save for
#             and create a table with the necessary index for users' saving, such as interest, current balance, new balance, etc.

#define the main function
def main():
    compound_amount()

#define the function to calculate and create a table for shwoing users' accumulated money after n years based on their input
def compound_amount():
    years = int(input("For how many years do you want to save?"))
    curr_balance = 1000
    new_deposit = 100.0
#print the header of the table
    print("Year", "Curr Balance", "Interest", "New Deposit", "New Balance", sep="\t")
#calculate the accumulated money and other index
    for i in range(years):
        interest = int(curr_balance * 0.0065 * 100) / 100
        new_balance = int((curr_balance + interest + new_deposit) * 100) / 100          #both will display two digits
        print(i, "     ", curr_balance, end="\t\t")
        print(interest, new_deposit, new_balance, sep="\t\t")       #print the result and make the table seem good
        curr_balance  = new_balance         #let curr_balance equal to new_balance and ready to calculate interest of next year

main()

