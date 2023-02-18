from dictor import dictor
from api_helper_class import ApiHelper
from classes.tank_class import Tank


class Player:
    def __init__(self, name, application_id):
        self.name = name
        self.player_info = []
        self.player_tanks = []
        self.application_id = application_id
        self.apiHelper = ApiHelper()
        self.account_id = self.getPlayerAccountId(name)

    def getPlayerAccountId(self, name):
        api_url = "https://api.worldoftanks.eu/wot/account/list/?application_id=" + self.application_id + "&search=" + name
        data = self.apiHelper.getJsonFromUrl(api_url=api_url)
        accountData = dictor(data, "data")
        accountId = dictor(accountData[0], "account_id")
        return accountId

    def getPlayerInfo(self):
        if len(self.player_info) == 0:
            api_url = "https://api.worldoftanks.eu/wot/account/info/?application_id=" + self.application_id + "&account_id=" + str(self.account_id)
            player_data = self.apiHelper.getJsonFromUrl(api_url=api_url)
            self.player_info.append({"name": self.name,
                                     "account_id": self.account_id,
                                     "clan_id": dictor(player_data, "data." + str(self.account_id) + ".clan_id"),
                                     "created_at": dictor(player_data, "data." + str(self.account_id) + ".created_at"),
                                     "trees_cut": dictor(player_data, "data." + str(self.account_id) + ".statistics.trees_cut")})
        return self.player_info

    def getPlayerTanks(self):
        if len(self.player_info) == 0:
            api_url = "https://api.worldoftanks.eu/wot/account/tanks/?application_id=" + self.application_id + "&account_id=" + str(self.account_id)
            data = self.apiHelper.getJsonFromUrl(api_url=api_url)
            
            tanks = dictor(data, "data." + str(self.account_id))                       
            tank_ids = []
            for tank in tanks:                
                tank_ids.append ({"tank_id": dictor(tank, "tank_id")})                
                self.player_tanks.append({"tank_id": dictor(tank, "tank_id"),
                                          "wins": dictor(tank, "statistics.wins"),
                                          "battles": dictor(tank, "statistics.battles")})
            tank_objetcs = Tank.tankFactory(tank_ids=tank_ids, application_id=self.application_id)
            for tank_object in tank_objetcs:
                pass
                

        return self.player_tanks
