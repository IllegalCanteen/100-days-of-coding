
import random
from black_jack_logos import logo
from black_jack_logos import win
from black_jack_logos import lose
from black_jack_logos import draw



def black_jack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_score = 0
    play_again=True
    player_cards = [random.choice(cards), random.choice(cards)]
    if player_cards[0] == 11 and player_cards[1] == 11:
        player_cards[0]=1
    print(f"PLAYERS CARDS : {player_cards}")

    computer_cards = [random.choice(cards)]
    print(f"COMPUTER'S FIRST CARD- {computer_cards}: ")

    print("\n")

    computer_cards += [random.choice(cards)]

    pick_again = input("Do you want to pick another card: ").lower()
    while play_again:
        player_score=0
        if pick_again == "y":
            player_cards.append(random.choice(cards))

            for card in player_cards:
                player_score += card



            if player_score > 21:
                if 11 in player_cards:
                    player_score=0
                    position_of_11=player_cards.index(11)
                    player_cards[position_of_11]= 1
                    for card in player_cards:
                        player_score += card
                    print(f"Your cards: {player_cards}")
                    print(f"Your score: {player_score}")
                    pick_again=input("\nDo you want to pick another card: ").lower()
                else:
                    print(f"Your cards: {player_cards}")
                    print(f"You lose you have {player_score} which is above 21 ")
                    print("\n")
                    print("Dealer wins")
                    print(lose)
                    return()
            elif player_score == 21:
                print(f"Your cards: {player_cards}")
                break
            else:
                print(f"Your cards: {player_cards}")
                print(f"Your score: {player_score}")
                pick_again = input("\nDo you want to pick another card: ").lower()

        elif pick_again == "n":
            for card in player_cards:
                player_score += card
            print(f"Your score: {player_score}")
            break

    print("\n" )
    computer_score = 0
    for card in computer_cards:
        if computer_cards[0] == 11 and computer_cards[1] == 11:
            computer_cards[0]=1
        computer_score += card
    print(f"computers cards: {computer_cards}")
    print(f"computers score: {computer_score}")
    if computer_score< 17:
        cpick_again=True
        while cpick_again:
            print("\nDealer cards too low picking another card ")
            computer_cards.append(random.choice(cards))
            computer_score = 0
            for card in computer_cards:
                computer_score += card

            if computer_score > 21:
                if 11 in computer_cards:
                    computer_score = 0
                    position_of_11_dot_2 = computer_cards.index(11)
                    computer_cards[position_of_11_dot_2] = 1
                    for card in computer_cards:
                        computer_score += card
                    print(computer_cards)
                    if computer_score >21:
                        print(f"Computers new cards:{computer_cards} ")
                        print("Computer has exceeded 21 you win! ")
                        print(win)
                        return
                else:
                    print(f"\nComputers new cards:{computer_cards} ")
                    print("\nComputer has exceeded 21 you win! ")
                    print(win)
                    return

            elif computer_score >= 17:
                print(f"Dealer's cards: {computer_cards}")
                print(computer_score)
                break
            else:
                print(f"Computers new cards:{computer_cards} ")
                print(f"computers new score: {computer_score}")


    print(f'''Your cards: {player_cards} vs Dealers cards: {computer_cards} ''')
    if computer_score > player_score:
        print("Dealer Wins")
        print(lose)
    elif computer_score == player_score:
        print("Its a draw no one wins")
        print(draw)

    elif computer_score < player_score:
        print("Player wins")
        print(win)
    return None


black_jack()
