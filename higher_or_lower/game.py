import random
from art import Or
import time
from game_data import celebrities_data
from art import game_over
from art import banner

print(banner)
print("Welcome to the higher or lower game")
print("Try to guess who has more followers on instagram")


def higher_or_lower():
    Alive = True
    score = 0
    while Alive:
        print("\n" * 100)
        number_1 = random.randint(1, 20)
        number_2 = random.randint(1, 20)

        while number_1 == number_2:
            number_2 = random.randint(1, 20)

        person_1 = celebrities_data[number_1]["name"]
        description_1 = celebrities_data[number_1]["description"]
        country_1 = celebrities_data[number_1]["country"]

        person_2 = celebrities_data[number_2]["name"]
        description_2 = celebrities_data[number_2]["description"]
        country_2 = celebrities_data[number_2]["country"]

        print(f"(A)-\n{person_1} who is  {description_1} from the {country_1}")
        print(Or)
        print(f"(B)_\n{person_2} who is  {description_2} from the {country_2}")
        a = celebrities_data[number_1]["followers"]
        b = celebrities_data[number_2]["followers"]
        Guessed = True
        while Guessed:
            guess = input("Who do you think has more followers A or B? ").lower()
            if guess == "a":
                if a > b:
                    print(f"You guessed correctly {person_1} has {a} million followers while  {person_2} has only {b} million followers!")
                    score += 1
                    time.sleep(5)
                else:
                    print(f"You guessed wrong {person_1} has only {a} million followers while  {person_2} has  {b} million followers!")
                    print(f"Your score is {score}")
                    print(game_over)
                    return
                break

            elif guess == "b":
                if b > a:
                    print(f"You guessed correctly {person_1} has only {a} million followers while  {person_2} has  {b} million followers!")
                    score += 1
                    time.sleep(5)
                else:
                    print(f"You guessed wrong {person_1} has {a} million followers while  {person_2} has only {b} million followers!")
                    print(f"Your score is {score}")
                    print(game_over)
                    return


                break
            else:
                print("That is not a guess, try again")


playing=True
while playing:
    play = input("Do you want to begin yes(y) or no(n)? ")
    if play == "y":
        higher_or_lower()
        playing = False
    elif play == "n":
        print("Its ok play whenever you are free")
        break
    else:
        print("Enter valid input y or n")



