MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
machine_on = True


# Function to handle money input
def money(user_coffee, cost):
    print(f"Cost of {user_coffee} is ${cost:.2f}")
    money_received = 0
    try:
        onedollar = int(input("How many $1 coins do you want to insert? "))
        money_received += 1.00 * onedollar

        fiftycent = int(input("How many 50 cent coins do you want to insert? "))
        money_received += 0.50 * fiftycent

        twentycent = int(input("How many 20 cent coins do you want to insert? "))
        money_received += 0.20 * twentycent

        tencent = int(input("How many 10 cent coins do you want to insert? "))
        money_received += 0.10 * tencent

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return money(user_coffee, cost)  # Restart money input in case of error

    return money_received


# Function to calculate and return change
def change(money_received, user_coffee_cost):
    global profit

    if money_received >= user_coffee_cost:
        profit += user_coffee_cost
        change = round(money_received - user_coffee_cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# Check if resources are sufficient
def sufficient_resources(ingredients_order):
    for item in ingredients_order:
        if ingredients_order[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True


# Deduct resources and serve coffee
def coffee_made(user_coffee, ingredient_order):
    for item in ingredient_order:
        resources[item] -= ingredient_order[item]
    print(f"Here's your {user_coffee}. Enjoy!")


# Get user input
def user_input():
    while True:
        user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_coffee in MENU.keys() or user_coffee in ['off', 'report']:
            return user_coffee
        else:
            print("Invalid option. Please choose either espresso, latte or cappuccino.")


# Main coffee machine logic
def coffee_machine():
    global machine_on

    while machine_on:
        user_coffee = user_input()

        if user_coffee == "off":
            machine_on = False
            print("Goodbye. See you again.")

        elif user_coffee == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Profit: ${profit}")

        else:
            drink = MENU[user_coffee]
            if sufficient_resources(drink['ingredients']):
                payment = money(user_coffee, drink["cost"])
                if change(payment, drink["cost"]):
                    coffee_made(user_coffee, drink['ingredients'])


# Start the coffee machine
coffee_machine()
