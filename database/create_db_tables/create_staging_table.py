import sqlite3
import os
import json


db_file = os.path.join('database', 'staging.db')
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS staging
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS staging (
    json_data TEXT
)""")

json_details_path = os.path.join('database', 'plant_details.json')
with open(json_details_path) as file:
    data = json.load(file)
    for plant in data:
        cursor.execute("""
        INSERT INTO staging (json_data)
        VALUES (?)
        """, (json.dumps(plant),))

conn.commit()


result = cursor.execute("""SELECT * FROM staging""")
for row in result.fetchall():
    print(row)
    
conn.close()