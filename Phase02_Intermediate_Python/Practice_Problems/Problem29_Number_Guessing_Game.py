# একটি number guessing game তৈরি করতে হবে।

secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")