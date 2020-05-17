# python-ftp -> A PyQT and Python 3 based FTP program.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from MainWindow import Ui_MainWindow
import os, sys, ftplib

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.hostEdit.setPlaceholderText("IP / Host")
        self.usernameEdit.setPlaceholderText("Enter Username")
        self.passwordEdit.setPlaceholderText("Enter Password")
        self.portEdit.setPlaceholderText("Default 22")
        # Started Program Events

        # Events for when the buttons are clicked
        self.connectButton.pressed.connect(self.establish_connection)


    # Individual events

    # Establishes connection from local computer to remote device
    def establish_connection(self):
        host = self.hostEdit.text()
        user = self.usernameEdit.text()
        pw = self.passwordEdit.text()
        print(host, user, pw)
        return host, user, pw



# Running the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()