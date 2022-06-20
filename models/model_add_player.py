import os
from tinydb import TinyDB

from controllers.controller_add_player import AddPlayerController

class AddPlayerModel(AddPlayerController):
    def __init__(self, l_name = "", f_name = "", b_day = "", gender = "", rank = 0.0):
        super().__init__(l_name, f_name, b_day, gender, rank)
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank

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
                        "Prenom" : self.f_name, 
                        "Date de naissance" : self.b_day,
                        "Genre" : self.gender, 
                        "Rang" : self.rank})  
    