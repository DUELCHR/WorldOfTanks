from classes.player_class import Player
import pandas as pd
import streamlit as st


class Application:
    def __init__(self, id):
        self.applicationId = id
        st.sidebar.header("World of Tanks Player Info")


    def run(self):
        playerName = st.sidebar.text_input("Please enter player name")
        if playerName == '':
            st.info(body="please insert a player name!")    
        else:    
            if st.sidebar.button("Show Info"):
                    self.showPlayerInfo(playerName)
            if st.sidebar.button("Show Tanks"):
                    self.showPlayerTanks(playerName)
                    
    def showPlayerInfo(self, playerName):
        st.header("Player Info " + playerName)
        self.player = Player(playerName, self.applicationId)
        player_info = self.player.getPlayerInfo()
        st.write(pd.json_normalize(player_info))

    def showPlayerTanks(self, playerName):
        st.header("Player Info " + playerName)
        self.player = Player(playerName, self.applicationId)
        player_tanks = self.player.getPlayerTanks()
        st.write(pd.json_normalize(player_tanks))