from PyQt5.QtCore import *
import paramiko
import os, sys
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class UploadFiles(QRunnable, Ui_MainWindow):
    def __init__(self, user, host, password, port_number, path, file,):
        super(UploadFiles, self).__init__()
        self.host = host
        self.user = user
        self.password = password
        self.port_number = 22
        self.path = path
        self.file = file
        self.remote = '/mnt/ftp/'
    @pyqtSlot()
    def run(self):
        try:
            destination = self.remote + self.file
            print(destination)
            transport = paramiko.Transport(self.host, self.port_number)
            transport.connect(None, self.user, self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.path, destination)
            print("Upload Done")
        except TypeError:
            print("Unable to upload files, may need to make changes in code, as there are several bugs that still need fixing")
            print("Several options are hardcoded.")
