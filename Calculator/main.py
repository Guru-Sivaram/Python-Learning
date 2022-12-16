import art

#Calculator
print(art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mult(n1, n2):
    return n1 * n2

Operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    nextNum = True
    num1 = float(input("What's the first number?: "))
    while nextNum == True:
        for symbol in Operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        answer = Operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        nextAnswer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to to start a new calculation.: ")

        if nextAnswer == 'y':
            nextNum = True
            num1 = answer
        else:
            nextNum = False
            calculator()

calculator()



# function = Operations["+"]
# function(2,3)