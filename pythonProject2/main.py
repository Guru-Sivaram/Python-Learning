num_char = len(input("What is your name\n"))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = 123
print(type(a))

a = float(123)
print(type(a))

# Coding Excercise 2, Adding the digits of a 2 digit number together

print("\n")

number = (input("Please type in a 2 digit number \n"))
print(float(number[0]) + float(number[1]))

print(6//4) # Double Slash is converting to into automatically
print(round(6/4)) # This is rounding numbers. By putting a comma, you can choose to what place

# f strings in python allow the machine to do all the formatting for you
score = 20
print(f"your score is {score}\n")


age = input("Please type in your current age \n")
print(f"Assuming you will live until 90 years old, you have {(90 * 365) - (int(age)*365)} days left, {(90 * 12) - (int(age)*12) } months left, and {(90 * 52) - (int(age)*52)} weeks left \n")

# The tip calculator

print("Welcome to the tip calculator\n")
bill = input("What was the total bill?\n")
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
split = input("how many people to split the bill\n")
print(f"total bill is {(float(bill) * ((100+int(tipPercentage)) / 100))}\n")

perPerson = ((float(bill) * ((100+int(tipPercentage)) / 100)) / int(split))

finalAmount = "{:.2f}".format(perPerson)
print(f"Each person should pay {finalAmount}")







