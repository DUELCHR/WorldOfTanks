# -*- coding: utf-8 -*-
import requests
from dictor import dictor
class Tank:
    def __init__(self, tank_id, application_id):
        self.tank_id = tank_id
        self.application_id = application_id
        self.tank_info = {}
    def tankFactory(tank_ids, application_id):
        tanks = []
        tank_id_str = ""
        #Build Tank Objects
        for tank_id in tank_ids:
            new_tank = Tank(tank_id, application_id=application_id)
            if tank_id_str == "":
                tank_id_str = str(tank_id)
            else:    
                tank_id_str = tank_id_str + "," + str(tank_id)
            tanks.append(new_tank)
        
        # Get Tank Information for all tanks
        api_url = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/?application_id=" + application_id + "&tank_id=" + tank_id_str
        response = requests.get(api_url)
        data = response.json()
        
        # update the tank objects with the gatherd informations
        for tank in tanks:            
            tank.tank_info = dictor(data, "data." + str(tank.tank_id))
            
                
        return tanks    
    def getTankInfo(self):
        if self.tank_info == {}:
            api_url = "https://api.worldoftanks.eu/wot/encyclopedia/vehicles/?application_id=" + self.application_id + "&tank_id=" + str(self.tank_id)
            response = requests.get(api_url)
            data = response.json()
            self.tank_info = dictor(data, "data." + str(self.tank_id))
        return self.tank_info