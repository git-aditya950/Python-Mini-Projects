import random

print(" Welcome to Aditya's Number Guessing Game!")

LOW = 1
HIGH = 100
secret_number = random.randint(LOW, HIGH)
attempts = 0

print(f" I've picked a number between {LOW} and {HIGH}. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < LOW or guess > HIGH:
            print(f" Your guess is out of range! Please choose between {LOW}-{HIGH}.")
            continue

        if guess < secret_number:
            print(" Too low! Try a higher number.")
        elif guess > secret_number:
            print(" Too high! Try a lower number.")
        else:
            print(f" Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print(" Invalid input! Please enter a number.")
