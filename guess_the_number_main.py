import random
from guess_the_number_art import header

print(header)
print("Welcome to number guessing game! ")
print("Im thinking of a number between 1 and 100")
print("Try to guess what it is-")
random_number = random.randint(1, 100)
here =True
while here:
    mode = input("Do you want to play the easy medium or hard mode: ").lower()
    if mode == "easy":
        lives=10
        here=False
    elif mode == "medium":
        lives=5
        here=False
    elif mode == "hard":
        lives=3
        here=False
    else:
        print("Invalid input enter easy medium or hard")

for turns in range(lives):
    number=True
    while number:
        try:
            guess=int(input("Guess a number: "))
            number=False
        except :
            print("Invalid input enter a whole number")
    if guess == random_number:
        print(f"Congratulations, you guessed it the number is {random_number}")
        break
    elif guess < random_number:
        print("Too low")
        lives-=1
        print(f"You have` {lives} lives left.")
    elif guess > random_number:
        print("Too high")
        print(f"You have` {lives} lives left.")
    if lives == 0:
        print("Game over you have lost all your lives")
