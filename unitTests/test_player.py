# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("../")
from classes.player_class import Player

class TestClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestClass, self).__init__(*args, **kwargs)
        self.application_id = "bf17b4a90124e900d3e0efffeedacabd"
        self.player_name = "Laquatas"
        self.account_id = 564790936
    def test_getPlayerAccountId(self):
        # Testdaten vorbereiten
        
        player = Player(self.player_name, self.application_id)

        # Test ausführen
        result = player.getPlayerAccountId(self.player_name)

        # Überprüfen, ob die Anforderungen und der Rückgabewert korrekt sind
        self.assertEqual(result, self.account_id)

    def test_getPlayerInfo(self):
        # Testdaten vorbereiten
        created_at = 1569141188
        player = Player(self.player_name, self.application_id)

        # Test ausführen
        result = player.getPlayerInfo()

        # Überprüfen, ob die Anforderungen und der Rückgabewert korrekt sind
        expected_result = {"name": self.player_name,
                           "account_id": self.account_id,
                           "clan_id": None,
                           "created_at": created_at }
        
        self.assertEqual(result[0].get('name'), expected_result["name"])
        self.assertEqual(result[0].get('account_id'), expected_result["account_id"])
        self.assertEqual(result[0].get('clan_id'), expected_result["clan_id"])
        self.assertEqual(result[0].get('created_at'), expected_result["created_at"])

    def test_getPlayerTanks(self):
        # Testdaten vorbereiten   
        tank_id = 52305
        player = Player(self.player_name, self.application_id)
    
        # Test ausführen
        result = player.getPlayerTanks()
        
        # Überprüfen, ob die Anforderungen und der Rückgabewert korrekt sind
        expected_result = {"name": self.player_name,
                           "account_id": self.account_id,
                           "tank_id": tank_id
                            }
              
        self.assertEqual(result[0].get('tank_id'), expected_result["tank_id"])


if __name__ == '__main__':
    unittest.main()