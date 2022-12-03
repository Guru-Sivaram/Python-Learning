import math
import art

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.

def greet():
    print("Hello")
    print("My name is")
    print("Slim Shady")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print("Blank line")
    print("Third line")

greet_with_name("Guru")

def greet_with_name_location(name, location):
    print(f"Hello {name} you are from {location}")
    print("Blank line")
    print("Third line")


#Write your code below this line 👇

def paint_calc(height, width, cover):
    numberOfCans = (height * width) / cover
    print(math.ceil(numberOfCans))





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# Write your code below this line 👇

def prime_checker(number):

    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    if isPrime == True:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is not a Prime Number")





# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Does user want to go again. Press type yes or no\n")
    if result == "no":
        should_continue = False
        print("Goodbye")