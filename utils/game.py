"""A class called Board that contains:

    - An attribute players that is a list of Player. It will contain all the players that are playing.
    - An attribute turn_count that is an int.
    - An attribute active_cards that will contain the last card played by each player.
    - An attribute history_cards that will contain all the cards played since the start of the game, except for
        active_cards.
   -- A method start_game() that will:
    - Start the game,
    - Fill a Deck,
    - Distribute the cards of the Deck to the players.
    - Make each Player play() a Card, where each player should only play 1 card per turn, and all players have to
        play at each turn until they have no cards left.
   -- At the end of each turn, print:
    - The turn count.
    - The list of active cards.
    - The number of cards in the history_cards."""


class Board:

    def __init__(self, players, turn_count, active_cards, history_cards):
        self.players = players  # a list that contains all the players that are playing
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

    def __str__(self):
        return "{} {} {} {}".format(self.player, self.turn_count, self.active_cards, self.history_cards)

    def start_game():
        # fill a deck
        fill_deck()
        # distribute the cards of the "Deck" to the players
        distribute()
        # make each Player play() a Card, where each player should only play 1
        ## card in turn until they have no cards left
        play()
        # at the end of each turn, print:
        ## - the turn count
        print(turn_count)
        ## - the list of active cards
        print(" ... list of active cards ... ")
        ## - the number of cards in the history_cards
        print(history_cards)
        return
