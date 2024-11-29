import os
import sys
from sql_functions import get_db_information, create_connection, execute_sql_file, insert_json_into_table


def main():
    try:
        database, password = get_db_information()
        connection = create_connection(database, password)
        try:
            sql_file_path = os.path.join("project", "database", "create tables", "create_staging_table.sql")
            execute_sql_file(connection, sql_file_path)

            json_file_path = os.path.join("project", "database", "indoor_plants.json")
            insert_json_into_table(connection, json_file_path, "staging")

            sql_file_path = os.path.join("project", "database", "create tables", "create_plant_data_table.sql")
            execute_sql_file(connection, sql_file_path)
        finally:
            connection.close()
            print("Connection closed.")
    except Exception as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    main()
