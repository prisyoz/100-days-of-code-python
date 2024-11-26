from game_data import data
from art import logo, vs
import random
import os

# clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# get a random profile
def profile():
    selected_profile = random.choice(data)
    name = selected_profile['name']
    follower = selected_profile['follower_count']
    describe = selected_profile['description']
    country = selected_profile['country']
    comparison = (f"{name}, a {describe}, from {country}")
    return comparison, follower

# comparing profiles
def high_low():
    # Set first profiles
    profile_a, followers_a = profile()
    profile_b, followers_b = profile()
    
    # Make sure no overlap profile
    while followers_a == followers_b:
        profile_b, followers_b = profile()

    score = 0
    game_on = True

    while game_on:
        clear()
        print(logo)

        if score > 0:
            print(f"Correct! Your current score is: {score}.")

        # print 2 comparisons

        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")


        # Check if correct
        while True:
             # Get user's guess
            guess = input("Who do you think has more followers? A or B ").upper()
            
            if guess in ['A', 'B']:
                break
            else:
                print("Invalid input. Please only type A or B.")

        if guess == 'A' and followers_a > followers_b:
            score += 1
            profile_b, followers_b = profile()
        elif guess == 'B' and followers_b > followers_a:
            score += 1
            profile_a, followers_a = profile()
        else:
            print(f"Incorrect, your final score is {score}")
            game_on = False


                

    # for replay
    while True:
        play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
        
        if play_again == 'Y':
            high_low()
        elif play_again == 'N':
            print('Goodbye!')
            exit()
        else:
            print("Invalid input. Please type 'Y' or 'N'. ")

# Start game
high_low()