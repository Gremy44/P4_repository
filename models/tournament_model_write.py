import os
from tinydb import TinyDB

class ModelWriteTournament:
    def __init__(self, t_name = "", t_place = "", t_date = "", t_round = 4, t_ronde = 0, t_players = [], t_time = "", t_desc = ""):
        
        self.t_name    = t_name
        self.t_place   = t_place
        self.t_date    = t_date
        self.t_round   = t_round
        self.t_ronde   = t_ronde
        self.t_players = t_players
        self.t_time    = t_time
        self.t_desc    = t_desc

    def id_tournament(self):
        return id(ModelWriteTournament)

    def save_input_tournament_db_reg(self):
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/tounament/actual_tournament")
        except FileExistsError:
            pass

        # ----.json creation----
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = "Save_Input_Tournament" # table name
        db_save.insert({"id_tournament" : self.id_tournament(),
                        "Name"          : self.t_name,
                        "Place"         : self.t_place, 
                        "Date"          : self.t_date, 
                        "Round"         : self.t_round,
                        "Tourne"        : self.t_ronde, 
                        "Players"       : self.t_players,
                        "Time"          : self.t_time,
                        "Description"   : self.t_desc})

class ModelWritePlayer:
    def __init__(self) -> None:
        pass

    def save_round_advance(self, players_infos, round):
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = f"Round {str(round)}"  # table name
        print("round :", round)
        for i in range(len(players_infos)):
            #print("players infos", players_infos)
            joueur_1_id    = players_infos[i][0]['id_player']
            joueur_1_name  = players_infos[i][0]['Prenom']
            joueur_1_score = players_infos[i][0]['Score']
            joueur_2_id    = players_infos[i][1]['id_player']
            joueur_2_name  = players_infos[i][1]['Prenom']
            joueur_2_score = players_infos[i][1]['Score']
            joueurs = [joueur_1_id, joueur_1_score, joueur_2_id, joueur_2_score]
            print(f"Sauvegarde ronde {i+1} : ", joueurs)
            db_save.insert({f"Ronde {i+1}" : joueurs})

        