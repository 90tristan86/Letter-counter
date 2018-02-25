import sys
import os
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Count seconds'
        self.left = 10
        self.top = 10
        self.width = 280
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 30)
        self.textbox.resize(230, 40)
        self.center()

        # Create a button in the window
        self.button = QPushButton('Розрахувати', self)
        self.button.resize(self.button.sizeHint())
        self.button.move(80, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.statusBar().showMessage('Вуличне радiо')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        count = round((len(textboxValue)*0,09), 2)
        counted = str(count)
        QMessageBox.question(self, 'Message', "Тривалсiть ролику: " + counted, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'logo.icns')
    app.setWindowIcon(QIcon(path))
    ex = App()
    sys.exit(app.exec_())
