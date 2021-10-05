import random
from card import Card

var_testing = Card("♥", "7")
print(var_testing)
print(var_testing.icon)


cards = ['A of ♥', '2 of ♥', '3 of ♥', '4 of ♥', '5 of ♥', '6 of ♥', '7 of ♥', '8 of ♥', '9 of ♥', '10 of ♥', 'J of ♥',
         'Q of ♥', 'K of ♥', 'A of ♦', '2 of ♦', '3 of ♦', '4 of ♦', '5 of ♦', '6 of ♦', '7 of ♦', '8 of ♦', '9 of ♦',
         '10 of ♦', 'J of ♦', 'Q of ♦', 'K of ♦', 'A of ♣', '2 of ♣', '3 of ♣', '4 of ♣', '5 of ♣', '6 of ♣', '7 of ♣',
         '8 of ♣', '9 of ♣', '10 of ♣', 'J of ♣', 'Q of ♣', 'K of ♣', 'A of ♠', '2 of ♠', '3 of ♠', '4 of ♠', '5 of ♠',
         '6 of ♠', '7 of ♠', '8 of ♠', '9 of ♠', '10 of ♠', 'J of ♠', 'Q of ♠', 'K of ♠']
history = []

class Player:

    def __init__(self, card, turn_count, number_of_cards, history):
        self.card = card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

        self.rnd_card_pick = ""
        self.player_name = "Player " + str(turn_count)

    def __str__(self):
        return "{} {} {} {}".format(self.card, self.turn_count, self.number_of_cards, self.history)

    def play(self, player_name, turn_count, card_number, card_symbol_icon):
        # randomly pick a card

        rnd_card_pick = cards[random.randrange(0, 52)]
        # add the card to the player's history
        history.append(rnd_card.pick)
        # print {player_name} {turn_count} played: {card_number} {card_symbol_icon}.

        return "{} {} played: {} {}".format(player_name, turn_count, card_number, card_symbol_icon)


# CHECK class PLAYER
player = Player(7, cards[0], 5, ["♥ of 10", "♥ of K", "♥ of 4"])
print(player)
print(type(player), player.card, player.turn_count, player.number_of_cards, player.history)
print(player.__str__())

# player = Player(7, cards[0], 5, ["♥ of 10", "♥ of K", "♥ of 4"])
# play()
# print(x)
# print(type(player), player.card, player.turn_count, player.number_of_cards, player.history)
# print(player.__str__())

"""
class Deck:

    icons = ["♥", "♦", "♣", "♠"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, cards):
        self.cards = cards[]
        return

    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += '\n ' + card.__str__()
        return "All of our cards:" + deck


    def fill_deck():
        for icon in icons:
            for value in values:
                self.cards.append(Card(icon, value))
        return

    def shuffle(self):
        random.shuffle(cards)
        return

    def distribute(self, play_list):
        self.play_list = play_list[]
        # this will take a list of player as parameter
        # end will distribute the cards evenly all the players
        return

fill_deck()
deck = Deck()
deck.display()

"""
