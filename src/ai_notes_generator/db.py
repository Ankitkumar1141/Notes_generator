import mysql.connector
from mysql.connector.connection import MySQLConnection

from ai_notes_generator.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def get_db() -> MySQLConnection:
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD is missing. Check your .env file.")

    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )