import random
import art
import os
print(art.logo)
# play = input("Do you want to play game of Blackjack?(y/n): ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function to generate card


def generate_card():
    generated_card = random.choice(cards)
    return generated_card


def restart_game():
    print(art.logo)


# start of the game
users_card = [generate_card(), generate_card()]
print(f"    Your cards: {users_card}, current score = {sum(users_card)}")
computers_card = [generate_card()]
print(f"    Computers first card: {computers_card[0]}")

# getting new card for user if user request for it and can change value of Ace if required


def get_users_card():
    users_card.append(generate_card())
    if 11 in users_card and sum(users_card) >= 21:
        x = users_card.index(11)
        users_card[x] = 1
    print(f"    Your cards: {users_card}, current score = {sum(users_card)}")
    print(f"    Computers first card: {computers_card[0]}")


get_card = True

# loop to keep game running till required
while get_card:
    answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    users_card_total = sum(users_card)
    if answer == "n":
        get_card = False
        while users_card_total > sum(computers_card):
            computers_card.append(generate_card())
            computers_card_total = sum(computers_card)
        if computers_card_total <= 21 and computers_card_total > users_card_total:
            print(
                f"You lose! Your cards: {users_card} your count: {sum(users_card)} \n\tComputers card: {computers_card} count: {sum(computers_card)}"
            )
        elif computers_card == users_card_total:
            print(
                f"Its a draw!! \n\t Your Cards: {users_card} \n\t Comp Cards: {computers_card}")
        else:
            print(
                f"You Win! Your cards: {users_card} your count: {sum(users_card)} \n\tComputers card: {computers_card} count: {sum(computers_card)}"
            )
    elif answer == "y":
        get_users_card()
        if sum(users_card) > 21:
            print(
                f"You lose! Your cards: {users_card} your count: {sum(users_card)}"
            )
            get_card = False
        elif sum(users_card) == 21:
            print(
                f"Black Jack!!!!!!! Your cards: {users_card} your count: {sum(users_card)}"
            )
            get_card = False
    if get_card == False:       
        play_again = input("want to play again?(y/n): ").lower()

        if play_again == "y":
            os.system('cls')
            users_card.clear()
            computers_card.clear()
            users_card = [generate_card(), generate_card()]
            print(
                f"    Your cards: {users_card}, current score = {sum(users_card)}")
            computers_card = [generate_card()]
            print(f"    Computers first card: {computers_card[0]}")
            get_card = True
        else:
            exit()
