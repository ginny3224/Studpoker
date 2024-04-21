class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.hand = []
        self.chips = chips

    def __str__(self):
        return f"{self.name} ({self.chips} chips)"

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def discard_hand(self):
        self.hand = []

    def bet(self, amount):
        self.chips -= amount

    def receive_winnings(self, amount):
        self.chips += amount
