from views.views_add_player import AddPlayerViews

class AddPlayerController(AddPlayerViews):
    def __init__(self, l_name = "", f_name = "", b_day = "", gender = "", rank = 0.0):
        super().__init__(l_name, f_name, b_day, gender, rank)
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank

    def add_player_data_control(self):
        # mettre toutes mes conditions pour tester la bonne forme
        # des infos envoyées au model
        self.rank = float(self.rank)
    