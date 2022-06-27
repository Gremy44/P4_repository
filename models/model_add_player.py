import os
from tinydb import TinyDB

class AddPlayerModel:
    def __init__(self):
        pass

    def player_id(self):
        return id(AddPlayerModel)

    def player_db_reg(self, l_name, f_name, b_day, gender, rank): # enregistre les infos joueurs dans la base donnée
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/players_data_base")
        except FileExistsError:
            pass
        # ----.json creation----
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json") # obj creation and path
        self.db.default_table_name = "Players" # table name

        self.db.insert({"id_player": self.player_id(),
                        "Nom" : l_name, 
                        "Prenom" : f_name, 
                        "Date de naissance" : b_day,
                        "Genre" : gender, 
                        "Rang" : rank,
                        "Score" : 0.0}) 
    