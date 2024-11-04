def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Program asks user to type in first number. 

first_number = int(input("Please enter the first number.\n"))

# Program ask user to type in mathematical operator

math_operator = input("Please choose a mathematical operator. + - * / \n")

# Program asks user to type in second number

second_number = int(input("Please enter the second number.\n"))

# Program works out the result based on chosen mathe operator

if math_operator == "+":
    results = operations["+"](n1=first_number, n2=second_number)
elif math_operator == "-":
    results = operations["-"](n1=first_number, n2=second_number)
elif math_operator == "*":
    results = operations["*"](n1=first_number, n2=second_number)
else:
    results = operations["/"](n1=first_number, n2=second_number)

print(f"The result of {first_number}{math_operator}{second_number} is {results}\n")


# Program asks if user wants to continue working with previous results
# If yes, program loops to use the previous result as the first number then repeats calculation process.
# If no, program wipes all memory of previous calculations and restarts calcuation process

continue_math = True
continue_calculation = input("Do you want to continue calculating? Y/N\n").lower()

while True:
    if continue_calculation == "y":
        continue_math = True

        math_operator = input("Please choose a mathematical operator. + - * / \n")
        second_number = int(input("Please enter the second number.\n"))

        if math_operator == "+":
            results = operations["+"](n1=results, n2=second_number)
        elif math_operator == "-":
            results = operations["-"](n1=results, n2=second_number)
        elif math_operator == "*":
            results = operations["*"](n1=results, n2=second_number)
        else:
            results = operations["/"](n1=results, n2=second_number)

        print(f"The result of {results}{math_operator}{second_number} is {results}\n")

        continue_calculation = input("Do you want to continue calculating? Y/N\n").lower()

    else:
        continue_math = False

        first_number = int(input("Please enter the first number.\n"))
        math_operator = input("Please choose a mathematical operator. + - * / \n")
        second_number = int(input("Please enter the second number.\n"))

        if math_operator == "+":
            results = operations["+"](n1=first_number, n2=second_number)
        elif math_operator == "-":
            results = operations["-"](n1=first_number, n2=second_number)
        elif math_operator == "*":
            results = operations["*"](n1=first_number, n2=second_number)
        else:
            results = operations["/"](n1=first_number, n2=second_number)

        print(f"The result of {first_number}{math_operator}{second_number} is {results}\n")

        continue_calculation = input("Do you want to continue calculating? Y/N\n").lower()


