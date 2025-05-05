import random
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Enter a valid number.")
        continue

    guess = int(guess)
    attempts += 10

    if guess < secret_number:
        print("Low number")
    elif guess > secret_number:
        print("High number")
    else:
        print(f"Correct You guessed it in {attempts} attempts.")
        break
