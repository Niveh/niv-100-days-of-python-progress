import os
from day9_auction_art import logo


def clear():
    os.system("cls")


print(logo)

bids = {}
bid_ended = False


def get_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_price = bid_record[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder

    print(
        f"The bid has ended!\nThe winner is {winner} with a bid of {highest_bid}")


while not bid_ended:
    name = input("What is your name? ")
    bid = int(input("What is your bid price? "))
    bids[name] = bid

    bid_prompt = input(
        "Type \"yes\" if other users want to bid, otherwise anything else: ").lower()

    if bid_prompt != "yes":
        bid_ended = True
    else:
        clear()

get_highest_bidder(bids)
