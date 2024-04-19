import tkinter as tk
from game import StudGame

class StudGameGUI:
    def __init__(self):
        print("StudGameGUI __init__ called")
        self.root = tk.Tk()
        self.root.title("Stud Poker Game")

        # Create input fields for player chips, small blind, and big blind
        tk.Label(self.root, text="Player Chips:").pack()
        self.chips_entry = tk.Entry(self.root)
        self.chips_entry.pack()

        tk.Label(self.root, text="Small Blind:").pack()
        self.small_blind_entry = tk.Entry(self.root)
        self.small_blind_entry.pack()

        tk.Label(self.root, text="Big Blind:").pack()
        self.big_blind_entry = tk.Entry(self.root)
        self.big_blind_entry.pack()

        # Create button to start the game
        tk.Button(self.root, text="Start Game", command=self.start_game).pack()

        # Create text area to display game output
        self.text_area = tk.Text(self.root)
        self.text_area.pack()

    def start_game(self):
        print("Start game called")
        # Get player chips, small blind, and big blind from input fields
        chips = int(self.chips_entry.get())
        small_blind = int(self.small_blind_entry.get())
        big_blind = int(self.big_blind_entry.get())

        # Create a new game instance
        game = StudGame(7, chips, small_blind, big_blind)

        # Play the game
        winner = game.play_round()

        # Display player up cards in the GUI
        player_up_cards = game.get_player_up_cards()
        self.text_area.insert(tk.END, "Player Up Cards:\n")
        for card in player_up_cards:
            self.text_area.insert(tk.END, f"{card[0]} of {card[1]}\n")

        # Display game output in the text area
        self.text_area.insert(tk.END, f"Winner: {winner}")

if __name__ == "__main__":
    gui = StudGameGUI()
    gui.root.mainloop()