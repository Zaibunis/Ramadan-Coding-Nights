import random

print("Welcome to the game, this is a number guessing game!\nYou got 5 attempts to guess the number between 50 and 100, let's start the game.")

number_to_guess = random.randint(50, 100)
chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess}, and you found it right in {guess_counter} attempt(s)!")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops, sorry! The number was {number_to_guess}. Better luck next time!")
    elif my_guess < number_to_guess:
        print("Your guess is too low, try again!")
    elif my_guess > number_to_guess:
        print("Your guess is too high, try again!")