python-ftp.py - A PyQt5 and Python 3 based FTP program.

Upload and Download files, Create and Delete files and directories, basing the program off of FileZilla.

# Requirements: See requirements.txt

# Known Bugs
Currently destination directory for file uploading is hard coded. This is planning on being changed and is only for testing

Only IP addresses are usable

Port Number is hardcoded. 

Several Errors with crashing

Programs connects to FTP server then disconnects per file upload. This is planning on being changed.

# Optional Functions:
- SSH without needing password
- Automatic directory refresh
- Connect to FTP server via hostname

# CHANGELOG #
5/25/2020: Successfully redirected text to the QTextEditWidget

5/21/2020: Able to connect and disconnect from FTP Server. Redesigned GUI. Connection and Disconnections are running on seperate
threads from the main GUI

5/25/2020: Successfully redirected text to the QTextEdit Widget

5/21/2020: Able to connect and disconnect from FTP server. Redesigned GUI. Connection and Disconnections are running on seperate threads from the main GUI

5/17/2020: Intial Commit - Able to load GUI. No buttons have any functions.
