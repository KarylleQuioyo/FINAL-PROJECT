import random
def number_guessing_game():
    guess_number = random.randint(1, 100)
    guess = None

    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while guess != guess_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < guess_number:
            print("Too low! Try again.")
        elif guess > guess_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {guess_number} correctly!")


number_guessing_game()