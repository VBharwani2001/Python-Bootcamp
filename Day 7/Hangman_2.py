import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = word_list[random.randint(0, 2)]
for _ in chosen_word:
    display.append("_")
print(chosen_word)
print(display)
word_guessed = True

guess = input("Guess the letter:    ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

print(display)
