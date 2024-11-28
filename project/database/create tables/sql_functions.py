import pymysql
import sys
import pwinput
import pymysql.cursors
from pymysql.err import MySQLError

def get_db_information() -> tuple[str, str] | None:
    try:
        database = str(input("Enter the name of your MySQL database:\n"))
        password = str(pwinput.pwinput("Enter the password for your MySQL:\n"))
        return database, password
    except Exception as e:
        sys.exit(f"Invalid input : {e}.")

    
def create_connection(database: str, password: str) -> pymysql.connections.Connection | None:
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password=password,
            database=database)
        return connection        
    except MySQLError as e:
        sys.exit(f"Database connection failed: {e}.")


def create_cursor(connection: pymysql.connections.Connection) -> pymysql.cursors.Cursor | None:
    try:
        cursor = connection.cursor()
        return cursor
    except MySQLError as e:
        sys,exit(f"Error creating cursor: {e}.")

def close_cursor_and_connection(cursor: pymysql.cursors.Cursor, connection: pymysql.connections.Connection) -> None:
    try:
        cursor.close()
        connection.close()
    except MySQLError as e:
        sys.exit(f"Error closing connection: {e}.")


if __name__ == "__main__":
    db, pw = get_db_information()
    connection = create_connection(db, pw)
    cursor = create_cursor(connection)
    cursor.execute("""CREATE TABLE IF NOT EXISTS project(
                id INT,
                age INT
                )""")
    close_cursor_and_connection(cursor, connection)