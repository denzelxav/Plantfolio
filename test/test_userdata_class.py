from project.classes.plant import *
from project.classes.userdata import UserData
from project.classes.spot_notification import Spot, Notification
from project.classes.enums import *

def create_plant(sunlight: Sunlight = Sunlight.FULL_SHADE):
    return Plant(425, 1, "flowerus_mapelus", "flowering-maple",
                 "default", datetime.timedelta(days=7),
                 ["full sun", "part shade"]
                 )

def test_create_userdata_basic():
    maple  = create_plant()
    mydata = UserData()

    mydata.add_room('bedroom')
    mydata.add_room('living room')

    # tests add_room
    assert mydata.rooms == {'bedroom': [], 'living room': []}
    
    spot1 = Spot('spot1', Sunlight.FULL_SHADE, 'high humidity', None, 21)    

    mydata.add_spot(spot1, 'bedroom')

    # tests add_spot
    assert mydata.rooms == {'bedroom': [spot1], 'living room': []}

    mydata.add_plant(maple, spot1)

    # tests add_plant
    assert mydata.rooms['bedroom'][0].assigned_plant == maple
    assert mydata.plants == {maple}

    mydata.water_all()

    # tests water_all
    assert all(plant.watered[-1] < datetime.datetime.now() + datetime.timedelta(seconds = 1) for plant in mydata.plants)

    mydata.delete_plant(maple)

    # tests delete_plant
    assert len(mydata.plants) == 0

    mydata.delete_spot(spot1)

    # tests delete_spot
    assert mydata.rooms == {'bedroom': [], 'living room': []}

    mydata.delete_room('bedroom')

    assert mydata.rooms == {'living room': []}
