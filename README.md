# Python Keylogger

A Python-based keylogger that securely tracks keystrokes, clipboard activity, active window changes, and periodic screenshots. All logs are encrypted for privacy and security.

## Features

- **Keystroke Logging:** Records every key pressed with timestamps.
- **Active Window Tracking:** Logs the title of the active window when it changes.
- **Clipboard Monitoring:** Captures clipboard (copy-paste) activity.
- **Screenshot Capture:** Takes screenshots at regular intervals.
- **Encrypted Logs:** All logs are encrypted using Fernet symmetric encryption.
- **Hotkey Stop:** Stop all logging instantly with `Ctrl+Shift+Alt+M`.

## Usage

1. **Clone the repository and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate an encryption key (only once):**
   ```bash
   python generate_key.py
   ```

3. **Run the keylogger:**
   ```bash
   python main.py
   ```

4. **View decrypted logs:**
   ```bash
   python decrypt_logs.py
   ```

## Security & Ethics

> **Warning:**  
> This tool is for educational and authorized security testing purposes only.  
> Do not use it on any system without explicit permission. Unauthorized use is illegal and unethical.

## License

This project is licensed for educational use only.

---

**Created by Abhiram Hosmane**
