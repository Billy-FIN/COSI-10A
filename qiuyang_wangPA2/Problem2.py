#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #2

#define main function
def main():
	mile_km_conversion()

#define the function to converse miles into km
def mile_km_conversion():
	miles = float(input("Enter a length in miles: ")) #input the numbers of miles that object wants to converse
	km = int(miles * 1.609344 * 100) / 100 #converse and display the result with two decimals places
	print(miles, "miles is,", km, "kilometers")

main()