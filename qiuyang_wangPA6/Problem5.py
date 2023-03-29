# Qiuyang Wang
# COSI 10a, Spring 2022
# Programming Assignment #6
#
# Description: This is the program that can encode the Caesar Cipher message

#define the main function
def main():
    caesar_cipher(input("Please enter a string message: "), int(input("How many times you want to rotate each letter: ")))

#define the function to rotate every character in the message several times based on the user's input
#requires two parameters, one is string value, the other is integer value
def caesar_cipher(str, int_num):
    if int_num > 26 or int_num < -26:       #rotating over 26 or minus 26 times is meaningless
        print("Error!")
        return False
    else: 
        for character in str:
            if ord("a") <= ord(character) <= ord("z"):          #lowercase condition
                value = ord(character) + int_num
                if value > ord("z"):                            #when the value is over or below the range of a~z
                    value -= 26
                elif value < ord("a"):
                    value += 26
            elif ord("A") <= ord(character) <= ord("Z"):        #uppercase condition
                value = ord(character) + int_num
                if value > ord("Z"):                            #when the value is over or below the range of A~Z
                    value -= 26
                elif value < ord("A"):
                    value += 26
            print(chr(value), end="")

main()