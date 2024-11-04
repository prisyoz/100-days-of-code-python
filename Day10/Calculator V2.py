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
def calculator():
    should_accumulate = True
    
    # Program asks user to type in first number. 
    
    while True:
        try:
            first_number = float(input("Please enter the first number.\n"))
            break
        except ValueError:
            print("Please enter numbers only.")
    
      
    while should_accumulate:
          # Program ask user to type in mathematical operator
        while True:
                math_operator = input("Please choose a mathematical operator. + - * / \n")
                
                if math_operator in ["+", "-", "*", "/"]:
                    break
                else:
                    print("Please only type + - * /.")
        
        # Program asks user to type in second number
        
        while True:
            try:
                second_number = float(input("Please enter the second number.\n"))
                break
            except ValueError:
                print("Please enter numbers only.")
        
        # Program works out the result based on chosen math operator
        
        results = operations[math_operator](first_number, second_number)
        
        print(f"The result of {first_number}{math_operator}{second_number} is {results}\n")
        
        
        # Program asks if user wants to continue working with previous results
        # If yes, program loops to use the previous result as the first number then repeats calculation process.
        # If no, program wipes all memory of previous calculations and restarts calcuation process
        
        while True:
            continue_calculation = input("Do you want to continue calculating? Y/N\n").lower()
            if continue_calculation in ["y", "n"]:
                break
            else:
                print("Invalid option. Please type Y or N.\n")
                
        if continue_calculation == "y":
            
            first_number = results
            
        else:
            
            should_accumulate = False
            
            print('\n' * 20)
            print("Starting a new calculation...\n")
            calculator()

calculator()  
