import sys
from PyQt5.QtWidgets import (QApplication, QAction, QWidget, QToolTip, QPushButton, QDesktopWidget, QMainWindow, QFileDialog, QTextEdit)
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar().showMessage("Current Status: Ready")
        self.resize(250, 150)
        self.setWindowTitle('OCR-GUI')

        openFile = QAction(QIcon("open.png"), "open", self)
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)
        
        self.center()

        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ma = MyApp()
    sys.exit(app.exec_())



