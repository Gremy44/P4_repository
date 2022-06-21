import os
from tinydb import TinyDB
from controllers.controller_new_tournament import ControllerNewTournament

class ModelNewTournament():
    def __init__(self):
        self.state = True #indique si le tournois est en cour ou terminé

    def new_tournament_infos(self):
        infos_new_tournament = ControllerNewTournament().infos_new_tournament()
        self.t_name    = infos_new_tournament[0]
        self.t_place   = infos_new_tournament[1]
        self.t_date    = infos_new_tournament[2]
        self.t_round   = infos_new_tournament[3]
        self.t_tourne  = infos_new_tournament[4]
        self.t_players = infos_new_tournament[5]
        self.t_time    = infos_new_tournament[6]
        self.t_desc    = infos_new_tournament[7]

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

    def save_input_tournament_db_reg(self):
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = "Save_Input_Tournament" # table name
        db_save.insert({"id_tournament" : self.id_tournament(),
                   "Tournament state" : self.state,
                   "Name" : self.t_name,
                   "Place" : self.t_place, 
                   "Date" : self.t_date, 
                   "Round" : self.t_round,
                   "Tourne" : self.t_tourne, 
                   "Players" : self.t_players,
                   "Time" : self.t_time,
                   "Description" : self.t_desc})