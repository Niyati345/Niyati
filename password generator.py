letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#esay
import random

"""passward = ""
for i in range (0,nr_letters):
    passward += random.choice(letters)
for i in range(0, nr_numbers):
    passward += random.choice(numbers)
for i in range(0, nr_symbols):
    passward += random.choice(symbols)
print (passward)"""

#hard
password_list=[]
for i in range (0,nr_letters):
    password_list += random.choice(letters)
for i in range(0, nr_numbers):
    password_list += random.choice(numbers)
for i in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password=""
for i in password_list:
    password += i
print (password)


def check_strength(pwd):
    length_score = len(pwd) >= 12
    upper = any(c.isupper() for c in pwd)
    lower = any(c.islower() for c in pwd)
    digit = any(c.isdigit() for c in pwd)
    symbol = any(c in symbols for c in pwd)

    score = sum([length_score, upper, lower, digit, symbol])

    if score == 5:
        return "🟢 Strong password"
    elif score >= 3:
        return "🟡 Medium strength password"
    else:
        return "🔴 Weak password"

print(f"Password strength: {check_strength(password)}")