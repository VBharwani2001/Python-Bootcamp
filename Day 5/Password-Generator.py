# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for i in range(0, nr_letters):
    letter = letters[random.randint(0, len(letters)-1)]
    password += letter
for j in range(0, nr_numbers):
    number = numbers[random.randint(0, len(numbers)-1)]
    password += number
for k in range(0, nr_symbols):
    symbol = symbols[random.randint(0, len(symbols)-1)]
    password += symbol
print(f"{password} ---- would be the easy password to hack")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for l in range(0, nr_letters):
    password_list += random.choice(letters)
for m in range(0, nr_numbers):
    password_list += random.choice(numbers)
for n in range(0, nr_symbols):
    password_list += random.choice(symbols)


random.shuffle(password_list)
hard_pass = ""
for char in password_list:
    hard_pass += char

print(f"\n{hard_pass} ---- would be difficult password to hack")
