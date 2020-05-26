from PyQt5.QtCore import *
import paramiko
import sys

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
class WorkerConnect(QRunnable):

    def __init__(self, host, user, password, port_number):
        super(WorkerConnect, self).__init__()
        self.host = host
        self.user = user
        self.password = password
        self.port_number = port_number
        self.transport = paramiko.Transport((self.host, self.port_number))

    @pyqtSlot()
    def run(self):
        """This is going to connect to the server"""
        self.transport.connect(None, self.user, self.password)
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        files = sftp.listdir('/home/' + self.user)
        print(files)
        print(f"You're now connected to {self.host}")
        WorkerConnect.setAutoDelete(self, False)  # This is so the thread doesn't close as soon as you connect