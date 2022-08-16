# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw_easy = ""
for i in range(nr_letters):
    pw_easy += random.choice(letters)
for i in range(nr_symbols):
    pw_easy += random.choice(symbols)
for i in range(nr_numbers):
    pw_easy += random.choice(numbers)

print(f"Password (Easy): {pw_easy}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw_hard = ""
total = nr_letters + nr_symbols + nr_numbers

while total > 0:
    next_type = random.randint(1, 3)
    if next_type == 1 and nr_letters:
        pw_hard += random.choice(letters)
        nr_letters -= 1
    elif next_type == 2 and nr_symbols:
        pw_hard += random.choice(symbols)
        nr_symbols -= 1
    elif next_type == 3 and nr_numbers:
        pw_hard += random.choice(numbers)
        nr_numbers -= 1
    total = nr_letters + nr_symbols + nr_numbers

print(f"Password (Hard): {pw_hard}")
