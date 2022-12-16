

"""
Functions with outputs
"""

def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #instead of printing the result below, we can return it to the function
    #print(f"{formatted_f_name} {formatted_l_name}")

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name(input("What is your first name? "), input("What is your last name? "))

print(formatted_string)

#Days in Month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print("Leap year.")
                return True
            else:
                #print("Not leap year.")
                return False
        else:
            #print("Leap year.")
            return True
    else:
        #print("Not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        return 29
    else:
        return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
