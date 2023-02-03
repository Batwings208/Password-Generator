import random
import string

print("Welcome to a Password Generator!")
choice = input("Which format? (Numbers, Text, Lowercase, Uppercase, Punctuation): ")

if choice == "Lowercase":
    # printing lowercase
    letters = string.ascii_lowercase
    print(''.join(random.choice(letters) for i in range(10)))

elif choice == "Uppercase":
    # printing uppercase
    letters = string.ascii_uppercase
    print(''.join(random.choice(letters) for i in range(10)))

elif choice == "Text":
    # printing letters
    letters = string.ascii_letters
    print(''.join(random.choice(letters) for i in range(10)))

elif choice == "Digits":
    # printing digits
    letters = string.digits
    print(''.join(random.choice(letters) for i in range(10)))

elif choice == "Punctuation":
    # printing punctuation
    letters = string.punctuation
    print(''.join(random.choice(letters) for i in range(10)))

