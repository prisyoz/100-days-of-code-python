import random
import day12_art

# Global variable for the generated number
number = 0


# Generate a number
def number_generator():
    global number
    number = random.randint(1, 101)


# Function to handle user input for replay
def replay_game():
    while True:
        replay_again = input("Would you like to play again? Y/N \n").upper()

        if replay_again == "Y":
            print("\n" * 5)
            number_generator()  # Generate a new number
            welcome_message()  # Start a new game
            break  # Exit the loop to start a new game
        elif replay_again == "N":
            print("Thank you and Goodbye.")
            break  # Exit the loop and end the game
        else:
            print("Invalid option. Please type Y or N.\n")  # Loop until valid input


# Function to handle the guessing logic (easy and hard modes share similar logic)
def guess_number(remaining_tries, mode):
    global number
    is_game_over = False

    while not is_game_over:
        try:
            user_number = int(input("Guess a number.\n"))

            if user_number < number:
                remaining_tries -= 1
                print("Too low.")
                print(f"You have {remaining_tries} tries left.")
            elif user_number > number:
                remaining_tries -= 1
                print("Too high.")
                print(f"You have {remaining_tries} tries left.")
            else:
                print(f"The number is {number}!")
                guess_attempts = mode - remaining_tries + 1
                print(f"You got it in {guess_attempts} tries. Great job!")
                is_game_over = True

            if remaining_tries == 0 and not is_game_over:
                is_game_over = True
                print("You lose.")
                print(f"The number is {number}")

            if is_game_over:
                replay_game()  # Call replay after the game ends

        except ValueError:
            print("Not a valid number. Please guess a number.")


# Easy mode
def easy_try():
    remaining_tries = 10  # Number of tries for easy mode
    guess_number(remaining_tries, 10)  # Call the shared guess function


# Hard mode
def hard_try():
    remaining_tries = 5  # Number of tries for hard mode
    guess_number(remaining_tries, 5)  # Call the shared guess function


def welcome_message():
    print(day12_art.logo)
    print("Welcome to Guess The Number.\nNumber ranges from 1-100.")

    while True:
        try:
            user_mode = int(input("Pick 1 for Easy and 2 for Hard.\n"))

            if user_mode == 1:
                easy_try()  # Start the easy mode game
                break  # End the loop after the game finishes
            elif user_mode == 2:
                hard_try()  # Start the hard mode game
                break  # End the loop after the game finishes
            else:
                print("Invalid input. Please enter a number (1 for Easy, 2 for Hard.)")
        except ValueError:
            print("Invalid input. Please enter a number (1 for Easy, 2 for Hard.)")


# Start the game
number_generator()  # Generate a random number to start the game
welcome_message()    # Show the welcome message and start the game
