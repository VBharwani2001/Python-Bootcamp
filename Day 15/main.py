import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def generate_report():
    return f"Water : {resources['water']}ml,\nMilk : {resources['milk']}ml,\nCoffee : {resources['coffee']}g,\nMoney : ${resources['money']}"


def update_resources(coffee):
    global resources
    resources["water"] = resources["water"] - \
        MENU[coffee]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - \
        MENU[coffee]["ingredients"]["coffee"]
    resources["money"] = resources["money"] + MENU[coffee]["cost"]
    # return generate_report()


def calculate_and_update_change(quater, dimes, nickel, penny, coffee):
    total_money_paid = (quater * 0.25) + (dimes * 0.10) + \
        (nickel * 0.05) + (penny * 0.01)
    total_money_paid = round(total_money_paid, 2)
    coffee_price = MENU[coffee]["cost"]
    if(total_money_paid < coffee_price):
        return "Insufficient money inserted. Your money is returned to you"
    elif(total_money_paid > coffee_price):
        difference = total_money_paid - coffee_price
        difference = round(difference, 2)
        update_resources(coffee)
        return f"You paid {total_money_paid}$. Here is your {coffee} and change: {difference}$ \n!!!!!!Have a great day!!!!!\n-----------Next Customer-----------"


def check_resource_sufficient(coffee):
    water_check = resources["water"] - MENU[coffee]["ingredients"]["water"]
    milk_check = resources["milk"] - MENU[coffee]["ingredients"]["milk"]
    coffee_check = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    response = ""
    if(water_check < 0):
        response += "Water not sufficient\n"
    if(milk_check < 0):
        response += "Milk not suffiecient \n"
    if(coffee_check < 0):
        response += "Coffee not suffiecient\n"
    return response


def coffee_machine():
    user_response = input(
        "What would you like? (espresso/latte/cappuccino):").lower()
    if(user_response == "report"):
        print(generate_report())
    elif(user_response == "off"):
        print("Have a great day! ")
        exit()
    else:
        check = check_resource_sufficient(user_response)
        if(check == ""):
            # anything
            print("Please insert coins")
            get_quater = int(input("How many quaters?  "))
            get_dimes = int(input("How many dimes?  "))
            get_nickel = int(input("How many nickels? "))
            get_penny = int(input("How many pennys? "))
            cal_update = calculate_and_update_change(
                get_quater, get_dimes, get_nickel, get_penny, user_response)
            os.system('cls')
            print(cal_update)

        elif(check != ""):
            print(check)


while True:
    coffee_machine()
