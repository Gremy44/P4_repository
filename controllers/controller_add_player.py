from views.views_add_player import AddPlayerViews

class AddPlayerController():
    
    def add_player_data_control(self):
        player_infos = AddPlayerViews().ask_player_infos()
        return player_infos
    