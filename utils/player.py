import random

# from card import Card

"""Create a class Player with attributes:
    - 'cards' which is a list of 'Card' (import 'Card' from card.py
    - 'turn_count' which is an int starting a 0
    - 'number_of_cards' which is an int starting at 0
    - 'history' which is a list of 'Card' that will contain all the cards played by the player
   ----------------------with some methods:
    - 'play()' that will:
    -- randomly pick a 'Card' in 'cards'
    -- Add the 'Card' to the 'Player's history'
    -- Print: '{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}'
    -- Return the 'Card'    
"""


class Player:

    #    rnd_card_pick = ""
    #    player_name = "Player " + str(turn_count)

    def __init__(self, card, turn_count, number_of_cards, history):
        self.card = card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def __str__(self):
        return "{} {} {} {}".format(self.card, self.turn_count, self.number_of_cards, self.history)

    def play(player):
        # randomly pick a card
        global rnd_card_pick
        rnd_card_pick = cards[random.randint(0, 52)]
        # add the card to the player's history
        history.append(rnd_card.pick)
        # print {player_name} {turn_count} played: {card_number} {card_symbol_icon}.

        return "{} {} played: {} {}".format(self, turn_count, card_number, card_symbol_icon)


"""Create a Deck class that contains:
    - An attribute cards which is going to contain a list of instances of Card.
    - A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 
        10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
    - A shuffle() method that will shuffle all the list of cards.
    - A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the 
        players.
"""


class Deck():

    def __init__(self, value_list, icon_color_list):
        super().__init__(value_list, icon_color_list)
        self.card = card
        self.value_list = value_list
        self.icon_color_list = icon_color_list
        return

    def __str__(self):
        return "{}".format(self.card)

    def fill_deck():
        icon_color_list = ["♥ - Red", "♦ - Red", "♣ - Black", "♠ - Black"]
        value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        global deck
        deck = []
        for item in range(len(icon_color_list)):
            for value in range(len(value_list)):
                deck.append(value_list[value] + " << " + icon_color_list[item] + " >>")
        print(len(deck),deck)
        print(deck)
        return deck

    def shuffle():
        x = deck.split()
        return random.shuffle(deck)

    """"'Distribute()' will take a list of player as parameter
        end will distribute the cards evenly all the players
    """

    def distribute(self, players):
        """for players check the 'class Board'"""
        # self.players = players[]

        return
