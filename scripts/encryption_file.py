from passlib.hash import argon2
from cryptography.fernet import Fernet
from hashlib import sha256

key = b"wQk2-stOKQ7v-Oos3KSHPqRWEsSilKCcNE5iH2mjmRQ="


def encrypt_password(password: str) -> str:
    hashed_password = argon2.hash(password)
    return hashed_password


def verify_hashed_password(password: str, saved_hashed_password: str) -> bool:
    if argon2.verify(password, saved_hashed_password):
        return True
    else:
        return False


def encrypt(password: str) -> str:
    cipher = Fernet(key)
    encrypted = cipher.encrypt(password.encode())
    return encrypted.decode()


def decrypt(password: str) -> str:
    cipher = Fernet(key)
    decrypted = cipher.decrypt(password.encode()).decode()
    return decrypted


def encrypt_email(text: str) -> str:
    return sha256(text.encode()).hexdigest()
