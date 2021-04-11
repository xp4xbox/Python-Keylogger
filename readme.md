# Python Keylogger

This program is an object oriented windows keylogger written in python3.

![](https://i.imgur.com/RIORDBw.png)

## Installation

This program requires:
* [Python3](https://www.python.org/downloads/) (Make sure to add python to PATH during installation)
* [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
* [Pynput](https://pypi.org/project/pynput/)
* [WMI](https://pypi.org/project/WMI/)
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

> NOTE: Env Variables such as `%userprofile%` and `%tmp%` are allowed in the log path. Also, if sending logs to a gmail account, that account must have allowed access for less secure apps.

## Uninstallation

1. Enter `shift+F1` or kill the program in task manager.
2. If the program was added to startup, open regedit, navigate to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, and delete `winupdate` value.
