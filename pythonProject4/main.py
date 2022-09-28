# Split string method

import random
names_string = input("Give me everybody's names, separated by a comma.\n")
print(names_string)
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = len(names)
print(x)

n = random.randint(0, x)

print("This human will have to pay for the bill\n" + names[n])


# You can combine lists together into making a larger list with dirty_dozen = [fruits, vegetables]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])