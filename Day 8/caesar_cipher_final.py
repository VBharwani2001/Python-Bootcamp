import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

check_continue = True
while check_continue:

    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cipher(input_text, input_shift, input_direction):
        cipher_text = ""
        if direction == "decode":
            input_shift *= -1
        for letter in input_text:
            if letter in alphabet:
                alphabet_position = alphabet.index(letter)
                new_position = alphabet_position + input_shift
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter
        print(f"The {input_direction}d text is {cipher_text}")
        if input("Continue?(Y/N)") == "N":
            check_continue = False
    if shift > 26:
        shift = shift % 26
    cipher(text, shift, direction)

print("goodbye")
