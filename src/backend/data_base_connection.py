import sqlite3
from typing import Any


def create_db(name: str) -> None:
    db = sqlite3.connect("database\\usersData.db")
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
    db = sqlite3.connect("database\\usersData.db")
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
    db = sqlite3.connect("database\\usersData.db")
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
    db = sqlite3.connect("database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        UPDATE {name} SET secret = ? WHERE email = ?
    """,
        (secret, email),
    )

    db.commit()
    db.close()


def delete_user_from_db(name: str, email: str) -> None:
    db = sqlite3.connect("database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(
        f"""
        DELETE FROM {name} WHERE email = ?
    """,
        (email,),
    )

    db.commit()
    db.close()


def delete_table_from_db(name: str) -> None:
    db = sqlite3.connect("database\\usersData.db")
    cursor = db.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {name}")

    db.commit()
    db.close()


def get_secret_from_db(name: str, email: str) -> str:
    db = sqlite3.connect("database\\usersData.db")
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
    db = sqlite3.connect("database\\usersData.db")
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
    db = sqlite3.connect("database\\usersData.db")
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
