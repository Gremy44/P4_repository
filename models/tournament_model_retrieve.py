from ast import Return
import os
from tinydb import TinyDB, Query, where

class ModelRetrieveTournament:
    def __init__(self):
        self.id_round = 0

    def retrieve_tournament(self):
        current_tournament = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        current_tournament.default_table_name = "Save_Input_Tournament"
        tournament = current_tournament.all()
        return tournament

    def retrieve_players_input_information(self): 
        '''
        - Retourne liste joueur ordre input tournoi
        '''
        self.ct = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        self.ct.default_table_name = "Save_Input_Tournament"
        self.current_tournament = self.ct.all()

        #self.name   = self.current_tournament[0]['Name']
        #self.place  = self.current_tournament[0]['Place']
        #self.date   = self.current_tournament[0]['Date']
        #self.round  = self.current_tournament[0]['Round']
        #self.tourne = self.current_tournament[0]['Tourne']
        player_ids  = self.current_tournament[0]['Players']
        #self.time   = self.current_tournament[0]['Time']
        #self.desc   = self.current_tournament[0]['Description']

        # --- retrieve players deserializer ---

        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.db.default_table_name = "Players"
        self.players= []
        for i in player_ids:
            deSerialized_players = self.db.search(where('id_player') == i) 
            self.players.append(deSerialized_players)
        
        return self.players

    def test_current_tournament(self):
        '''
        - Retourne True si fichier infos tournoi existe
        ''' 
        path = "./chess_data_base/tounament/actual_tournament/save_tournament_infos.json" 
        if os.path.exists(path):
            return True
        return False

    def test_current_round(self): 
        '''
        - Test si des round ont été commencés, retourne True si oui
        '''
        round_db = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables = round_db.tables() # donne les tables dans le fichier
        tables_nb = len(tables)
        if tables_nb > 1:
            return True
        return False

    def retrieve_round(self): 
        ''' 
        - Retourne une liste avec les joueurs et les scores au dernier round
        - Format => [[{...}{...}][{...}{...}]...]
        '''
        compt_1 = 1
        
        rtt = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables_name = rtt.tables() # donne les tables dans le fichier
        self.id_round = len(tables_name)
        ma_table = rtt.table(f'Round {self.id_round-1}').all() # donne les infos de la dernière table

        pdb = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        pdb.default_table_name = "Players"

        player_ids = []
        self.players = []

        for i in ma_table:
            print("Table actuelle : ", i)
            #deserialise les joueurs
            deSerialized_players_1 = pdb.search(where('id_player') == i[f"Ronde {compt_1}"][0]) 
            deSerialized_players_2 = pdb.search(where('id_player') == i[f"Ronde {compt_1}"][2])
            #créé la liste des joueurs
            player = [*deSerialized_players_1, *deSerialized_players_2]
            #ajoute leur score actuel
            player[0]['Score'] = i[f"Ronde {compt_1}"][1]
            player[1]['Score'] = i[f"Ronde {compt_1}"][3]
            player_ids.append(player)
            compt_1 += 1

        return player_ids 