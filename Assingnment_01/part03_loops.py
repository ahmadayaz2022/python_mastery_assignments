# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import random

# Warm-up: Times table
try:
    number = int(input("Enter a number for its times table: "))
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")
except ValueError:
    print("Please enter an integer.")

# Build: ATM PIN check
correct_pin = "4321"
for attempt in range(1, 4):
    entered_pin = input("\nEnter your 4-digit PIN: ").strip()
    if entered_pin == correct_pin:
        print("Welcome")
        break
    tries_left = 3 - attempt
    if tries_left:
        print(f"Incorrect PIN. Tries left: {tries_left}")
    else:
        print("Card blocked")

# Challenge: Number guessing game
while True:
    secret = random.randint(1, 50)
    guesses = 0
    while True:
        try:
            guess = int(input("Guess a number from 1 to 50: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        guesses += 1
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Got it in {guesses} guesses!")
            break
    if input("Play again? (y/n): ").strip().lower() != "y":
        break

# Extra practice
for row in range(1, 6):
    print("*" * row)
print("Sum of even numbers from 1 to 100:", sum(range(2, 101, 2)))
