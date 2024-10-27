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

import random

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[player_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])



  if player_choice == 2 and computer_choice == 0:
    print("You lose")
  elif player_choice == 0 and computer_choice == 2:
    print("You win")
  elif player_choice == computer_choice:
    print("It's a draw")
  elif player_choice < computer_choice:
    print("You lose")
  elif player_choice > computer_choice:
    print("You win")


# print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#   player_choice = int(input())

# if player_choice == 0:
#     print(rock)
# if player_choice == 1:
#     print(paper)
# if player_choice == 2:
#     print(scissors)

# print("Computer chose:")

# computer_choice = random.randint(0,2)
# if computer_choice == 0:
#     print(rock)
# if computer_choice == 1:
#       print(paper)
# if computer_choice == 2:
#       print(scissors)

# if player_choice == 0 and computer_choice == 0:
#     print("It's a draw")
# if player_choice == 0 and computer_choice == 1:
#     print("You lose")
# if player_choice == 0 and computer_choice == 2:
#     print("You win")

# if player_choice == 1 and computer_choice == 1:
#     print("It's a draw")
# if player_choice == 1 and computer_choice == 2:
#     print("You lose")
# if player_choice == 1 and computer_choice == 0:
#     print("You win")

# if player_choice == 2 and computer_choice == 2:
#     print("It's a draw")
# if player_choice == 2 and computer_choice == 0:
#     print("You lose")
# if player_choice == 2 and computer_choice == 1:
#     print("You win")