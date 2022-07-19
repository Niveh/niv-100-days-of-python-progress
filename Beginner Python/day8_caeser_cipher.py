
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(plain_text, shift_amount, direction):
    message = ""
    shift_value = -1
    if direction == "decode":
        shift_value = 1
        shift_amount *= -1

    for i in plain_text:
        pos = alphabet.index(i) + shift_amount

        if pos >= len(alphabet) or pos < 0:
            pos += len(alphabet) * shift_value

        message += alphabet[pos]

    print(f"The {direction}d message is {message}")


caeser(text, shift, direction)
