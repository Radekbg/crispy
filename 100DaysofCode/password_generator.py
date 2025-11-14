import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# random_choice = ""
#
# for i in range(nr_letters):
#     random_choice += random.choice(letters)
#
# for j in range(nr_symbols):
#     random_choice += random.choice(symbols)
#
# for n in range(nr_numbers):
#     random_choice += random.choice(numbers)
#
# your_password = ""
# for i in random_choice:
#     your_password += random.choice(random_choice)
#
# print("Your password is:", your_password)
#
random_choice = []

for i in range(nr_letters):
    random_choice += random.choice(letters)

for j in range(nr_symbols):
    random_choice.append(random.choice(symbols))

for n in range(nr_numbers):
    random_choice.append(random.choice(numbers))

your_password = ""

for i in random_choice:
    your_password += random.choice(random_choice)

print("Your password is:", your_password)
