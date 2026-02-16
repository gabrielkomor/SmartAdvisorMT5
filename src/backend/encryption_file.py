"""
This file contains functions that are used to encrypt data stored in the database.
"""

from passlib.hash import argon2
from cryptography.fernet import Fernet
from hashlib import sha256

key = b"wQk2-stOKQ7v-Oos3KSHPqRWEsSilKCcNE5iH2mjmRQ="


def encrypt_password(password: str) -> str:
    """
    This function is responsible for hashing user password.
    :param password: unhashed password.
    :return: hashed password.
    """
    hashed_password = argon2.hash(password)
    return hashed_password


def verify_hashed_password(password: str, saved_hashed_password: str) -> bool:
    """
    This function is responsible for compare passwords.
    :param password: current password.
    :param saved_hashed_password: saved password.
    :return: boolean.
    """
    if argon2.verify(password, saved_hashed_password):
        return True
    else:
        return False


def encrypt(password: str) -> str:
    """
    This function is responsible for encrypt password.
    :param password: password.
    :return: encrypted password.
    """
    cipher = Fernet(key)
    encrypted = cipher.encrypt(password.encode())
    return encrypted.decode()


def decrypt(password: str) -> str:
    """
    This function is responsible for password decryption.
    :param password: encrypted password.
    :return: decrypted password.
    """
    cipher = Fernet(key)
    decrypted = cipher.decrypt(password.encode()).decode()
    return decrypted


def encrypt_email(text: str) -> str:
    """
    This function is responsible for email address encryption.
    :param text: user email.
    :return: encrypted email.
    """
    return sha256(text.encode()).hexdigest()
