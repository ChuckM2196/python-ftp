from PyQt5.QtCore import *
import paramiko

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
class WorkerDisconnect(QRunnable):

    def __init__(self, host, port_number):
        super(WorkerDisconnect, self).__init__()
        self.host = host
        self.port_number = port_number

    @pyqtSlot()
    def run(self):
        try:
            """This is going to discconnect you from the server"""
            transport = paramiko.Transport(self.host, self.port_number)
            if transport is not None:
                transport.close()
                print("The connection has been closed")
        except OSError:
            print("You're not connected to any server")
