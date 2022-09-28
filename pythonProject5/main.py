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
