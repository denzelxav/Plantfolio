DROP TABLE IF EXISTS plant_data;

CREATE TABLE plant_data (
    plant_id INT PRIMARY KEY,
    common_name VARCHAR(100),
    cycle VARCHAR(100),
    watering VARCHAR(100),
    other_name VARCHAR(100),
    scientific_name VARCHAR(100)
);

INSERT INTO plant_data (plant_id, common_name, cycle, watering, other_name, scientific_name)
SELECT
    JSON_EXTRACT(json_data, '$.id') AS plant_id,
    JSON_EXTRACT(json_data, '$.common_name') AS common_name,
    JSON_EXTRACT(json_data, '$.cycle') AS cycle,
    JSON_EXTRACT(json_data, '$.watering') AS watering,
    JSON_EXTRACT(json_data, '$.other_name') AS other_name,
    JSON_EXTRACT(json_data, '$.scientific_name') AS scientific_name
FROM staging;


SELECT *
FROM plant_data
WHERE scientific_name LIKE '%,%';