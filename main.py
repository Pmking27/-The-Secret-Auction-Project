from replit import clear
from art import logo,bidding_finish,winner_of_bidding,continue_bidding
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:   
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
          highest_bid = bid_amount
          winner = bidder\
    
    clear()          
    print(winner_of_bidding)      
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name? = ")
  price = int(input("What is your bid? = $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'. = ")
  if should_continue == "no":
      bidding_finished = True
      print(bidding_finish)
      find_highest_bidder(bids)
  elif should_continue == "yes":
      clear()
      print(continue_bidding)
  else:
      print("Invalid Choice.")
      bidding_finished = True
      find_highest_bidder(bids)