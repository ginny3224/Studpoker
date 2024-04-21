from PyQt5 import QtWidgets, QtCore
from game import Game

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = Game()

        # Create GUI elements
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.player_label = QtWidgets.QLabel("Player 1")
        self.bet_button = QtWidgets.QPushButton("Bet")
        self.fold_button = QtWidgets.QPushButton("Fold")
        self.chips_label = QtWidgets.QLabel("Chips: 1000")

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.player_label)
        layout.addWidget(self.bet_button)
        layout.addWidget(self.fold_button)
        layout.addWidget(self.chips_label)
        self.central_widget.setLayout(layout)

        # Connect buttons to game logic
        self.bet_button.clicked.connect(self.game.bet)
        self.fold_button.clicked.connect(self.game.fold)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gui = GUI()
    gui.show()
    app.exec_()