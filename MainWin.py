# Import any modules we need
import random
import time
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_MainWin import Ui_MainWindow

class MainWindow:
    # Initiliaze the program
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Connect signals to slots
        self.ui.boyButton.clicked.connect(self.on_boy_button_clicked)
        self.ui.girlButton.clicked.connect(self.on_girl_button_clicked)

    # Show the main window
    def show(self):
        self.main_win.show()

    def on_boy_button_clicked(self):
        f = open('boy_names.txt', 'r')
        names = f.read().splitlines()
        f.close()
        random.shuffle(names)
        finalBoyName = names[0]
        self.ui.label.setText(finalBoyName)

    def on_girl_button_clicked(self):
        f = open('girl_names.txt', 'r')
        names = f.read().splitlines()
        f.close()
        random.shuffle(names)    
        finalGirlName = names[0]
        self.ui.label.setText(finalGirlName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())