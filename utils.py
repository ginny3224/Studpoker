# utils.py

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a string representation of the card."""
        return f"({self.rank} of {self.suit})"

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def rank(self):
        """Evaluate the rank of the poker hand."""
        ranks = [card.rank for card in self.cards]
        rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}

        # Check for specific hand ranks (e.g., pair, two pair, three of a kind, etc.)
        if len(rank_counts) == 5:
            # No pairs or other combinations, check for high card
            return "High Card"
        elif 4 in rank_counts.values():
            return "Four of a Kind"
        elif 3 in rank_counts.values() and 2 in rank_counts.values():
            return "Full House"
        elif 3 in rank_counts.values():
            return "Three of a Kind"
        elif list(rank_counts.values()).count(2) == 2:
            return "Two Pair"
        elif 2 in rank_counts.values():
            return "Pair"
        else:
            return "High Card"

def evaluate_hand(hand):
    """Evaluate the strength of a poker hand based on visible cards."""
    hand_instance = Hand()
    for card in hand:
        hand_instance.add_card(card)
    return hand_instance.rank()

def get_card_rank_value(card):
    """Return the numerical value of a card's rank."""
    rank = card.rank
    if rank.isdigit():
        return int(rank)  # Convert digit rank to integer
    elif rank == "Jack":
        return 11
    elif rank == "Queen":
        return 12
    elif rank == "King":
        return 13
    elif rank == "Ace":
        return 14  # Ace is highest rank
    else:
        return 0  # Invalid rank (should not happen in a valid deck)
