 
import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("Thinking of a number between 1 and 100")
    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == secret_number:
            print("Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_the_number()