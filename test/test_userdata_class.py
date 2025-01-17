import datetime
from project.classes.plant import Plant
from project.classes.userdata import UserData
from project.classes.spot_notification import Spot
from project.classes.enums import Sunlight

def create_plant1():
    """
    Creates a plant object for testing
    """
    return Plant(425, 1, "Abutilon hybridum", "flowering-maple",
                 "default", datetime.timedelta(days=4),
                 [Sunlight.FULL_SUN, Sunlight.PART_SHADE]
                 )

def create_plant2():
    """
    Creates a plant object for testing
    """
    return Plant(434, 2, "Acalypha wilkesiana", "Jacob's coat",
                 "default", datetime.timedelta(days=4),
                 [Sunlight.FULL_SUN, Sunlight.PART_SHADE]
                 )

def create_plant3():
    """
    Creates a plant object for testing
    """
    return Plant(502, 2, "Achimenes (group)", "hot water plant",
                 "default", datetime.timedelta(weeks=1),
                [Sunlight.PART_SHADE]
                 )


def test_create_userdata_basic():
    """
    Tests the basic functionality of the UserData class
    """
    maple  = create_plant1()
    mydata = UserData()

    mydata.add_room('bedroom')
    mydata.add_room('living room')

    # tests add_room
    assert mydata.rooms == {'bedroom': [], 'living room': []}

    spot1 = Spot('spot1', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')

    mydata.add_spot(spot1)

    # tests add_spot
    assert mydata.rooms == {'bedroom': [spot1], 'living room': []}

    mydata.add_plant(maple, spot1)

    # tests add_plant
    assert mydata.rooms['bedroom'][0].assigned_plant == maple
    assert mydata.plants == [maple]

    mydata.water_all()

    # tests water_all
    assert all(plant.watered[-1] < datetime.datetime.now() + datetime.timedelta(seconds = 1)
               for plant in mydata.plants)

    mydata.delete_plant(maple)

    # tests delete_plant
    assert len(mydata.plants) == 0

    mydata.delete_spot(spot1)

    # tests delete_spot
    assert mydata.rooms == {'bedroom': [], 'living room': []}

    mydata.delete_room('bedroom')

    assert mydata.rooms == {'living room': []}

def test_add_plant_spot_not_in_room():
    """
    Tests the add_plant method of the UserData class when the spot is not in the room
    """
    maple  = create_plant1()
    mydata = UserData()

    spot1 = Spot('spot1', Sunlight.FULL_SHADE, 'high humidity', None, 21, 'bedroom')
    spot2 = Spot('spot2', Sunlight.FULL_SUN, 'low humidity', None, 22, 'living room')

    mydata.add_spot(spot1)

    mydata.add_plant(maple, spot2)

    assert mydata.rooms == {'bedroom': [spot1], 'living room': [spot2]}
    assert mydata.plants == [maple]
    assert spot2.assigned_plant == maple

def test_sort_plants():
    """
    Tests the sort_plants method of the UserData class
    """
    maple  = create_plant1()
    maple.current_tasks.add('water')
    sansevieria = create_plant2()
    sansevieria.current_tasks.update(['water', 'repot'])
    strelitzia = create_plant3()
    mydata = UserData()

    mydata.add_room('bedroom')
    mydata.add_room('living room')
    table = Spot('table', Sunlight.PART_SHADE, 'high humidity', maple, 21, 'bedroom')
    ledge1 = Spot('ledge1', Sunlight.FULL_SUN, 'low humidity', sansevieria, 22, 'living room')
    ledge2 = Spot('ledge2', Sunlight.FULL_SUN, 'low humidity', strelitzia, 22, 'living room')

    mydata.add_spot(table)
    mydata.add_spot(ledge1)
    mydata.add_spot(ledge2)
    mydata.add_plant(maple, table)
    mydata.add_plant(sansevieria, ledge1)
    mydata.add_plant(strelitzia, ledge2)

    sortedonname = mydata.sort_plants('core_name', False)
    assert sortedonname == [maple, strelitzia, sansevieria]

    sortedonscientificname = mydata.sort_plants('scientific_name', False)
    assert sortedonscientificname == [maple, sansevieria, strelitzia]

    sortedonroom = mydata.sort_plants('room', False)
    assert sortedonroom[0] == maple

    sortedoncurrent_tasks = mydata.sort_plants('current_task', False)
    assert sortedoncurrent_tasks == [sansevieria, maple, strelitzia]

    sortedonnothing = mydata.sort_plants('blabla', True)
    assert ValueError


def test_load_spot_data():
    """
    Tests the load_spot_data method of the UserData class
    """
    mydata = UserData()
    spot_data = {'spot_id': 'Window',
                 'light_level': 'FULL_SHADE',
                 'humidity': 'high humidity',
                 'temperature': 21,
                 'room': 'bedroom'}

    mydata.load_spot_data(spot_data)

    assert mydata.rooms == {'bedroom': [Spot('Window',
                                             Sunlight.FULL_SHADE,
                                             'high humidity',
                                             None,
                                             21,
                                             'bedroom')]}

    spot_data = {'spot_id': 'Cabinet',
                 'light_level': 'FULL_SUN',
                 'humidity': 'high humidity',
                 'temperature': 21,
                 'room': 'kitchen'}

    mydata.load_spot_data(spot_data)

    assert mydata.rooms == {'bedroom': [Spot('Window',
                                             Sunlight.FULL_SHADE,
                                             'high humidity',
                                             None,
                                             21,
                                             'bedroom')],
                            'kitchen': [Spot('Cabinet',
                                             Sunlight.FULL_SUN,
                                             'high humidity',
                                             None,
                                             21,
                                             'kitchen')]}

    spot_data = {'spot_id': 'Shelf',
                 'light_level': 'FULL_SHADE',
                 'humidity': 'low humidity',
                 'temperature': 21,
                 'room': 'living room'}

    mydata.load_spot_data(spot_data)

    assert mydata.rooms == {'bedroom': [Spot('Window',
                                             Sunlight.FULL_SHADE,
                                             'high humidity',
                                             None,
                                             21,
                                             'bedroom')],
                            'kitchen': [Spot('Cabinet',
                                             Sunlight.FULL_SUN,
                                             'high humidity',
                                             None,
                                             21,
                                             'kitchen')],
                            'living room': [Spot('Shelf',
                                                 Sunlight.FULL_SHADE,
                                                 'low humidity',
                                                 None,
                                                 21,
                                                 'living room')]}
