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

        t_n  = self.current_tournament[0]['Name']
        t_p  = self.current_tournament[0]['Place']
        t_d  = self.current_tournament[0]['Date']
        t_r  = self.current_tournament[0]['Round']
        t_to = self.current_tournament[0]['Tourne']
        t_j  = self.current_tournament[0]['Players']
        t_t  = self.current_tournament[0]['Time']

        return  t_n, t_p, t_d, t_r, t_to, t_j, t_t

    def save_advance(self, tour, resultats):
        infos_pour_stockage = AdvanceTournamentController().infos_round()
        print(infos_pour_stockage)
        """db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = "Tour"+ str(tour+1) # table name
        for i in resultats:
            print(i)"""
        #db_save.insert({"resusltats" : resultats})
        
    def pairing_first_round(self):
        # Acces db
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.db.default_table_name = "Players"
       
        # --- retrieve players ---
        l_serialize_players = []
        for i in self.current_tournament[0]['Players']:
            serialized_players = self.db.search(where('id_player') == i) 
            l_serialize_players.append(serialized_players)

        # --- sort by rank ---
        malist = []
        for i in l_serialize_players: #supprime 1 degré de liste
            malist.extend(i)
        tri_rang = sorted(malist, key=lambda k: k['Rang'])#tri par rang

        # --- do paires ---
        length_to_split = len(tri_rang)/2
        length_to_split = int(length_to_split)
        for i in range(length_to_split):
            paires_1 = tri_rang[i], tri_rang[i+length_to_split]
            self.my_paires.append(paires_1)

        #print(self.my_paires)
        return self.my_paires # retourne les paire triées

    def pairing_other_round():
        pass

    