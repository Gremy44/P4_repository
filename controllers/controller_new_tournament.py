from views.views_new_tournament import ViewsNewTournament

class ControllerNewTournament(ViewsNewTournament):
    def __init__(self, t_name ="", t_place="", t_date ="", t_round=4, t_tourne="",t_players=[], t_time="", t_desc=""):
        super().__init__(t_name, t_place, t_date, t_round, t_tourne,t_players, t_time, t_desc)
        self.t_name = t_name
        self.t_place = t_place
        self.t_date = t_date
        self.t_round = t_round 
        self.t_tourne = t_tourne
        self.t_players = t_players 
        self.t_time = t_time
        self.t_desc = t_desc

    # Mettre ici mes méthode pour controller les données 
    # qui vont allé dans la db