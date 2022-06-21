from tinydb import TinyDB
from controllers.controller_adavance_tournament import AdvanceTournamentController

class SaveAdvanceTournamentModel():
    def __init__(self) -> None:
        pass

    def save_advance(self):
        result_of_round = AdvanceTournamentController().info_round
        print(result_of_round)


        """db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
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
                        "Description" : self.t_desc})"""