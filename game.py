import random
from PyQt5 import QtCore, QtGui, QtWidgets

class RockPaperScissorsGame:
    def __init__(self):
        """
        Initialize the RockPaperScissorsGame.

        Attributes:
        - user_score (int): User's score.
        - ai_score (int): AI's score.
        - possible_moves (List[str]): List of possible moves (rock, paper, scissors).
        """
        self.user_score: int = 0
        self.ai_score: int = 0
        self.possible_moves: List[str] = ["rock", "paper", "scissors"]

    def play_round(self, choice: str) -> str:
        """
        Play a round of Rock, Paper, Scissors.

        Parameters:
        - choice (str): The user's choice.

        Returns:
        - str: Result of the round.
        """
        computer_action: str = random.choice(self.possible_moves)

        if computer_action == "rock":
            return self.evaluate_round(choice, "paper", "rock", "scissors")
        elif computer_action == "paper":
            return self.evaluate_round(choice, "scissors", "paper", "rock")
        else:
            return self.evaluate_round(choice, "rock", "scissors", "paper")

    def evaluate_round(self, choice: str, win_move: str, tie_move: str, lose_move: str) -> str:
        """
        Evaluate the result of a round.

        Parameters:
        - choice (str): User's choice.
        - win_move (str): Winning move against the user's choice.
        - tie_move (str): Tying move against the user's choice.
        - lose_move (str): Losing move against the user's choice.

        Returns:
        - str: Result of the round.
        """
        result_tie: str = f"{choice}_tie"
        result_win: str = f"user_{choice}_win"
        result_lose: str = f"ai_{choice}_win"

        if choice == win_move:
            self.user_score += 1
            print("You Won!")
            return result_win
        elif choice == tie_move:
            print("You Tie!")
            return result_tie
        else:
            self.ai_score += 1
            print("You Lost!")
            return result_lose

class Ui_MainWindow(object):
    def __init__(self):
        self.game: RockPaperScissorsGame = RockPaperScissorsGame()
        
        
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 610)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rockButton = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton.setGeometry(QtCore.QRect(40, 420, 221, 101))
        self.rockButton.setObjectName("rockButton")
        self.paperButton = QtWidgets.QPushButton(self.centralwidget)
        self.paperButton.setGeometry(QtCore.QRect(280, 420, 221, 101))
        self.paperButton.setObjectName("paperButton")
        self.scissorButton = QtWidgets.QPushButton(self.centralwidget)
        self.scissorButton.setGeometry(QtCore.QRect(540, 420, 221, 101))
        self.scissorButton.setObjectName("scissorButton")
        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(210, 90, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.main_text.setFont(font)
        self.main_text.setTextFormat(QtCore.Qt.AutoText)
        self.main_text.setObjectName("main_text")
        self.side_label = QtWidgets.QLabel(self.centralwidget)
        self.side_label.setGeometry(QtCore.QRect(340, 160, 200, 16))
        self.side_label.setObjectName("side_label")
        self.main_image = QtWidgets.QLabel(self.centralwidget)
        self.main_image.setGeometry(QtCore.QRect(20, 190, 781, 211))
        self.main_image.setText("")
        self.main_image.setPixmap(QtGui.QPixmap("test.png"))
        self.main_image.setObjectName("main_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rockButton.clicked.connect(self.rockButton_command)
        self.paperButton.clicked.connect(self.paperButton_command)
        self.scissorButton.clicked.connect(self.scissorButton_command)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock, Paper, Scissors!"))
        self.rockButton.setText(_translate("MainWindow", "Rock"))
        self.paperButton.setText(_translate("MainWindow", "Paper"))
        self.scissorButton.setText(_translate("MainWindow", "Scissors"))
        self.main_text.setText(_translate("MainWindow", "Choose your hand!"))

    def update_image(self, result: str) -> None:
        """
        Update the main image based on the result.

        Parameters:
        - result (str): Result of the round.
        """
        self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
        self.main_image.setPixmap(QtGui.QPixmap(f"{result}.png"))
        
    def rockButton_command(self) -> None:
        """Handler for the Rock button click event."""
        result: str = self.game.play_round("rock")
        self.update_image(result)

    def paperButton_command(self) -> None:
        """Handler for the Paper button click event."""
        result: str = self.game.play_round("paper")
        self.update_image(result)

    def scissorButton_command(self) -> None:
        """Handler for the Scissors button click event."""
        result: str = self.game.play_round("scissors")
        self.update_image(result)

if __name__ == "__main__":
    import sys
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    MainWindow: QtWidgets.QMainWindow = QtWidgets.QMainWindow()
    ui: Ui_MainWindow = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
