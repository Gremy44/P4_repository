from views.views_add_player import AddPlayerViews
from models.model_add_player import AddPlayerModel

class AddPlayerController:
    def __init__(self) -> None:
        pass
    
    def add_player(self): # add new player to db
        add_player_view = AddPlayerViews()
        infos_player = add_player_view.ask_player_infos()
        AddPlayerModel().player_db_reg(infos_player[0], infos_player[1],
                                       infos_player[2], infos_player[3],
                                       infos_player[4])

player = AddPlayerController()
add_player = player.add_player()
        

    