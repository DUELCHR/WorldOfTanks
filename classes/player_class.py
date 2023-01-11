from dictor import dictor
import requests
from classes.tank_class import Tank


class Player:
    def __init__(self, name, application_id):
        self.name = name
        self.player_info = []
        self.player_tanks = []
        self.application_id = application_id
        self.account_id = self.getPlayerAccountId(name)

    def getPlayerAccountId(self, name):
        api_url = "https://api.worldoftanks.eu/wot/account/list/?application_id=" + self.application_id + "&search=" + name
        response = requests.get(api_url)
        data = response.json()
        accountData = dictor(data, "data")
        accountId = dictor(accountData[0], "account_id")
        return accountId

    def getPlayerInfo(self):
        if len(self.player_info) == 0:
            api_url = "https://api.worldoftanks.eu/wot/account/info/?application_id=" + self.application_id + "&account_id=" + str(self.account_id)
            response = requests.get(api_url)
            player_data = response.json()
            self.player_info.append({"name": self.name,
                                     "account_id": self.account_id,
                                     "clan_id": dictor(player_data, "data." + str(self.account_id) + ".clan_id"),
                                     "created_at": dictor(player_data, "data." + str(self.account_id) + ".created_at"),
                                     "trees_cut": dictor(player_data, "data." + str(self.account_id) + ".statistics.trees_cut")})
        return self.player_info

    def getPlayerTanks(self):
        if len(self.player_info) == 0:
            api_url = "https://api.worldoftanks.eu/wot/account/tanks/?application_id=" + self.application_id + "&account_id=" + str(self.account_id)
            response = requests.get(api_url)
            data = response.json()   
            tanks = dictor(data, "data." + str(self.account_id))
            for tank in tanks:
                self.player_tanks.append({"tank_id": dictor(tank, "tank_id"),
                                          "wins": dictor(tank, "statistics.wins"),
                                          "battles": dictor(tank, "statistics.battles")})

        return self.player_tanks
