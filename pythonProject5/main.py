fruits = ["Apple", "Pear", "Orange"]

for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)

#Average Height

heights_string = input("Please enter all heights of students\n")
heights = heights_string.split(" ")
print(heights)
sumHeight = 0
counter = 0

for height in heights:
    sumHeight = sumHeight + int(height)
    print(sumHeight)
    counter += 1

avgHeight = round(sumHeight / counter)
print(counter)
print(f"Average height is {avgHeight}")



# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores \n").split(" ")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highScore = 0
for score in student_scores:
    if score > highScore:
        highScore = score
print(f"the highest score in the class is {highScore}")

print(max(student_scores))

    #if student_scores[scores + 1] > student_scores[scores]:
     #   highScore = student_scores[scores + 1]


#For Loop with range

for number in range(0, 10):
    print(number)

for number in range(0, 10, 2):
    print(number)


total2 = 0
for numba in range(0, 101):
    total2 += numba
print(total2)

# The sum of all even numbers from 0 to 100

sumEven = 0
for even in range(0, 101, 2):
    sumEven += even
print(sumEven)



#FizzBuzz, print 1 to 100, if divisible by 3 fizz, if divisble by 5 buzz, if divisible by both FizzBuzz

for fizzBuzz in range (1, 101):
    if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzBuzz % 3 == 0:
        print("Fizz")
    elif fizzBuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzBuzz)

#Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

unOrderedList = []
for letter in range(0, nr_letters):
    print(random.choice(letters), end="")
for symbol in range(0, nr_symbols):
    print(random.choice(symbols), end="")
for number in range(0, nr_numbers):
    print(random.choice(numbers), end="")

print("/n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for letter in range(0, nr_letters):
    unOrderedList.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    unOrderedList.append(random.choice(symbols))
for number in range(0, nr_numbers):
    unOrderedList.append(random.choice(numbers))

print(unOrderedList)
random.shuffle(unOrderedList)
print(unOrderedList)

for x in range(len(unOrderedList)):
    print(unOrderedList[x], end="")

#instead of making an empty list, you could've made an empty string and accomplished the same thing. Something to note :))
