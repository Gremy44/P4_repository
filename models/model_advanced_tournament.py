import os
from tinydb import TinyDB, where
#from controllers.controller_adavance_tournament import AdvanceTournamentController

class ModelAdvancedTournament:
    def __init__(self) :
        self.current_tournament = []
        self.my_paires = []

    def retrieve_tournament(self):
        self.ct = TinyDB("./chess_data_base/tounament/actual_tournament/input_tournament_infos.json")
        self.ct.default_table_name = "Input_Tournament"
        self.current_tournament = self.ct.search(where("Tournament state") == True)#recherche tournois en cours dans db
        #print(self.current_tournament)

        self.name   = self.current_tournament[0]['Name']
        self.place  = self.current_tournament[0]['Place']
        self.date   = self.current_tournament[0]['Date']
        self.round  = self.current_tournament[0]['Round']
        self.tourne = self.current_tournament[0]['Tourne']
        self.time   = self.current_tournament[0]['Time']
        self.desc   = self.current_tournament[0]['Description']

        #firs retrieve id of playeers
        player_ids  = self.current_tournament[0]['Players']
        # --- retrieve players deserializer ---
        # Acces db
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.db.default_table_name = "Players"
        self.players= []
        for i in player_ids:
            deSerialized_players = self.db.search(where('id_player') == i) 
        self.players.append(deSerialized_players)

    def save_advance(self, tour, resultats):
        infos_pour_stockage = AdvanceTournamentController().infos_round()
        print(infos_pour_stockage)
        """db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = "Tour"+ str(tour+1) # table name
        for i in resultats:
            print(i)"""
        #db_save.insert({"resusltats" : resultats})
        
    def pairing_first_round(self):
        #sorting suivant le rang
        self.players.sort(key="Rank")
        length_to_split=len(self.players)/2
        for i in range(length_to_split):
            paires_1 = [self.players[i], self.players[i+length_to_split]]
            self.my_paires.append(paires_1)

        #print(self.my_paires)
        return self.my_paires # retourne les paire triées

    def pairing_other_round():
        pass

    