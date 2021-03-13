import os
from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


continue_calculation = True
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
num1 = int(input("Whats the first number?  "))
for symbols in operations:
    print(symbols)
while continue_calculation:
    response = input("Pick an operator?  ")
    num2 = int(input("Whats the second number?  "))
    operator = operations[response]
    answer = operator(num1, num2)
    print(f"{num1} {response} {num2} = {answer}")
    want_to_continue = input(
        f"Do you want to continue with {answer}(y) or want to start with new number(n) or enter exit?  ").lower()
    if want_to_continue == "n":
        os.system('cls')
        num1 = int(input("Whats the first number?  "))
        print(logo)
    elif want_to_continue == "exit":
        exit()
    else:
        num1 = answer


# num1 = int(input("Please enter first number:  "))
# num2 = int(input("Please enter second number: "))
# print("""Operations :
# +
# -
# *
# /""")
# operation = input("Please select operation from the above options:  ")
# function = operations[operation]
# answer = function(num1, num2)
# print(f"{num1} {operation} {num2} = {answer}")
