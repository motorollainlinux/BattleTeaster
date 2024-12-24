from PyQt5 import QtCore, QtWidgets, uic
#          Menu         BS-B        BS-P        Battle      Settings    Leaders
Sizes = [[295, 369], [310, 330], [338, 330], [464, 579], [385, 295], [549, 744]]
class BattleTeaster(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi("./Assets/UI/Menu.ui", self)
        self.widget.setStyleSheet("background: url(\"./Assets/img/LOGO.png\") no-repet auto;")
        self.pushButton1.clicked.connect(self.ChangeToBotBattleSettings)
        self.pushButton2.clicked.connect(self.ChangeToPlayerBattleSettings)
        self.pushButton3.clicked.connect(self.ChangeToSettings)
        self.pushButton4.clicked.connect(self.ChangeToLeaders)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[0][0], Sizes[0][1])
    def ChangeToBotBattleSettings(self) -> None:
        uic.loadUi("./Assets/UI/BS-B.ui", self)
        self.pushButtonM1.setStyleSheet("background: url(\"./Assets/img/minuse 1 2 1.png\") no-repet auto;")
        self.pushButtonM2.setStyleSheet("background: url(\"./Assets/img/minuse 1 2 1.png\") no-repet auto;")
        self.pushButtonM3.setStyleSheet("background: url(\"./Assets/img/minuse 1 2 1.png\") no-repet auto;")
        self.pushButtonP1.setStyleSheet("background: url(\"./Assets/img/pluse 1 2 1.png\") no-repet auto;")
        self.pushButtonP2.setStyleSheet("background: url(\"./Assets/img/pluse 1 2 1.png\") no-repet auto;")
        self.pushButtonP3.setStyleSheet("background: url(\"./Assets/img/pluse 1 2 1.png\") no-repet auto;")
        self.pushButton4.clicked.connect(self.ChangeToMenu)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[1][0], Sizes[1][1])
    def ChangeToPlayerBattleSettings(self) -> None:
        uic.loadUi("./Assets/UI/BS-P.ui", self)
        self.pushButton4.clicked.connect(self.ChangeToMenu)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[2][0], Sizes[2][1])
    def ChangeToSettings(self) -> None:
        uic.loadUi("./Assets/UI/Settings.ui", self)
        self.pushButton.clicked.connect(self.ChangeToMenu)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[4][0], Sizes[4][1])
    def ChangeToBattle(self) -> None:
        uic.loadUi("./Assets/UI/Battle.ui", self)
        self.pushButton2.clicked.connect(self.ChangeToMenu)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[3][0], Sizes[3][1])
    def ChangeToLeaders(self) -> None:
        uic.loadUi("./Assets/UI/Leaders.ui", self)
        self.pushButton1.clicked.connect(self.ChangeToMenu)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[5][0], Sizes[5][1])
    def ChangeToMenu(self) -> None:
        uic.loadUi("./Assets/UI/Menu.ui", self)
        self.widget.setStyleSheet("background: url(\"./Assets/img/LOGO.png\") no-repet auto;")
        self.pushButton1.clicked.connect(self.ChangeToBotBattleSettings)
        self.pushButton2.clicked.connect(self.ChangeToPlayerBattleSettings)
        self.pushButton3.clicked.connect(self.ChangeToSettings)
        self.pushButton4.clicked.connect(self.ChangeToLeaders)
        self.setMinimumSize(0, 0)
        self.resize(Sizes[0][0], Sizes[0][1])
        
        
        
        
