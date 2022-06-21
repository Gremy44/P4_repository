from views.views_new_tournament import ViewsNewTournament

class ControllerNewTournament():
    def __init__(self):
        pass

    def infos_new_tournament(self):
        new_tournament = ViewsNewTournament().ask_tounament_infos()
        return new_tournament

    # Mettre ici mes méthode pour controller les données 
    # qui vont allé dans la db