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

#print("This human will have to pay for the bill\n" + names[n])


# You can combine lists together into making a larger list with dirty_dozen = [fruits, vegetables]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])

#reverse a string

s = 'GuruSivaram'
s1 = ''

for c in s:
    s1 = c + s1
print(s1)

#reverse an array

arr = [1,2,3,4]

for i in range(len(arr) - 1,-1,-1):
    print(arr[i])