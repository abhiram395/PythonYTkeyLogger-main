import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def decrypt_logs():
    fernet = Fernet(load_key())
    output.delete(1.0, tk.END)
    try:
        with open("log.txt", "rb") as log_file:
            for line in log_file:
                try:
                    decrypted = fernet.decrypt(line.strip()).decode()
                    output.insert(tk.END, decrypted + "\n")
                except Exception as e:
                    output.insert(tk.END, "[Could not decrypt line]\n")
    except FileNotFoundError:
        output.insert(tk.END, "log.txt not found.\n")

root = tk.Tk()
root.title("Decrypted Keylogger Logs")

output = ScrolledText(root, width=80, height=30)
output.pack(padx=10, pady=10)

btn = tk.Button(root, text="Load Logs", command=decrypt_logs)
btn.pack(pady=5)

root.mainloop()