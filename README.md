# PRODIGY_CS_04
Simple Keylogger
Simple Keylogger
This Python script implements a basic keylogger that records keystrokes and saves them into a log file.

How it Works
The keylogger uses the pynput library to capture keystrokes. When a key is pressed, it is logged into a file (keylog.txt). The keylogger continues to run in the background until the Esc key is pressed to stop it.

Requirements
Python 3.x
pynput library (pip install pynput)
Usage
Clone or download this repository to your local machine.
Install the required Python library using pip install pynput.
Run the script by executing python keylogger.py.
Press the Esc key to stop the keylogger.
Output
The recorded keystrokes are saved into a log file named keylog.txt. The log file is created in the same directory where the script is located. Each keystroke is logged as it is pressed, and the log file continues to grow as more keystrokes are recorded.

Note
This keylogger is for educational purposes only. Ensure that you have proper authorization before using it.
Use responsibly and respect the privacy of others.
