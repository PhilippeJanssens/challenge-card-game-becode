icons = ["♥", "♦", "♣", "♠"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Symbol():
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon
    def __str__(self):
        return

class Card(Symbol):
    def __init__(self, symbol, value):
        super().__init__()

    def __str__(self):
        return

    value=""

