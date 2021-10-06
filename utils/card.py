icons = ["♥", "♦", "♣", "♠"]
colors = ["Red", "Black"]
icon_color_list = ["♥ - Red", "♦ - Red", "♣ - Black", "♠ - Black"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

"""cards = ['A of ♥', '2 of ♥', '3 of ♥', '4 of ♥', '5 of ♥', '6 of ♥', '7 of ♥', '8 of ♥', '9 of ♥', '10 of ♥', 'J of ♥',
         'Q of ♥', 'K of ♥', 'A of ♦', '2 of ♦', '3 of ♦', '4 of ♦', '5 of ♦', '6 of ♦', '7 of ♦', '8 of ♦', '9 of ♦',
         '10 of ♦', 'J of ♦', 'Q of ♦', 'K of ♦', 'A of ♣', '2 of ♣', '3 of ♣', '4 of ♣', '5 of ♣', '6 of ♣', '7 of ♣',
         '8 of ♣', '9 of ♣', '10 of ♣', 'J of ♣', 'Q of ♣', 'K of ♣', 'A of ♠', '2 of ♠', '3 of ♠', '4 of ♠', '5 of ♠',
         '6 of ♠', '7 of ♠', '8 of ♠', '9 of ♠', '10 of ♠', 'J of ♠', 'Q of ♠', 'K of ♠']
"""


class Symbol:
    """Class representing one symbol"""

    def __init__(self, icon, color):
        """Constructor of the class Symbol"""
        self.icon = icon
        self.color = color

    def __str__(self):
        """Method called during a conversion of the object
        into a chain"""
        return "{}-{}".format(self.icon, self.color)


class Card(Symbol):
    """
    A class that defines a card.
    It inherits from the class Symbol.
    """

    def __init__(self, value_list, icon_color_list):
        """A card is defined by its value and icon."""
        super().__init__(value_list, icon_color_list)
        self.value_list = []
        self.icon_color_list = icon_color_list

    def __str__(self):
        """Method called during a conversion of the object
        into a chain"""
        return "{} {} {}".format(self.icon, self.value_list, self.icon_color_list)
