from typing import Optional, Tuple

from ai_notes_generator.db import get_db


def create_users_table() -> None:
    connection = get_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def register_user(username: str, password: str) -> None:
    if not username or not password:
        raise ValueError("Username and password are required.")

    create_users_table()

    connection = get_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password),
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def login_user(username: str, password: str) -> Optional[Tuple]:
    if not username or not password:
        return None

    create_users_table()

    connection = get_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, password),
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()