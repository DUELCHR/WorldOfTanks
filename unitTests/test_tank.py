import unittest
import sys
sys.path.append("../")
from classes.tank_class import Tank

class TestClass(unittest.TestCase):
    application_id = "bf17b4a90124e900d3e0efffeedacabd"
    player_name = "Laquatas"
    account_id = 564790936
    def __init__(self, *args, **kwargs):
        super(TestClass, self).__init__(*args, **kwargs)        
    def test_tankFactory(self):
        # given        
        tanks_ids = [52305,14609]
        # when
        tank_objects = Tank.tankFactory(tank_ids=tanks_ids, application_id=TestClass.application_id)
        # then  
        self.assertEqual(len(tank_objects), 2)
        self.assertEqual(tank_objects[0].getTankInfo().get("name"), "GSOR 1008")
        self.assertEqual(tank_objects[1].getTankInfo().get("name"), "Leopard 1")
    def test_getTankInfo(self):
        # given
        tank_id = 52305
        tank = Tank(tank_id=tank_id, application_id=TestClass.application_id)
        # when
        tank_info = tank.getTankInfo()
        # then
        self.assertEqual(tank_info.get("name"), "GSOR 1008")