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
#     print("You cannot ride")

print("----------------Day 3 BMI Calculator 2.0----------------")
height = float(input("whats your hight in meter? "))
weight = float(input("whats your weight in Kg's? "))
calculatedBMI = int(weight/(height**2))
if calculatedBMI <= 18.5:
    print("You are under weight !!")
elif calculatedBMI > 18.5 & calculatedBMI <= 25:
    print("You have normal weight ! ")
elif calculatedBMI > 25 & calculatedBMI <= 30:
    print("You are over weight ! ")
elif calculatedBMI > 30 & calculatedBMI <= 35:
    print("You are Obese ! ")
elif calculatedBMI > 35:
    print("you are clinically obese !!!!!")
