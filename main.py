"""
This file starts the 'CARD GAME'
"""
import utils.player
from utils.player import Deck
import utils.card
import utils.game
import random

print("Card Game")
"""
Start the game. You should only run this file to have the game running.
"""
"""ask how many players there are
    and their names
"""
players_list = []
number_of_players = 0
game_on = True
game_ini = False

"""Start of the game"""
while game_on:
    print("Welcome to the Game!")
    print("Let's start")
    """get players names"""
    while not game_ini:
        number_of_players = int(input("How many players? Type: < 2 > or < 4 > "   ))
        if number_of_players not in [2, 4]:
            print("Try again! TWO (2) or FOUR (4) players?   ")
        else:
            game_ini = True
        break
    print("Fine, ", number_of_players, " players it is!")

    for player in range(1, number_of_players+1):
        players_list.append(str(input("name: ")))

    print("Welcome ", players_list)
    print("Let's Rock 'nRoll !")
    print("GAME STARTS")
    break
"""call fill_deck() from class Deck
    tokenManager_obj = TokenManager()
    tokenManager_obj.create()"""

deck = Deck.fill_deck()

#    fill_deck(cards)

print("-------------")
#deck.shuffle()
#print(deck.shuffle)





print("Game Over")
game_on = False

