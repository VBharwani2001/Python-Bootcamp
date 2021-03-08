alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cipher(input_text, input_shift, input_direction):
    cipher_text = ""
    if direction == "decode":
        input_shift *= -1
    for letter in input_text:
        alphabet_position = alphabet.index(letter)
        new_position = alphabet_position + input_shift
        cipher_text += alphabet[new_position]
    print(f"The {input_direction}d text is {cipher_text}")


cipher(text, shift, direction)
