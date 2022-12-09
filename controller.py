from PyQt5.QtWidgets import *
from view import *
from random import randint

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """A class for the controller, contains the play methods, reset method and initial state method"""

    def __init__(self, *args, **kwargs):
        """Constructor to create initial state of class object"""

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cardNumberTop.setText('?')  # Set card numbers to question mark when game is first started
        self.cardNumberMiddle.setText('?')
        self.cardNumberBottom.setText('?')
        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        self.LowButton.clicked.connect(lambda: self.playLow())
        self.HighButton.clicked.connect(lambda: self.playHigh())
        self.resetButton.clicked.connect(lambda: self.reset())
        self.balance = int(100)

    def playLow(self):
        """Method checks if balance is greater than 0 (zero) and generates random number between 1-10 for the
        Low number guess """

        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        if self.balance > int(0):
            number = randint(1, 10)
            self.cardNumberTop.setText(f'{number}')
            self.cardNumberMiddle.setText(f'{number}')
            self.cardNumberBottom.setText(f'{number}')
            if number > 5:
                self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
                self.balance = self.balance - 10
                self.balanceCounter.setText(f'{self.balance}')
                if self.balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
            if number < 6:
                self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
                self.balance = self.balance + 10
                self.balanceCounter.setText(f'{self.balance}')
                if self.balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
        else:
            self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def playHigh(self):
        """Method checks if balance is greater than 0 (zero) and generates random number between 1-10 for the
        High number guess"""

        self.errorLabel.setText('Choose High or Low\nLow (1-5) High (6-10)')
        if self.balance > int(0):
            number = randint(1, 10)
            self.cardNumberTop.setText(f'{number}')
            self.cardNumberMiddle.setText(f'{number}')
            self.cardNumberBottom.setText(f'{number}')
            if number > 5:
                self.winOrLoseLabel.setText('Congratulations, you won!\nClick High or Low to play again')
                self.balance = self.balance + 10
                self.balanceCounter.setText(f'{self.balance}')
                if self.balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
            if number < 6:
                self.winOrLoseLabel.setText(f'Sorry, you guessed wrong!\nThe number was {number}')
                self.balance = self.balance - 10
                self.balanceCounter.setText(f'{self.balance}')
                if self.balance < 1:
                    self.errorLabel.setText('You have a balance of 0\nClick reset to play again')
        else:
            self.errorLabel.setText('You have a balance of 0\nClick reset to play again')

    def reset(self):
        """Reset method to reset balance to 100 if the value of balance is 0"""
        
        if self.balance == int(0):
            self.balance = self.balance + 100
            self.balanceCounter.setText(f'{self.balance}')
        else:
            self.errorLabel.setText('Balance must be zero before you can reset.')
