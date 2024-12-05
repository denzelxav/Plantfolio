import sqlite3
import os
import json
from tabulate import tabulate


def create_database():
    """"
    Creates a relational database with multiple tables using SQLite and saves the file
    """
    try:
        db_file = os.path.join('project', 'plant_database.db')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Make sure all tables are deleted so we dont run into issues with creating tables
        cursor.execute("""DROP TABLE IF EXISTS staging""")
        cursor.execute("""DROP TABLE IF EXISTS plant_details""")
        cursor.execute("""DROP TABLE IF EXISTS plant_other_names""")
        cursor.execute("""DROP TABLE IF EXISTS plant_origins""")
        cursor.execute("""DROP TABLE IF EXISTS plant_sunlight""")

        # Create all tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging (
            json_data TEXT
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_details (
            plant_id INTEGER PRIMARY KEY,
            scientific_name TEXT,
            common_name TEXT,
            plant_family TEXT,
            plant_type TEXT,
            cycle TEXT,
            watering TEXT,
            watering_frequency TEXT,
            watering_depth TEXT,
            watering_period TEXT,
            maintenance TEXT,
            toxic_to_pets INTEGER,
            all_other_names TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_other_names (
            other_name_id INTEGER PRIMARY KEY,
            other_name TEXT,
            plant_id INTEGER,
            FOREIGN KEY(plant_id) REFERENCES plant_details(plant_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_origins (
            origin_id INTEGER PRIMARY KEY,
            origin TEXT,
            plant_id INTEGER,
            FOREIGN KEY(plant_id) REFERENCES plant_details(plant_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_sunlight (
            sunlight_id INTEGER PRIMARY KEY,
            sunlight TEXT,
            plant_id INTEGER,
            FOREIGN KEY(plant_id) REFERENCES plant_details(plant_id)
        )
        """)

        # Fill staging table with data from plant_details.json
        json_details_path = os.path.join('database', 'plant_details.json')
        with open(json_details_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            plants = [(json.dumps(plant),) for plant in data]
            cursor.executemany("""
                INSERT INTO staging (json_data)
                VALUES (?)
                """, plants)

        # Fill plant_details table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_details (plant_id, scientific_name, common_name, plant_family, plant_type, cycle, watering, watering_frequency, watering_depth, watering_period, maintenance, toxic_to_pets, all_other_names)
                    SELECT 
                        json_extract(json_data, '$.id') as plant_id,
                        json_extract(json_data, '$.scientific_name[0]') as scientific_name,
                        json_extract(json_data, '$.common_name') as common_name,
                        json_extract(json_data, '$.family') as plant_family,
                        json_extract(json_data, '$.type') as plant_type,
                        json_extract(json_data, '$.cycle') as cycle,
                        json_extract(json_data, '$.watering') as watering,
                        json_extract(json_data, '$.watering_general_benchmark.value') || ' ' || json_extract(json_data, '$.watering_general_benchmark.unit') as watering_frequency,
                        json_extract(json_data, '$.depth_water_requirement.value') || ' ' || json_extract(json_data, '$.depth_water_requirement.unit') as watering_depth,
                        json_extract(json_data, '$.watering_period') as watering_period,
                        json_extract(json_data, '$.maintenance') as maintenance,
                        json_extract(json_data, '$.poisonous_to_pets') as toxic_to_pets,
                        json_extract(json_data, '$.other_name') as all_other_names
                    FROM staging
                    """)
        
        # Fill plant_other_names table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_other_names (other_name, plant_id)
                    SELECT 
                        json_each.value as other_name,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.other_name'))
                    WHERE json_type(json_extract(json_data, '$.other_name')) = 'array'
                    """)
        
        # Fill plant_origins table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_origins (origin, plant_id)
                    SELECT 
                        json_each.value as origin,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.origin'))
                    WHERE json_type(json_extract(json_data, '$.origin')) = 'array'
                    """)
        
        # Fill plant_origins table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_sunlight (sunlight, plant_id)
                    SELECT 
                        json_each.value as sunlight,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.sunlight'))
                    WHERE json_type(json_extract(json_data, '$.sunlight')) = 'array'
                    """)

        conn.commit()
    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        conn.close()

def query_from_database(query: str) -> None:
    """
    Queries the database and returns the result in a txt file, database_output.txt
    """
    try:
        db_file = os.path.join('project', 'plant_database.db')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute(query)

        column_names = [description[0] for description in cursor.description]
        result = cursor.fetchall()

    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        conn.close()

    try:
        output_path = os.path.join('database', 'create_db_tables', 'database_output.txt')
        with open(output_path, 'w', encoding='utf-8') as file:
            table = tabulate(result, headers=column_names, tablefmt='pretty', numalign='center')
            file.write(str(table))
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    create_database()
    # query_from_database("""
    # SELECT pd.*
    # FROM plant_details pd
    # JOIN plant_origins po ON pd.plant_id = po.plant_id
    # WHERE po.origin LIKE '%islands%'
    # """)

    # query_from_database("""SELECT * FROM plant_origins""")

    query_from_database("""
    SELECT pd.*, ps.sunlight
    FROM plant_details pd
    JOIN plant_sunlight ps ON pd.plant_id = ps.plant_id
    WHERE ps.sunlight = 'part sun/part shade'
    """)

    # query_from_database("""SELECT sunlight, plant_id
    #                     FROM plant_sunlight
    #                     GROUP BY sunlight, plant_id
    #                     """)

    # query_from_database("""SELECT * FROM plant_details""")
