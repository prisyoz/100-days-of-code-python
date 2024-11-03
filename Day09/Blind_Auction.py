import art
print(art.logo)

# Welcome users to blind auction
print("Welcome to the secret auction.")

# Ask for their name
name = input("Please enter your name.\n")

# Ask for their bid.
bid = input("Please enter your bid.\n")

# Store the name and bids into a dictionary.
bid_store = {}
bid_overall = {}

bid_store[name] = bid
bid_overall = bid_store


# Ask if there are more users. if yes, repeat. if no, print the highest bidder name and bid.


new_user = True
bid_name = []
bid_amount = 0

more_users = input("Are there more users placing bids? Y/N\n").upper()

while new_user == True:
  if more_users == "Y":
    new_user = True
    print('\n' * 100)
    # Ask for their name
    name = input("Please enter your name.\n")

    # Ask for their bid.
    bid = input("Please enter your bid.\n")

    # Store the name and bids into a dictionary.

    bid_store[name] = bid
    bid_overall = bid_store
    
    more_users = input("Are there more users placing bids? Y/N\n").upper()
  else: 

    # Looping through dictionary to find the higgest bidder
    # for each name in the list. check the amount. 
    # if the next amount is higher, use that amount. if not, remain the previous name. 

    for bidder, amount in bid_overall.items():
      if amount > str(bid_amount):
        bid_name = bid_overall[bidder]
        
print(bid_name)
