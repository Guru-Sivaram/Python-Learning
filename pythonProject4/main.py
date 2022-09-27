# Split string method

import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = len(names)
print(x)

n = random.randint(0, x)

print("This human will have to pay for the bill\n" + names[n])


