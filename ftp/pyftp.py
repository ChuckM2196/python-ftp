#python-ftp -> A PyQT and Python 3 based FTP program

from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from MainWindow import Ui_MainWindow
import os, sys, time
from connect_threads import WorkerSignals, WorkerConnect
from disconnect_threads import WorkerSignals, WorkerDisconnect
from stout_redirect import WriteStream, MyReciever, PrintOutput
from queue import Queue
from upload_files import UploadFiles




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.hostEdit.setPlaceholderText("IP / Host")
        self.usernameEdit.setPlaceholderText("Enter Username")
        self.passwordEdit.setPlaceholderText("Enter Password")
        self.portEdit.setPlaceholderText("Default 22")

        # Handles queuing and execution of threads
        self.threadpool = QThreadPool()

        # Events for when the buttons are clicked
        self.connectButton.pressed.connect(self.establish_connection)
        self.disconnectButton.pressed.connect(self.disconnect_connection)
        self.UploadButton.pressed.connect(self.upload_files)

    # Establishes connection from local computer to remote device
    def establish_connection(self):
        hostname = self.hostEdit.text()
        u_name = self.usernameEdit.text()
        pw = self.passwordEdit.text()
        port = 22

        self.connect = WorkerConnect(host=hostname, user=u_name, port_number=port, password=pw)
        self.threadpool.start(self.connect)
        return hostname, u_name, pw, port

    # Disconnects from the remote device
    def disconnect_connection(self):
        hostname = self.hostEdit.text()
        port = self.portEdit.text()
        if not port:
            port = 22
        self.disconnect = WorkerDisconnect(host=hostname, port_number=port)
        self.threadpool.start(self.disconnect)

    # Upload button - upload files to FTP Server
    def upload_files(self):
        hostname = self.hostEdit.text()
        u_name = self.usernameEdit.text()
        pw = self.passwordEdit.text()
        port = self.portEdit.text()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Upload Files", "", "All Files (*);; Text Files *.(txt)", options=options)
        print(f'You have selected {file_path} for a remote directory transfer')
        path, file = os.path.split(file_path)



        # File uploading will be attached to another thread
        self.ftp_save = UploadFiles(host=hostname, password=pw, user=u_name, port_number=port, path=file_path, file=file)
        self.threadpool.start(self.ftp_save)




    # Slots that reacts to events from the application starting, help connect things together.

    # Appends text to the end of infoBox
    @pyqtSlot(str)
    def append_text(self, text):
        self.infoBox.moveCursor(QTextCursor.End)
        self.infoBox.insertPlainText(text)

    # Threads that runs that, outputs information to infoBox
    @pyqtSlot()
    def start_thread(self):
        self.thread = QThread()
        self.printoutput = PrintOutput()
        self.printoutput.moveToThread(self.thread)
        self.thread.started.connect(self.printoutput.run)
        self.thread.start()

# Create the Queue and redirect sys.stdout to this queue
queue = Queue()
sys.stdout = WriteStream(queue)


# Starting the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Create thread that will listen on the other end of the queue and send the text to the textedit in our application
thread = QThread()
my_reciever = MyReciever(queue)
my_reciever.mysignal.connect(window.append_text)
my_reciever.moveToThread(thread)
thread.started.connect(my_reciever.run)
thread.start()

# Application running
app.exec_()


