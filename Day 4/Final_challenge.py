import random
print("DAY 4 ROCK PAPER SCISSORS GAME!!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(
    input("Select your answer: (0-rock, 1-paper, 2-scissors)   "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid selection")
    user_choice = -1


computer_choice = random.randint(0, 2)
print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == computer_choice:
    print("Its Draw")
elif user_choice > computer_choice:
    print("You win")
elif user_choice < computer_choice:
    print("You Lose")
else:
    print("Invalid choice! you lose")
