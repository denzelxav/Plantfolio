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
    SELECT pd.plant_id, ppm.pruning_month
    FROM plant_details pd
    INNER JOIN plant_pruning_months ppm ON pd.plant_id = ppm.plant_id
    WHERE ppm.pruning_month IN ("June", "July", "August")
    """

    test2 = """
    SELECT pd.plant_id, po.origin, ppm.pruning_month
    FROM plant_details pd
    INNER JOIN plant_origins po ON pd.plant_id = po.plant_id
    INNER JOIN plant_pruning_months ppm ON pd.plant_id = ppm.plant_id
    WHERE po.origin = 'Brazil'
    AND ppm.pruning_month = 'July'
    """
    query_from_database(test2, output_to_file=True)
