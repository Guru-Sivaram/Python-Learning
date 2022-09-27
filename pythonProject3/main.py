import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

"""
myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
compChoice = random.randint(0, 2)
print("You chose")

if myChoice == 0:
    print(rock)
    if compChoice == 0:
        print("Computer Chose\n" + rock)
        print("Tie")
    elif compChoice == 1:
        print("Computer Chose\n" + paper)
        print("You Lose")
    elif compChoice == 2:
        print("Computer Chose\n" + scissors)
        print("You Win")
elif myChoice == 1:
    print(paper)
    if compChoice == 0:
        print("Computer Chose\n" + rock)
        print("You Win")
    elif compChoice == 1:
        print("Computer Chose\n" + paper)
        print("Tie")
    elif compChoice == 2:
        print("Computer Chose\n" + scissors)
        print("You Lose")
elif myChoice == 2:
    print(scissors)
    if compChoice == 0:
        print("Computer Chose\n" + rock)
        print("You Lose")
    elif compChoice == 1:
        print("Computer Chose\n" + paper)
        print("You Win")
    elif compChoice == 2:
        print("Computer Chose\n" + scissors)
        print("Tie")
"""

# new rock paper scissors
gameImages = [rock, paper, scissors]
myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
compChoice = random.randint(0, 2)
print(f"You chose {myChoice}\n" + gameImages[myChoice])
print(f"Computer chose {compChoice}\n" + gameImages[myChoice])


if myChoice == compChoice:
    print("Tie!")
elif myChoice == 0 and compChoice == 1:
    print("You Lose!")
elif myChoice == 0 and compChoice == 2:
    print("You Win!")
elif myChoice == 1 and compChoice == 0:
    print("You Win!")
elif myChoice == 1 and compChoice == 2:
    print("You Lose!")
elif myChoice == 2 and compChoice == 0:
    print("You Lose!")
elif myChoice == 2 and compChoice == 1:
    print("You Win!")





