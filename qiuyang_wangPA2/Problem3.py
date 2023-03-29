#Qiuyang Wang
#COSI 10a, Spring 2022
#Programming Assignment #2

#define main function
def main():
	average_calculator()

#define the function to calculate the average
def average_calculator():
	num1 = int(input("Enter the first value: "))
	num2 = int(input("Enter the second value: "))
	num3 = int(input("Enter the third value: ")) #input all the three numbers and ready to calculate their average
	average = (num1 + num2 + num3) / 3 #basically calculate the average
	print("The average is:", average)

main()