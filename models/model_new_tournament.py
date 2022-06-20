import os
from tinydb import TinyDB
from controllers.controller_new_tournament import ControllerNewTournament

class ModelNewTournament(ControllerNewTournament):
    def __init__(self, t_name="", t_place="", t_date="", t_round=4, t_tourne="", t_players=..., t_time="", t_desc=""):
        super().__init__(t_name, t_place, t_date, t_round, t_tourne, t_players, t_time, t_desc)

        self.state = True #indique si le tournois est en cour ou terminé

    def id_tournament(self):
        return id(ModelNewTournament)
    
    def input_tournament_db_reg(self):
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/tounament/actual_tournament")
        except FileExistsError:
            pass

        # ----.json creation----
        db = TinyDB("./chess_data_base/tounament/actual_tournament/input_tournament_infos.json") # obj creation and path
        db.default_table_name = "Input_Tournament" # table name
        db.insert({"id_tournament" : self.id_tournament(),
                   "Tournament state" : self.state,
                   "Name" : self.t_name,
                   "Place" : self.t_place, 
                   "Date" : self.t_date, 
                   "Round" : self.t_round,
                   "Tourne" : self.t_tourne, 
                   "Players" : self.t_players,
                   "Time" : self.t_time,
                   "Description" : self.t_desc})