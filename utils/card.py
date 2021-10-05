icons = ["♥", "♦", "♣", "♠"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


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


"""
CHECK class SYMBOL
symbol = Symbol("♥", "red")
print(type(symbol), symbol.color, symbol.icon)
print(symbol.__str__())
"""


class Card(Symbol):
    """
    A class that defines a card.
    It inherits from the class Symbol.
    """

    def __init__(self, icon, value):
        """A card is defined by its value and icon."""
        super().__init__(icon, value)
        self.icon = icon
        self.value = value

    def __str__(self):
        """Method called during a conversion of the object
        into a chain"""
        return "{} {}".format(self.icon, self.value)


# CHECK class CARD
"""card = Card("♥", "7")
print(type(card), card.color, card.icon)
print(card.__str__())

print(card.__str__())
print(card)
print(str(card))
print(card.__repr__())
"""
