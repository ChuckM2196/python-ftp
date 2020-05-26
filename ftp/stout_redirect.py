from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
import sys, os
from MainWindow import Ui_MainWindow

# The new Stream Object which replaces the default stream associated with sys.stdout
# This object just puts data in a queue
class WriteStream(object):
    def __init__(self, queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)


# A QObject (something that recieves events, to be run in a QThread) which sits waiting for the data to come through Queue.Queue()
# It blocks until data is available, and once its got something from the queue, it sends it to the main thread
# by emitting q Qt Signal

class MyReciever(QObject):
    mysignal = pyqtSignal(str)

    def __init__(self, queue, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.queue = queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.mysignal.emit(text)

# QObject which outputs information with print # This is where I can put the sdtout and stderr redirect
class PrintOutput(QObject):
    @pyqtSlot()
    def run(self):
        sys.stdout = open(self.infoBox, 'a')
        sys.stderr = open(self.infoBox, 'a')








