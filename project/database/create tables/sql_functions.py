import pymysql
import sys
import pwinput
import pymysql.cursors
from pymysql.err import MySQLError
import os
import json


def get_db_information() -> tuple[str, str]:
    try:
        database = input("Enter the name of your MySQL database:\n").strip()
        password = pwinput.pwinput("Enter the password for your MySQL:\n").strip()
        return database, password
    except Exception as e:
        sys.exit(f"Invalid input: {e}")


def create_connection(database: str, password: str) -> pymysql.connections.Connection:
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password=password,
            database=database
        )
        return connection
    except MySQLError as e:
        sys.exit(f"Database connection failed: {e}")


def execute_sql_file(connection: pymysql.connections.Connection, sql_file_path: str) -> None:
    try:
        if not os.path.exists(sql_file_path):
            raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

        with open(sql_file_path, "r") as file:
            queries = file.read()

        with connection.cursor() as cursor:
            for statement in queries.split(";"):
                if statement.strip():
                    cursor.execute(statement)
            connection.commit()

        print("SQL file executed successfully.")

    except MySQLError as e:
        sys.exit(f"Error executing query: {e}")
    except Exception as e:
        sys.exit(f"Error reading file: {e}")


def insert_json_into_table(connection: pymysql.connections.Connection, json_path: str, table_name: str) -> None:
    try:
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"File not found: {json_path}")

        with open(json_path, "r") as file:
            json_data = json.load(file)

        with connection.cursor() as cursor:
            for item in json_data:
                cursor.execute(
                    f"INSERT INTO {table_name} (json_data) VALUES (%s)",
                    (json.dumps(item),)
                )
            connection.commit()

        print(f"JSON data inserted into table `{table_name}` successfully.")
    except FileNotFoundError as e:
        sys.exit(f"{e}")
    except MySQLError as e:
        sys.exit(f"Database error: {e}")
    except Exception as e:
        sys.exit(f"Error processing JSON file: {e}")


