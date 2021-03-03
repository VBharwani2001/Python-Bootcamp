import random
import hangman_logo
import hangman_word_list

stages = hangman_logo.stages
print(hangman_logo.logo)
word_list = hangman_word_list.word_list
display = []

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.


lives = len(stages) - 1
chosen_word = word_list[random.randint(0, len(word_list))]
for _ in chosen_word:
    display.append("_")
print(chosen_word)
print(display)
word_guessed = True

while word_guessed:
    guess = input("Guess the letter:   \n ").lower()
    if guess in display:
        print(f"You have already guessed the letter {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            print(display)
# TODO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(display)
    if lives == 0:
        print("You lose!")
        word_guessed = False
        print(
            f"{'' .join(display)} is your guessed answer but the actual answer is {chosen_word}")

    if not "_" in display:
        word_guessed = False
        print("you win")
        print(f"{''.join(display)} is the correct word guessed")
