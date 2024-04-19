from gui import StudGameGUI
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    gui = StudGameGUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()