from PyQt5.QtCore import *
import paramiko
from MainWindow import Ui_MainWindow
import os

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread
    Supported signals are:
    finished -> No Data
    error -> 'tuple' (exctype, value, traceback.format_exec() )
    result -> 'object' data return from processing, anything
    '''

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

# This is a seperate thread from the GUI thread that is suppossed to connect you to the FTP server
class WorkerConnect(QRunnable, Ui_MainWindow):
    def __init__(self, host, user, password, port_number):
        super(WorkerConnect, self).__init__()
        super(Ui_MainWindow, self).__init__()
        self.host = host
        self.user = user
        self.password = password
        self.port_number = port_number

    @pyqtSlot()
    def run(self):
        """This is going to connect to the server"""
        try:
            transport = paramiko.Transport(self.host, self.port_number)
            transport.connect(None, self.user, self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            files = sftp.listdir('/home/' + self.user)
            print(files)
            print(f"You're now connected to {self.host}")
            WorkerConnect.setAutoDelete(self, False)
        except OSError:
            print("Unable to connect")
            WorkerConnect.setAutoDelete(self, False)
