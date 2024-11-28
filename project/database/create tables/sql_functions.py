import pymysql
import sys
import pwinput
import pymysql.cursors
from pymysql.err import MySQLError
import os

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

def execute_sql_file(cursor: pymysql.cursors.Cursor, sql_file_path: str) -> None:
    try:
        if not os.path.exists(sql_file_path):
            sys.exit(f"SQL file not found: {sql_file_path}")

        with open(sql_file_path) as file:
            query = file.read()

        for statement in query.split(";"):
            if statement.strip():
                cursor.execute(statement)
        print("SQL file executed successfully.")
    except MySQLError as e:
        sys.exit(f"Error executing query: {e}")
    except Exception as e:
        sys.exit(f"Error reading file: {e}")


if __name__ == "__main__":
    db, pw = get_db_information()
    connection = create_connection(db, pw)
    cursor = create_cursor(connection)
    sql_file = os.path.join("project", "database", "create tables", "create_staging_table.sql")
    execute_sql_file(cursor, sql_file)
    close_cursor_and_connection(cursor, connection)