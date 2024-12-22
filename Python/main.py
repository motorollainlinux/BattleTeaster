from PyQt5 import QtCore, QtWidgets, uic
import sys, Btn_func

class BattleTeaster(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi("Battle-Teaster.ui", self)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = BattleTeaster()
    Window.show()
    sys.exit(app.exec_())