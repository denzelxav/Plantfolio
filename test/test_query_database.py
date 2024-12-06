import os
from database.query_function import query_from_database
from database.create_plant_database import create_database

def test_query_plant_details():
    """
    Tests the query for plant_details
    length of result is tested
    column names are tested
    first row of the database is tested
    """
    assert os.path.exists('project/plant_database.db')
    test_query = "SELECT * FROM plant_details"
    result = query_from_database(test_query)
    assert len(result) == 154    
    assert (result[0] == (425,
                          "Abutilon hybridum",
                          "flowering-maple",
                          "Malvaceae",
                          "Broadleaf evergreen",
                          "Perennial",
                          "Frequent",
                          "Low",
                          None ,
                          0))
    
def test_other_names():
    """
    Tests the query for plants with no other names
    543 does have other names
    540 does not have other names
    """
    test_query = """
    SELECT pd.plant_id
        FROM plant_details pd
        LEFT JOIN plant_other_names pon
        ON pd.plant_id = pon.plant_id
        WHERE pon.other_name IS NULL
    """

    result = query_from_database(test_query)
    assert (543 not in result)
    assert ((540, ) in result)
    

def test_origin():
    """
    Tests the query for plants with origin Brazil
    426 has origin Brazil
    425 does not have origin Brazil
    """
    test_query = """
    SELECT pd.plant_id, po.origin
        FROM plant_details pd
        LEFT JOIN plant_origins po
        ON pd.plant_id = po.plant_id
        WHERE po.origin = 'Brazil'
        """
    result = query_from_database(test_query)
    assert ((426, "Brazil") in result)
    assert ((425, "Brazil") not in result)


def test_multiple_pruning_months():
    test_query = """
    SELECT pd.plant_id
        FROM plant_details pd
        INNER JOIN plant_pruning_months ppm
        ON pd.plant_id = ppm.plant_id
        WHERE ppm.pruning_month = 'July'
        """
    result = query_from_database(test_query, output_to_file=True)
    with open(os.path.join('database', 'database_output.txt'), 'r', encoding='utf-8') as file:
        content = file.read()
    assert (os.path.exists('database/database_output.txt'))
    assert ('plant_id' in content)
    assert ('428' in content)
    

def test_all_names():
    test_query = """
    SELECT * FROM all_names
    """
    result = query_from_database(test_query)
    assert len(result) == 329
    assert (('maidenhair fern', 543) in result)
    assert (('Adiantum capillus-veneris', 543) in result)
    assert (('Southern Maidenhair', 543) in result)
    assert (("Venus' Hair Fern", 543) in result)
    

def test_origin_and_pruning_month():
    test_query = """
    SELECT pd.plant_id, po.origin, ppm.pruning_month
    FROM plant_details pd
    INNER JOIN plant_origins po ON pd.plant_id = po.plant_id
    INNER JOIN plant_pruning_months ppm ON pd.plant_id = ppm.plant_id
    WHERE po.origin = 'Brazil'
    AND ppm.pruning_month = 'July'
    """
    result = query_from_database(test_query)
    assert ((428, "Brazil", "July") in result)
    assert ((502, "Brazil", "July") not in result)