import math

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

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


    for i in range(2, number):
        if number % i == 0:
            print(f"{number} This is not a prime number")
            break
    else:
        print("This is a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


