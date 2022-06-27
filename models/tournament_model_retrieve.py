from tinydb import TinyDB, where

class ModelRetrieveTournament:
    def __init__(self):
        self.id_round = 0

    def retrieve_players(self): #retourne liste joueur ordre input tournoi
        self.ct = TinyDB("./chess_data_base/tounament/actual_tournament/input_tournament_infos.json")
        self.ct.default_table_name = "Input_Tournament"
        self.current_tournament = self.ct.search(where("Tournament state") == True)#recherche tournois en cours dans db

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

    def retrieve_tournament(self): #retourne la liste et le score de du dernier round de la db
        compt_1 = 0
        
        rtt = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables_name = rtt.tables() # donne les tables dans le fichier
        tables_nb = len(tables_name)
        self.id_round = tables_nb-2
        ma_table = rtt.table(f'Round {self.id_round}').all() # donne les infos de la dernière table

        pdb = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        pdb.default_table_name = "Players"

        player_ids = []
        self.players = []
        print("id round model : ", self.id_round)

        for i in ma_table:
            print("Table actuelle : ", i)
            #deserialise les joueurs
            deSerialized_players_1 = pdb.search(where('id_player') == i[f"Ronde {compt_1+1}"][0])
            deSerialized_players_2 = pdb.search(where('id_player') == i[f"Ronde {compt_1+1}"][2])
            #créé la liste des joueurs
            player = [*deSerialized_players_1, *deSerialized_players_2]
            #ajoute leur score actuel
            player[0]['Score'] = i[f"Ronde {compt_1+1}"][1]
            player[1]['Score'] = i[f"Ronde {compt_1+1}"][3]
            player_ids.append(player)
            compt_1 += 1

        return player_ids # format [[{...}{...}][{...}{...}]...]

        

