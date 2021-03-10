import os
import art
bidders = {}
print(art.logo)
print("Welcome to the blind auction!!!")
continue_bid = True
while continue_bid:
    name = input("what is your name?   ")
    bid = int(input("How much bid amount?   $"))
    bidders[name] = bid
    response = input("Is there any other bidder?(Y/N):   ").lower()
    if response == "n" or response != "y":
        continue_bid = False
    else:
        os.system('cls')

highest_amount = 0
highest_bidder = ""
for people in bidders:
    if bidders[people] > highest_amount:
        highest_amount = bidders[people]
        highest_bidder = people


print(f"The winner is {highest_bidder} with {highest_amount}$ bid")
