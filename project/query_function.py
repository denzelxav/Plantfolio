import os
import sys
import sqlite3
from tabulate import tabulate


def query_from_database(query: str, output_to_file: bool=False) -> list[tuple[str | int, ...]]:
    """
    Queries the database and returns the result in a txt file, database_output.txt
    """
    # Connect to the database and execute the query
    if getattr(sys, 'frozen', False):
        db_file = os.path.join(sys._MEIPASS, 'plant_database.db')

    elif __file__:
        db_file = os.path.join(os.path.dirname(__file__), 'plant_database.db')


    with sqlite3.connect(db_file) as conn:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(query)

        column_names = [description[0] for description in cursor.description]
        result = cursor.fetchall()


    if output_to_file:
        output_path = os.path.join('database', 'database_output.txt')
        with open(output_path, 'w', encoding='utf-8') as file:
            table = tabulate(result, headers=column_names, tablefmt='pretty', numalign='center')
            file.write(str(table))

    return result
