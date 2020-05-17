# python-ftp -> A PyQT and Python 3 based FTP program.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import os, sys

app = QApplication(sys.argv)
window = uic.loadUi('../mainwindow.ui')
window.show()
app.exec_()