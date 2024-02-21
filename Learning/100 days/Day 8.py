# 1st exercise (multifunctional function)
import math
wall_h = int(input())
wall_l = int(input())
coverage = 5
def paint_calc (height, widht, cover):
    number = (height*widht)/cover
    rounded = math.ceil(number)
    print (rounded)
paint_calc (height=wall_h, widht=wall_l, cover=coverage)

#2nd exercise
n = int(input())
def prime_checker(number):
    is_prime= True
    for i in range(2,number):
        if number % i == 0:
            is_prime= False
    if is_prime:
        print(f"{number} is prime!")
    else:
        print(f"{number} is not prime!")
prime_checker(number=n)

# Final exercise
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'enconde' or 'decode':\n")
text = input("Inser your text:\n").lower()
shift = int(input("Set number of shifts:\n"))

def encode (msg, shift, direction):
    txt = ""
    if direction == "encode":
        for i in msg:
            if i not in alphabet:
                txt += i
            else:
                index = alphabet.index(i) + shift
                while index > 26:
                    index = index - 26
                new_i = alphabet[index]
                txt += new_i
        print(f"Encoded message is: {txt}")
    elif direction == "decode":
        for i in msg:
            if i not in alphabet:
                txt += i
            else:
                index = alphabet.index(i) - shift
                while index < 0:
                    index = index + 26
                new_i = alphabet[index]
                txt += new_i
        print(f"Decoded message is: {txt}")


encode (msg= text, shift= shift, direction= direction )

again = input("Do you wanna do it again? 'yes' or 'no'")
if again == "yes":
    direction = input("Type 'enconde' or 'decode':\n")
    text = input("Inser your text:\n").lower()
    shift = int(input("Set number of shifts:\n"))
    encode (msg= text, shift= shift, direction= direction )
else:
    print("Goodbye!")


