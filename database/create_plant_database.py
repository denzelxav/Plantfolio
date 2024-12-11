import sqlite3
import os
import json


def create_database():
    """"
    Creates a relational database with multiple tables using SQLite and saves the file
    """
    db_file = os.path.join('project', 'plant_database.db')
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        # Make sure all tables are deleted so we dont run into issues with creating tables
        cursor.execute("""DROP TABLE IF EXISTS staging""")
        cursor.execute("""DROP TABLE IF EXISTS plant_details""")
        cursor.execute("""DROP TABLE IF EXISTS plant_other_names""")
        cursor.execute("""DROP TABLE IF EXISTS plant_origins""")
        cursor.execute("""DROP TABLE IF EXISTS plant_sunlight""")
        cursor.execute("""DROP TABLE IF EXISTS plant_pruning_months""")
        cursor.execute("""DROP TABLE IF EXISTS all_names""")

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
            sunlight_list TEXT,
            cycle TEXT,
            watering TEXT,
            maintenance TEXT,
            pruning_frequency TEXT,
            toxic_to_pets INTEGER
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

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant_pruning_months (
            pruning_month_id INTEGER PRIMARY KEY,
            pruning_month TEXT,
            plant_id INTEGER,
            FOREIGN KEY(plant_id) REFERENCES plant_details(plant_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS all_names (
            name TEXT,
            plant_id INTEGER
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
                    INSERT INTO plant_details (plant_id, scientific_name, common_name, plant_family, plant_type, sunlight_list, cycle, watering, pruning_frequency, maintenance, toxic_to_pets)
                    SELECT 
                        json_extract(json_data, '$.id') as plant_id,
                        json_extract(json_data, '$.scientific_name[0]') as scientific_name,
                        json_extract(json_data, '$.common_name') as common_name,
                        json_extract(json_data, '$.family') as plant_family,
                        json_extract(json_data, '$.type') as plant_type,
                        json_extract(json_data, '$.sunlight') as sunlight_list,
                        json_extract(json_data, '$.cycle') as cycle,
                        json_extract(json_data, '$.watering') as watering,
                        json_extract(json_data, '$.pruning_count.amount') || ' '|| 'time per year' as pruning_frequency,
                        json_extract(json_data, '$.maintenance') as maintenance,
                        json_extract(json_data, '$.poisonous_to_pets') as toxic_to_pets
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

        # Fill plant_sunlight table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_sunlight (sunlight, plant_id)
                    SELECT 
                        json_each.value as sunlight,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.sunlight'))
                    WHERE json_type(json_extract(json_data, '$.sunlight')) = 'array'
                    """)

        # Fill plant_pruning_months table with data from staging table
        cursor.execute("""
                    INSERT INTO plant_pruning_months (pruning_month, plant_id)
                    SELECT 
                        json_each.value as pruning_month,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.pruning_month'))
                    WHERE json_type(json_extract(json_data, '$.pruning_month')) = 'array'
                    """)

        cursor.execute("""
                    INSERT INTO all_names (name, plant_id)
                    SELECT
                        json_each.value as name,
                        json_extract(json_data, '$.id') as plant_id
                    FROM staging,
                       json_each(json_extract(json_data, '$.other_name'))
                    WHERE json_type(json_extract(json_data, '$.other_name')) = 'array'
                       """)

        cursor.execute("""
                    INSERT INTO all_names (name, plant_id)
                       SELECT
                        json_extract(json_data, '$.scientific_name[0]') as name,
                        json_extract(json_data, '$.id') as plant_id
                       FROM staging
                       """)

        cursor.execute("""
                    INSERT INTO all_names (name, plant_id)
                       SELECT
                        json_extract(json_data, '$.common_name') as name,
                        json_extract(json_data, '$.id') as plant_id
                       FROM staging
                       """)

        conn.commit()
