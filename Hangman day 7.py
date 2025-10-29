#Hangman
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

chosen_word=random.choice(word_list)
placeholder=""
lives=6



for letter in range(len(chosen_word)):
    placeholder+="-"

game_over = False
correct_letters=[]
print(placeholder)
while not game_over:
    print(f"******************************************YOU HAVE {lives} LIVES LEFT******************************************************")
    guess = input("What letter do you want to guess: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter== guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"The {guess} was a bad guess you lose a life !")
        if lives == 0:
            game_over=True
            print("******************************************YOU  LOSE GAME OVER !******************************************************")
            print(f"THE ACTUAL WORD WAS  {chosen_word}!")

    if  "_" not in display:
        game_over=True
        print("**********************************************YOU  WON GAME OVER !*******************************************************")
    print(stages[lives])

