
import random
from art import logo
import os
from time import sleep

# print(f"Welcome to blackjack \n{logo}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# randomizer
def rand():
    x = cards[random.randint(0, 12)]
    return x

def game():
    dealer = [rand(), rand()]
    player = [rand(), rand()]
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {dealer[0]}")
    if sum(dealer) == 21 or (sum(player) == 21 and sum(dealer) == 21):
        print(f"Computer's hand: {dealer} \nComputer's score is: {sum(dealer)}")
        print(f"\nYour hand: {player} \nYour score is: {sum(player)}")
        print("Black Jack, You LOSE :(")
        return ("Game over")
    elif sum(player) == 21:
        print(f"Computer's hand: {dealer} \nComputer's score is: {sum(dealer)}")
        print(f"\nYour hand: {player} \nYour score is: {sum(player)}")
        print("Black Jack, You WIN!!")
        return("Game over")
    else:
        return (player, dealer)

# first answer
def game_cont(ply, deal):
    cont_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if cont_game == "y":
        # player new hand
        new_card = rand()
        ply.append(new_card)
        print(f"\nYour cards: {ply}, current score: {sum(ply)}")
        # for ace subs
        for acex in ply:
            if acex == 11 and sum(ply) > 21:
                z = ply.index(acex)
                ply[z] = 1
        for aces in deal:
            if aces == 11 and sum(deal) > 21:
                v = deal.index(aces)
                deal[v] = 1
        if sum(ply) == 21:
            print(f"\nComputer's hand: {deal} \nComputer's score is: {sum(deal)}")
            print(f"\nYour hand: {ply} \nYour score is: {sum(ply)}")
            print("You WIN!!")
        elif sum(ply) > 21:
            print(f"Computer's hand: {deal} \nComputer's score is: {sum(deal)}")
            print(f"\nYour hand: {ply} \nYour score is: {sum(ply)}")
            print("Bust")
        else:
            game_cont(ply, deal)
        #  Win Condition

    elif cont_game == "n":
        while sum(deal) < 17:
            dealer_new_card = rand()
            deal.append(dealer_new_card)
        print(f"Computer's hand: {deal} \nComputer's score is: {sum(deal)}")
        print(f"\nYour hand: {ply} \nYour score is: {sum(ply)}")
        if sum(ply) > sum(deal) and sum(ply) < 21:
            print("You WIN!!!")
        elif sum(ply) < sum(deal) and sum(deal) > 21:
            print("You Win")
        elif sum(ply) == sum(deal):
            print("Stand OFF!!")
        else:
            print("You Lose!")
    else:
        print("Wrong input try again")
        game_cont(ply, deal)

def restarter(start):
    if start == "yes":
        z = game()
        if z != "Game over":
            game_cont(z[0], z[1])
        start = input("Do you want to play again? yes? or no? ").lower()
        if start == "yes":
            sleep(1)
            os.system('cls')
            sleep(2)
            print(f"Welcome to blackjack \n{logo}")
            restarter(start)
    elif start == "no":
        print("Game over")
    else:
        print("Wrong input try again")
        starter()

def starter():
    print(f"Welcome to blackjack \n{logo}")
    start = input("Do you want to play? ").lower()
    restarter(start)
# PROGRAM START
rand()
starter()