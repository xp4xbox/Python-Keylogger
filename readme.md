# Python Keylogger

This program is an object oriented windows keylogger written in python3.

![](https://i.imgur.com/RIORDBw.png)

## Installation

This program requires:
* [Python3](https://www.python.org/downloads/)
* [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* [Pynput](https://pypi.org/project/pynput/)
* [Pyinstaller](https://pypi.org/project/PyInstaller/)

1. Download the repository using github or git.
2. Install the modules above one by one or install them all at once by running `python -m pip install -r requirements.txt`

## Features
* Ability to send logs to any gmail account.
* Ability to store logs locally.
* Ability to add to startup.
* Ability to log special characters.
* Ability to capture window mouse clicks.
* Ability to check for sandboxie/virtual machine.
* And more...

## Usage

1. Navigate to `src` in windows explorer.
2. Right-click while holding shift to open powershell window.
3. Run `python setup.py` to build the .exe.
4. Open the `dist` folder and run the compiled .exe.
5. To stop the prgoram enter `shift+F1` or kill the program in task manager.

> NOTE: Env Variables such as `%userprofile%` and `%tmp%` are allowed in the log path.
