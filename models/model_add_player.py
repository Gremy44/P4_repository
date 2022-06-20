import os
from tinydb import TinyDB

from controllers.controller_add_player import AddPlayerController

class AddPlayerModel:
    def __init__(self):
        pass
    
    def player_infos(self):
        player_info = AddPlayerController().add_player_data_control()
        self.l_name = player_info[0]
        self.l_name = player_info[1]
        self.b_day  = player_info[2]
        self.gender = player_info[3]
        self.rank   = player_info[4]
        print("Infos niveau modèle : ", player_info)

    def player_id(self):
        return id(AddPlayerModel)

    def player_db_reg(self): # enregistre les infos joueurs dans la base donnée
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/players_data_base")
        except FileExistsError:
            pass
        # ----.json creation----
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json") # obj creation and path
        self.db.default_table_name = "Players" # table name

        self.db.insert({"id_player": self.player_id(),
                        "Nom" : self.l_name, 
                        "Prenom" : self.l_name, 
                        "Date de naissance" : self.b_day,
                        "Genre" : self.gender, 
                        "Rang" : self.rank})  
    