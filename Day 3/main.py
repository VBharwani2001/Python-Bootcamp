print("----------------- Day 3 Roller Coster Height check----------------------")
height = int(input("Please enter your height in cm: "))
if height > 120:
    print("You can Ride")
else:
    print("You cannot ride")

print("----Odd Even Exersice----")
user_number = int(
    input("Please enter a number to check if the number is odd or even: "))
if user_number == 0:
    print(f"{user_number} is neither odd nor even!")
elif user_number % 2 == 0:
    print(f"{user_number} is an even number")
else:
    print(f"{user_number} is an odd number")
