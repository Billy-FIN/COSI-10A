#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #2

#define main function
def main():
	calculate_change()

#define the function to calculate the change from the vending machine
def calculate_change():
	price = int(input("Enter price of item\n(from 25 cents to a dollar, in 5-cents increments): ")) #input the price
	totalchange = 100 - price #first calculate the change
	change_quarters = totalchange // 25 #then calculate how many quarters
	change_dimes = (totalchange - change_quarters * 25) // 10 #calculate how many dimes
	change_nickels = (totalchange - change_quarters * 25 - change_dimes * 10) // 5 #calculate how many nickels
	print("You bought an item for", price, "cents and gave me a dollar, so your change is:")
	print(change_quarters, "quarters,")
	print(change_dimes, "dimes,")
	print(change_nickels, "nickels")

main()