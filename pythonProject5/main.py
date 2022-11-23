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

    #if student_scores[scores + 1] > student_scores[scores]:
     #   highScore = student_scores[scores + 1]
