
#Work in progress please wait till i fix code and sort out all issues and bugs :)
import random
from black_jack_logos import logo

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_score = 0
    play_again=True
    player_cards = random.sample(cards, 2)
    print(f"PLAYERS CARDS : {player_cards}")

    computer_cards = random.sample(cards, 1)
    print(f"COMPUTER'S CARDS {computer_cards}: ")

    computer_cards += random.sample(cards, 1)

    pick_again = input("Do you want to pick another card: ").lower()
    while play_again:
        if pick_again == "y":
            player_cards += random.sample(cards, 1)
            print(player_cards)
            for card in player_cards:
                player_score += card
            print(f"Your score: {player_score}")
            if player_score > 21:
                print(f"You lose you have {player_score} which is above 21 ")
                print("Dealer wins")
                return()
            elif player_score == 21:
                break
            else:
                pick_again = input("Do you want to pick another card: ").lower()
                player_score=0
        elif pick_again == "n":
            for card in player_cards:
                player_score += card
            print(player_score)
            break



    computer_score = 0
    for card in computer_cards:
        computer_score += card
    print(computer_cards)
    print(f"computers score: {computer_score}")
    if computer_score< 17:
        print("Dealer cards too low picking another card ")
        computer_cards+=random.sample(cards,1)
        computer_score=0
        for card in computer_cards:
            computer_score += card
        if computer_score > 21:
            print(f"Computers new cards:{computer_cards} ")
            print("Computer has exceeded 21 you win! ")
            return
        else:
            print(f"Computers new cards:{computer_cards} ")
            print(f"computers new score: {computer_score}")

    if computer_score > player_score:
        print("Dealer Wins")

    elif computer_score == player_score:
        print("Its a draw no one wins")

    elif computer_score < player_score:
        print("Player wins")
    return None

print(logo)
black_jack()

