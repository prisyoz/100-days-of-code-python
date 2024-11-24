import random
import day12_art

# Global variable
number = 0
easy_mode = 10
hard_mode = 5

# Generate a number
def number_generator():
    global number
    number = random.randint(1, 101)

# replay function
def replay_game():
    while True:
        replay_again = input("Would you like to play again? Y/N \n").upper()

        if replay_again in ["Y", "N"]:
            if replay_again == "Y":
                print("\n" * 5)
                number_generator()
                welcome_message()
                break
            else:
                print("Thank you and Goodbye.")
        break
    else:
        print("Invalid option. Please type Y or N.\n")

# Easy try
def easy_try():
    is_game_over = False
    global easy_mode

    # number of tries for easy mode
    remaining_tries = 10

    # user guessing
    while not is_game_over:
        try:
            user_number = int(input("Guess a number.\n"))

            if user_number < number:
                remaining_tries -= 1
                print("Too low.")
                print(f"You have {remaining_tries} times left.")
            elif user_number > number:
                remaining_tries -= 1
                print("Too high.")
                print(f"You have {remaining_tries} times left.")
            else:
                print(f"The number is {number}!")
                guess_attempts = easy_mode - remaining_tries + 1
                print(f"You got it in {guess_attempts} times. Great job!")
                is_game_over = True

            if remaining_tries == 0 and not is_game_over:
                is_game_over = True
                print(f"You lose.")
                print(f"The number is {number}")

            if is_game_over:
                replay_game()

        except ValueError:
            print("Not a valid number. Please guess a number.")

# Hard try
def hard_try():
    is_game_over = False
    global hard_mode

    # number of tries for hard mode
    remaining_tries = 5

    # user guessing
    while not is_game_over:
        try:
            user_number = int(input("Guess a number.\n"))

            if user_number < number:
                remaining_tries -= 1
                print("Too low.")
                print(f"You have {remaining_tries} times left.")
            elif user_number > number:
                remaining_tries -= 1
                print("Too high.")
                print(f"You have {remaining_tries} times left.")
            else:
                print(f"The number is {number}!")
                guess_attempts = hard_mode - remaining_tries + 1
                print(f"You got it in {guess_attempts} times. Great job!")
                is_game_over = True

            if remaining_tries == 0 and not is_game_over:
                is_game_over = True
                print("You lose.")
                print(f"The number is {number}")

            # call for replay function after game ends
            if is_game_over:
                replay_game()

        except ValueError:
            print("Not a valid number. Please guess a number.")


def welcome_message():
    print(day12_art.logo)
    print("Welcome to Guess The Number.\nNumber ranges from 1-100.")
    
    while True:
        try:
            user_mode = int(input("Pick 1 for Easy and 2 for Hard.\n"))

            if user_mode == 1:
                easy_try()
                break
            elif user_mode == 2:
                hard_try()
                break
            else:
                print("Invalid input. Please enter a number (1 for Easy, 2 for Hard.)")
        except ValueError:
            print("Invalid input. Please enter a number (1 for Easy, 2 for Hard.)")




number_generator()
welcome_message()


