import art
import game_data as data
import random
import os


data = data.data

OptionA = ""
OptionB = ""


def get_data():
    number = random.randint(0, len(data))
    return data[number]


def option_A_assign():
    global OptionA
    if (OptionA == ""):
        OptionA = get_data()
    elif(OptionB != ""):
        OptionA = OptionB


def print_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}a {description} from {country}"


def option_B_assign():
    global OptionB
    OptionB = get_data()


def compare_options(guess):
    if(OptionA["follower_count"] > OptionB["follower_count"]):
        if (guess == "b"):
            return True
    else:
        if (guess == "a"):
            return True


def game():
    game_over = False
    score = 0
    while not game_over:
        print(art.logo)
        option_A_assign()
        option_B_assign()
        print(f"OPTION A : {print_info(OptionA)}")
        print(art.vs)
        print(f"OPTION B : {print_info(OptionB)}")
        print(f"Current Score: {score}")
        guess = input(
            "Who has more followers on Instagram?(a or b):  ").lower()
        game_over = compare_options(guess)
        os.system('cls')
        print(
            f"OPTION A: {OptionA['name']} has {OptionA['follower_count']} \n OPTION B: {OptionB['name']} has {OptionB['follower_count']} followers")
        score += 1
    print(f"Sorry you lost game over! Your score: {score}")


game()
