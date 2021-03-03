import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, 2)]
print(chosen_word)
word_guessed = True
guess = input("Guess the letter").lower()
for letter in chosen_word:
    if letter == guess:
        print("Yes it is in there")
    else:
        print("nope")
