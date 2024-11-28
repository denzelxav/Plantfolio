import pymysql
import json

def get_db_information() -> tuple[str, str] | None:
    try:
        database = str(input("Enter the name of your MySQL database:\n"))
        passwd = str(input("Enter the password for your MySQL:\n"))
    except:
        print("Invalid input.")
        return 
    return database, passwd
    
def create_connection(database: str, passwd: str) -> pymysql.connections.Connection:
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password=passwd,
            database=database)
    except:
        print("Connection failed.")
        return
    return connection

def create_cursor(connection: pymysql.connections.Connection) -> pymysql.cursors.Cursor:
    try:
        cursor = connection.cursor()
    except:
        print("Cursor creation failed.")
        return
    return cursor


if __name__ == "__main__":
    db, pw = get_db_information()
    connection = create_connection(db, pw)
    cursor = create_cursor(connection)
    cursor.execute("""CREATE TABLE IF NOT EXISTS project(
                id INT,
                age INT
                )""")