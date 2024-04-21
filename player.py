class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 1000  # Initialize with 1000 chips
        self.bet_amount = 0  # Initialize bet amount to 0

    def receive_card(self, card):
        self.hand.append(card)

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            self.bet_amount = amount
        else:
            print(f"{self.name} doesn't have enough chips to bet.")

    def fold(self):
        self.bet_amount = 0

    def get_bet_amount(self):
        return self.bet_amount

    def show_hand(self):
        print(f"{self.name}'s hand: {', '.join(str(card) for card in self.hand)}")

    def show_chips(self):
        print(f"{self.name} has {self.chips} chips remaining.")

    def show_bet(self):
        print(f"{self.name} has bet {self.bet_amount} chips.")

    def get_bet_amount(self):
        return self.bet