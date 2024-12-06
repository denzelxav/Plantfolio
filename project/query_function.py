import os
import sqlite3
from tabulate import tabulate


def query_from_database(query: str, output_to_file: bool=False) -> list[tuple[str | int]]:
    """
    Queries the database and returns the result in a txt file, database_output.txt
    """
    try:
        # Connect to the database and execute the query
        db_file = os.path.join('project', 'plant_database.db')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(query)

        column_names = [description[0] for description in cursor.description]
        result = cursor.fetchall()

    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        # Close the connection to the database
        conn.close()

    if output_to_file:
        try:
            # Open output file and write the result to it
            output_path = os.path.join('database', 'database_output.txt')
            with open(output_path, 'w', encoding='utf-8') as file:
                table = tabulate(result, headers=column_names, tablefmt='pretty', numalign='center')
                file.write(str(table))
        except Exception as e:
            print(f"An error occured: {e}")

    return result


if __name__ == '__main__':
    test_query = """
SELECT * FROM all_names
"""
    query_from_database(test_query, output_to_file=True)
