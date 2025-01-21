from project.classes.spot_notification import Spot, Notification

def test_spot_initialization():
    spot = Spot("1", "High", "High", None, 20, "Living Room")
    equals = spot == Spot("1", "High", "High", None, 20, "Living Room")
    not_equals = spot == 1
    assert spot.spot_id == "1"
    assert spot.light_level == "High"
    assert spot.humidity == "High"
    assert spot.assigned_plant == None
    assert spot.temperature == 20
    assert spot.room == "Living Room"
    assert equals == True
    assert not_equals == False
