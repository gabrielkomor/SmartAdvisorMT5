"""
This file is responsible for communication between the application and the database.
"""

import sqlite3
from typing import Any


def create_db(name: str) -> None:
    """
    This function is responsible for creating new database and table.
    :param name: table name.
    :return: nothing.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(f"""
            CREATE TABLE If NOT EXISTS {name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email STRING,
                password STRING,
                secret STRING
            )
        """)

    db.commit()
    db.close()


def save_email_in_db(name: str, email: str) -> None:
    """
    This function is responsible for saving email in database.
    :param name: table name.
    :param email: user email.
    :return: nothing.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        INSERT INTO {name} (email, password, secret) VALUES (?, NULL, NULL)
    """,
        (email,),
    )

    db.commit()
    db.close()


def save_password_in_db(name: str, email: str, password: str) -> None:
    """
    This function is responsible for save password in database.
    :param name: table name.
    :param email: user email.
    :param password: user password.
    :return: nothing.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        UPDATE {name} SET password = ? WHERE email = ?
    """,
        (password, email),
    )

    db.commit()
    db.close()


def save_secret_in_db(name: str, email: str, secret: str) -> None:
    """
    This function is responsible for saving secret in database.
    :param name: table name.
    :param email: user email.
    :param secret: secret.
    :return: nothing.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        UPDATE {name} SET secret = ? WHERE email = ?
    """,
        (secret, email),
    )

    db.commit()
    db.close()


def get_secret_from_db(name: str, email: str) -> str:
    """
    This function is responsible for fetching secret from database.
    :param name: table name.
    :param email: user email.
    :return: secret.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        SELECT secret FROM {name} WHERE email = ?
    """,
        (email,),
    )

    secret = cursor.fetchone()
    db.close()
    return secret[0]


def get_password_from_db(name: str, email: str) -> Any:
    """
    This function is responsible for fetching password from database.
    :param name: table name.
    :param email: user email.
    :return: user password.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        SELECT password FROM {name} WHERE email = ?
    """,
        (email,),
    )

    password = cursor.fetchone()
    db.close()

    if password:
        return password[0]
    else:
        return None


def check_email_in_db(name: str, email: str) -> bool:
    """
    This function checks if email exist in database.
    :param name: table name.
    :param email: user email.
    :return: boolean.
    """
    db = sqlite3.connect("src\\database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        SELECT email FROM {name} WHERE email = ?
    """,
        (email,),
    )

    result = cursor.fetchone()

    db.close()
    if result is not None:
        return True
    else:
        return False
