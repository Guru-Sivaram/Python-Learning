from replit import clear
import art

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          }

#Retrieving items from a dictionary
print(programming_dictionary["Bug"])

#Adding new items
programming_dictionary["Loop"] = 'The action of doing something over and over again'

print(programming_dictionary)

#Loop through values
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Grading program excercise

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = 'Exceeds Expectations'
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = 'Acceptable'
    elif student_scores[key] <= 70:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting a dict in a dict
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total visits": 5}
}

print(travel_log)

#Nesting a dict in a list
travel_log = [
    {"country": "France",
     "Cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },

    {"country": "Germany",
     "Cities_visited": ["Berlin", "Hamburg", "Stuggart"],
     "total_visits": 12
    },
]

print(travel_log)

#Coding Excercise

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#Auction

# HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the secret auction program.")
userBid = True
peopleBids = {}


def HighestBidder(peopleBids):
    highestBid = 0
    winner = ''
    for bidder in peopleBids:
        if int(peopleBids[bidder]) > highestBid:
            highestBid = int(peopleBids[bidder])
            winner = bidder
    print(f"The winner is {winner} with a bid of {highestBid}")


while userBid == True:
    name = input("What is your name?: ")
    bidPrice = int(input("What's your bid?: "))
    moreBidders = input("Are there any other bidders? ")
    peopleBids[name] = bidPrice
    if moreBidders == "yes":
        clear()
    else:
        HighestBidder(peopleBids)
        userBid = False

