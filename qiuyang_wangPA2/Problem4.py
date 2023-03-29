#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #2

#define main function
def main():
	cookie_ingredients()

#define the function to calculate the cookie ingredients
def cookie_ingredients():
	amount_cookie = int(input("Please enter the amount of cookies you want to make: ")) #input how many cookies the object wants to make
	sugar = int(1.5 / 48 * amount_cookie * 100) / 100
	butter = int(1.0 / 48 * amount_cookie * 100) / 100
	flour = int(2.75 / 48 * amount_cookie * 100) / 100 #calculate and display the result with two decimals places
	print("You need:")
	print(sugar, "cups of sugar")
	print(butter, "cups of butter")
	print(flour, "cups of flour")

main()