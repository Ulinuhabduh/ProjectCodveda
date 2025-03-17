import random

print("Welcome to the Number Guessing Game!")
print('You have 10 attempts to guess the number')

number = random.randint(1, 100)

# The user input
guess = int(input("Guess a number between 1 and 100: "))

attempts = 1
max_attempts = 10

while guess != number:
    if guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
    
    print('------------------------')
    
    print(f"You have {max_attempts - attempts} attempts left.")

    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if attempts == max_attempts:
        print("You have reached the maximum number of attempts.")
        break

print(f"Congratulations! You guessed the number in {attempts} attempts.")
