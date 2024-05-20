import random

print("Welcome to the Guess the Number Game")
print("**************************************************")
print("I'm thinking of a number from 1 to 100")
print("Try to guess it.")

choice = "y"
while choice.lower() == "y":
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guess = None

    # Continue prompting the user until the correct guess
    while guess != target_number:
        attempts +=1
        guess = int(input("Enter your guess (1-100): "))

        if guess < target_number:
            print("Too low, try again.")
        elif guess > target_number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the number!")

    # Ask the user if they want to play again
    choice = input("Would you like to play again? (y/n): ")

print("Bye - Come back soon!")
