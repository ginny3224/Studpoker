from game import StudGame
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout

class StudGameGUI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Stud Poker Game")

        # Create input fields for player chips, small blind, and big blind
        self.chips_label = QLabel("Player Chips:")
        self.chips_entry = QLineEdit()

        self.small_blind_label = QLabel("Small Blind:")
        self.small_blind_entry = QLineEdit()

        self.big_blind_label = QLabel("Big Blind:")
        self.big_blind_entry = QLineEdit()

        # Create button to start the game
        self.start_game_button = QPushButton("Start Game")
        self.start_game_button.clicked.connect(self.start_game)

        # Create text area to display game output
        self.text_area = QTextEdit()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.chips_label)
        layout.addWidget(self.chips_entry)
        layout.addWidget(self.small_blind_label)
        layout.addWidget(self.small_blind_entry)
        layout.addWidget(self.big_blind_label)
        layout.addWidget(self.big_blind_entry)
        layout.addWidget(self.start_game_button)
        layout.addWidget(self.text_area)

        self.window.setLayout(layout)

        self.window.show()
        print("GUI created successfully")

    def start_game(self):
        # Get player chips, small blind, and big blind from input fields
        chips = int(self.chips_entry.text())
        small_blind = int(self.small_blind_entry.text())
        big_blind = int(self.big_blind_entry.text())

        # Create a new game instance
        game = StudGame(7, chips, small_blind, big_blind)

        # Play the game
        winner = game.play_round()

        # Display player up cards in the GUI
        player_up_cards = game.get_player_up_cards()
        self.text_area.append("Player Up Cards:")
        for card in player_up_cards:
            self.text_area.append(f"{card[0]} of {card[1]}")

        # Display game output in the text area
        self.text_area.append(f"Winner: {winner}")

if __name__ == "__main__":
    gui = StudGameGUI()
    sys.exit(gui.app.exec_())