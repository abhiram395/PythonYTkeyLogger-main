from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

fernet = Fernet(load_key())

with open("log.txt", "rb") as log_file:
    for line in log_file:
        try:
            print(fernet.decrypt(line.strip()).decode())
        except Exception as e:
            print("Could not decrypt a line:", e)