import random
from deck import Deck
from player import Player
import utils

# ANSI color escape codes (change text color)
COLOR_GREEN = "\033[92m"  # Green color
COLOR_BLUE = "\033[94m"   # Blue color
COLOR_RESET = "\033[0m"    # Reset to default color

# Betting limits
ANTE_AMOUNT = 10  # Ante amount (starting mandatory bet)
BRING_IN_AMOUNT = 20  # Bring-in amount (forced bet by the player with the lowest visible card)
SMALL_BET_AMOUNT = 20  # Small bet amount
BIG_BET_AMOUNT = 40  # Big bet amount

def determine_first_player(players):
    """Determine the player who acts first based on the strength of their face-up cards."""
    first_player = None
    highest_rank = -1  # Initialize with a low value
    for player in players:
        visible_card = player.hand[2]  # Index 2 is the first face-up card
        rank_value = utils.get_card_rank_value(visible_card)
        if rank_value > highest_rank:
            highest_rank = rank_value
            first_player = player
    return first_player

def determine_bring_in(players):
    """Determine the player who is the bring-in (lowest visible card)."""
    bring_in_player = None
    smallest_rank = float('inf')  # Initialize with a high value
    for player in players:
        visible_card = player.hand[2]  # Index 2 is the first face-up card
        rank_value = utils.get_card_rank_value(visible_card)
        if rank_value < smallest_rank:
            smallest_rank = rank_value
            bring_in_player = player
    return bring_in_player

def print_colored(message, color):
    """Print a message in the specified color."""
    print(f"{color}{message}{COLOR_RESET}")

def main():
    print("Welcome to 7 Card Stud Poker!")

    # Get number of players from user
    num_players = int(input("Enter the number of players (2-8): "))
    while num_players < 2 or num_players > 8:
        num_players = int(input("Invalid number of players. Please enter a number between 2 and 8: "))

    # Create players
    players = []
    player_names = ["Player 1"] + [f"CPU {i}" for i in range(2, num_players + 1)]
    for name in player_names:
        players.append(Player(name))

    # Initialize deck and shuffle
    deck = Deck()
    deck.shuffle()

    # Deal initial cards
    for _ in range(3):  # Deal three cards (two face down, one face up)
        for player in players:
            player.receive_card(deck.deal_card())

    # Determine first player based on the strength of face-up cards
    first_player = determine_first_player(players)
    player_index = players.index(first_player)
    players = players[player_index:] + players[:player_index]  # Rotate list based on first player

    # Determine bring-in player (lowest visible card)
    bring_in_player = determine_bring_in(players)
    print(f"The bring-in is: {bring_in_player.name}")

    # Rotate players list to start with bring-in player
    bring_in_index = players.index(bring_in_player)
    players = players[bring_in_index:] + players[:bring_in_index]

    # Game loop for betting rounds and drawing cards
    for round_num in range(3):  # Three betting rounds (adjust as needed)
        print(f"\n--- Round {round_num + 1} ---")

        # Display players' cards based on visibility rules
        for player in players:
            if player.name == "Player 1":
                # Human player can see all cards
                print(f"\n{player.name}'s cards: {', '.join(str(card) for card in player.hand)}")
            else:
                # CPU players can only see the face-up card
                visible_cards = [str(card) if index == 2 else "???" for index, card in enumerate(player.hand)]
                cpu_cards_display = ', '.join(visible_cards)
                if player == bring_in_player:
                    # Print bring-in message in green color for the bring-in player
                    print_colored(f"\n{player.name}'s cards: {cpu_cards_display}", COLOR_GREEN)
                else:
                    # Print other CPU players' cards in default color
                    print(f"\n{player.name}'s cards: {cpu_cards_display}")

        # Print bring-in message for human player
        if bring_in_player == players[0]:  # Check if bring-in player is the first player (human player)
            print_colored(f"\nThe bring-in is: {bring_in_player.name}", COLOR_GREEN)

        # Betting phase
        for player in players:
            print(f"\n{player.name}'s turn:")
            if player.name == bring_in_player.name:
                # Bring-in player makes bring-in bet
                bet_amount = BRING_IN_AMOUNT
            elif player.name == "Player 1":
                # Human player makes betting decision (fold, check, bet, raise, call)
                valid_actions = ["fold", "check", "bet", "raise", "call"]
                print("Valid actions: fold, check, bet, raise, call")
                player_action = input("Enter your action: ").lower()
                while player_action not in valid_actions:
                    player_action = input("Invalid action. Enter 'fold', 'check', 'bet', 'raise', or 'call': ").lower()
                
                if player_action == "bet":
                    bet_amount = SMALL_BET_AMOUNT
                elif player_action == "raise":
                    bet_amount = players[0].bet_amount * 2  # Double the previous bet amount
                elif player_action == "call":
                    bet_amount = players[0].bet_amount
                else:
                    bet_amount = 0  # Fold or check (no bet)
            else:
                # CPU players make automated bet decisions (based on limit rules)
                if round_num == 0:
                    # First betting round (bring-in)
                    bet_amount = BRING_IN_AMOUNT
                elif round_num == 1:
                    # Second betting round (small bet)
                    bet_amount = SMALL_BET_AMOUNT
                elif round_num == 2:
                    # Third betting round (big bet)
                    bet_amount = BIG_BET_AMOUNT
                else:
                    bet_amount = 0  # No bet (fold or check)
                print_colored(f"{player.name} bets: {bet_amount}", COLOR_BLUE)  # Print CPU player's action in blue
            player.bet(bet_amount)  # Pass the bet amount to the bet method

        # Card drawing phase (deal one card to each player)
        for player in players:
            new_card = deck.deal_card()
            player.receive_card(new_card)
            print(f"{player.name} draws: {new_card}")

    # Showdown - evaluate hands and determine winner
    print("\n--- Showdown ---")
    for player in players:
        print(f"{player.name}'s hand: {', '.join(str(card) for card in player.hand)}")

    # Determine winner based on hand evaluation
    winner = max(players, key=lambda player: utils.evaluate_hand(player.hand))
    print(f"\nWinner: {winner.name} with {utils.evaluate_hand(winner.hand)}")

if __name__ == "__main__":
    main()
