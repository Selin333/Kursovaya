import sys

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QApplication


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(200,200)

        self.btn = QPushButton('Open file', self)
        self.btn.move(35,50)
        self.btn.clicked.connect(self.knipka1)




    def knipka1(self):
        res = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self,'Open File', 'D:\\111\\Kursovaya','txt file(*.txt)')
        print(res)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())