import random

print("Welcome to number guessing game!")
print("I am thinking of number between 1 to 100.")

NUMBER = random.randint(1, 100)

difficulty = input("Choose difficulty (easy or hard): ").lower()

if (difficulty == "easy"):
    i = 10
elif(difficulty == "hard"):
    i = 5

while i >= 0:
    if(i != 0):
        print(f"You have {i} attempts left")
        make_a_guess = int(input("Make a guess:  "))
        if (make_a_guess == NUMBER):
            print(f"Horray you got it! Answer was {NUMBER}")
            exit()
        elif(make_a_guess > NUMBER):
            print("TOO HIGH")
            i -= 1
        elif(make_a_guess < NUMBER):
            print("TOO LOW")
            i -= 1
    elif(i == 0):
        print(f"You've run out of guesses. You lose! number was {NUMBER}")
        i -= 1
