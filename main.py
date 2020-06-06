import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import  QtCore
from PyQt5.QtCore import pyqtSlot
import numpy as np

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Würfel-o-Mate'
        self.left = 20
        self.top = 20
        self.width = 280
        self.height = 120
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.lineEditCount = QtWidgets.QLineEdit(self)
        self.lineEditCount.setGeometry(QtCore.QRect(20, 50, 41, 31))
        self.lineEditCount.setObjectName("lineEditCount")
        self.plainTextErgebnis = QtWidgets.QPlainTextEdit(self)
        self.plainTextErgebnis.setEnabled(False)
        self.plainTextErgebnis.setGeometry(QtCore.QRect(20, 10, 241, 31))
        self.plainTextErgebnis.setObjectName("plainTextErgebnis")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 50, 71, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEditNumberOfSides = QtWidgets.QLineEdit(self)
        self.lineEditNumberOfSides.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.lineEditNumberOfSides.setObjectName("lineEditNumberOfSides")
        self.pushButtonRoll = QtWidgets.QPushButton(self)
        self.pushButtonRoll.setGeometry(QtCore.QRect(90, 90, 75, 23))

        self.pushButtonRoll.clicked.connect(self.on_click)

        self.retranslateUi()

        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.plainTextErgebnis.setPlainText(_translate("MainWindow", "Ergebnis:"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "x W"))
        self.pushButtonRoll.setText(_translate("MainWindow", "Roll"))

    @pyqtSlot()
    def on_click(self):
        try:
            count = int(self.lineEditCount.text())
            sides = int(self.lineEditNumberOfSides.text())
        except Exception:
            self.plainTextErgebnis.setPlainText("Schreib hald bitte was gescheites rein!")
            return

        ergebnis = 0
        for i in range(count):
            ergebnis += ((np.random.uniform() * sides)+1) // 1
        self.plainTextErgebnis.setPlainText("Ergebnis: "+str(int(ergebnis)))
        dumm = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())