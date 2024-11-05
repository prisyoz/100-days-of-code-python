import random
from Day11_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deals random card to computer and user

def draw_cards():
  return int(random.choice(cards))

# Blackjack calculation

def cards_blackjack(user_cards, computer_cards):
  if sum(user_cards) == 21 and len(user_cards) == 2:
    print("BLACKJACK. YOU WIN!\n")
    return True
  elif sum(computer_cards) == 21 and len(computer_cards) == 2:
    print("COMPUTER BLACKJACK. YOU LOSE!\n")
    return True
  else:
    return False

# Adjust ace value from 11 to 1 if total exceeds 21
def ace_adjust(cards):
  while 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)


# Reveals user's 2 card. 
# Reveals computer 1 card

def blackjack():

  user_cards = []
  computer_cards = []

  # First draw of cards
  user_cards.append(draw_cards())
  computer_cards.append(draw_cards())

  # Second draw of cards
  user_cards.append(draw_cards())
  computer_cards.append(draw_cards())

  # Reveal both user cards and 1 card of computer

  print(f"Your cards: {user_cards}")
  print(f"Computer cards: [{computer_cards[0]}, '?']")

  # check if anyone has a blackjack

  if cards_blackjack(user_cards, computer_cards):
    # Ask if user wants to play again
    play_again = input("Would you like to play again? Y/N \n").upper()
    if play_again == "Y":
      blackjack()
    else:
      print("Thank you and Goodbye.")
      return

  # Ask if user would want to continue dealing

  continue_dealing = input("Would you like to deal another card? Y/N\n").lower()

  computer_less = True
  user_less = True
  sum_computer_cards = 0
  sum_user_cards = 0

  # If yes, deal one more card

  while user_less == True:
    if continue_dealing == "y":

      user_cards.append(draw_cards())
      print(f"Your cards: {user_cards}")
      print(f"Computer cards: [{computer_cards[0]}, '?']")
      continue_dealing = input("Would you like to deal another card? Y/N\n").lower()
    else:
      # If computer cards < 17, deal another card for computer
      # If no, check if computer is below 17 and needs another card. 
      user_less = False


  while computer_less == True:
    if sum(computer_cards) < 17:
        print("Computer will deal a card.")
        computer_cards.append(draw_cards())

    else:
      computer_less == False
      print("Calculating in progress...\n")
      break

  # Calculate the sum of computer cards

  sum_computer_cards = sum(computer_cards)

  # Calculate the sum of user cards

  sum_user_cards = sum(user_cards)

  # Adjust aces if needed
  ace_adjust(user_cards)
  ace_adjust(computer_cards)

  # If both no need card, then check if which of the carrds is bigger.
  # If user is bigger, user win. otherwise computer win.
  # If both same amount or burst, it's a draw.

  if sum_user_cards < 16:
    print("Your card is lesser than 16. You lose.")
  elif sum_user_cards > 21:
    print("You bust. You lose.")
  elif sum_computer_cards == sum_user_cards == 21:
    print("Both 21 dots. It's a draw.")
  elif sum_computer_cards == 21:
    print("Computer 21 dots. You lose.")
  elif sum_user_cards == 21:
    print("21 dots. You win.")
  elif sum_user_cards < sum_computer_cards and sum_computer_cards < 21:
    print("You lose.")
  elif sum_computer_cards > 21 and sum_user_cards < 21:
    print("Computer bust. You win.")
  elif sum_computer_cards == sum_user_cards:
    print("It's a draw.")
  else:
    print("You win.") 

  print(computer_cards)

# Welcome message - ask if user wants to play a game of Blackjack

print(logo)
welcome_message = input("Welcome to a game of 21 dots. Are you ready for a game? Y/N \n").upper()

if welcome_message == "Y":
  blackjack()


  print("\n" * 2)

  replay = True
  
  while replay:
    play_again = input("Would you like to play again? Y/N \n").upper()

    if play_again == "Y":
      print("\n" * 5)
      blackjack()
    
    else:
      replay = False
      print("Thank you and Goodbye.")
      exit()
else:
  print("Thank you and Goodbye.")
  exit()
