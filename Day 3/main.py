# print("----------------- Day 3 Roller Coster Height check----------------------")
# height = int(input("Please enter your height in cm: "))
# if height > 120:
#     print("You can Ride")
# else:
#     print("You cannot ride")

# print("----Odd Even Exersice----")
# user_number = int(
#     input("Please enter a number to check if the number is odd or even: "))
# if user_number == 0:
#     print(f"{user_number} is neither odd nor even!")
# elif user_number % 2 == 0:
#     print(f"{user_number} is an even number")
# else:
#     print(f"{user_number} is an odd number")

# print("-----------------Roller Coster Height and Age check----------------------")
# height = int(input("Please enter your height in cm: "))
# if height > 120:
#     print("You can Ride")
#     age = int(input("Whats your age? "))
#     if age >= 18:
#         print("Please pay 12$ to go ahead")
#     elif age >= 12 & age < 18:
#         print("Please pay 7$ to go ahead")
#     elif age < 12:
#         print("Please pay 5$ to go ahead")
# else:
# #     print("You cannot ride")

# print("----------------Day 3 BMI Calculator 2.0----------------")
# height = float(input("whats your hight in meter? "))
# weight = float(input("whats your weight in Kg's? "))
# calculatedBMI = int(weight/(height**2))
# if calculatedBMI <= 18.5:
#     print("You are under weight !!")
# elif calculatedBMI > 18.5 & calculatedBMI <= 25:
#     print("You have normal weight ! ")
# elif calculatedBMI > 25 & calculatedBMI <= 30:
#     print("You are over weight ! ")
# elif calculatedBMI > 30 & calculatedBMI <= 35:
#     print("You are Obese ! ")
# elif calculatedBMI > 35:
#     print("you are clinically obese !!!!!")

# print("----Leap year check challenge----")
# year = int(input("Year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

# print("-----------------Roller Coster Height + Age + photos check----------------------")
# height = int(input("Please enter your height in cm: "))
# bill = 0
# photos = input("Do you need photos?(Y or N): ")
# if height > 120:
#     print("You can Ride")
#     age = int(input("Whats your age? "))
#     if age >= 18:
#         bill += 12
#     elif age >= 12 & age < 18:
#         bill += 7
#     elif age < 12:
#         bill += 5
#     if photos == "Y":
#         bill += 3
#     print(f"You are eligible to ride and your bill would be {bill}$ only")
# else:
#     print("You cannot ride")

print("--------Welcome to pizza shop------------")
pizza_size = input("What size pizza would you like to have?(S, M or L):     ")
add_pepperoni = input(
    "Would you like to have pepperoni on it?(S = +2$ and M/L = +3$)(Y or N):    ")
add_cheese = input("Would you like extra cheese on it?(+1$)(Y or N):    ")
bill = 0
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    elif pizza_size == "M" or pizza_size == "L":
        bill += 3

if add_cheese == "Y":
    bill += 1

print(f"Thank you for the order. You final amount to pay is {bill} $")
