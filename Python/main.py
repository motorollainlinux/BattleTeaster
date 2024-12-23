from PyQt5 import QtCore, QtWidgets, uic
import sys, Btn_func
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = Btn_func.BattleTeaster()
    Window.show()
    sys.exit(app.exec_())