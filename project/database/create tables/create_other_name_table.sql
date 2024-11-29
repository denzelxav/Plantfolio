DROP TABLE IF EXISTS other_name_table;

CREATE TABLE other_name_table (
    other_name_id INT PRIMARY KEY AUTO_INCREMENT,
    plant_id INT,
    other_name VARCHAR(255),
    FOREIGN KEY (plant_id) REFERENCES plant_data(plant_id)
);


--@block
INSERT INTO other_name_table (plant_id, other_name)
SELECT
    CAST(JSON_EXTRACT(json_data, '$.id') AS UNSIGNED) AS plant_id,
    JSON_UNQUOTE(JSON_EXTRACT(json_data, '$.other_name'))
FROM staging;


--@block
SELECT * FROM other_name_table;
    