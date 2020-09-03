class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return ' \U0001f0a0  '.join((self.value, self.color))

