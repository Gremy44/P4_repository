class AddPlayerViews:
    def __init__(self, l_name = "", f_name = "", b_day = "", gender = "", rank = 0.0):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank
        self.score = 0.0

    def ask_player_infos(self):
        self.l_name = input("Entrez nom : ")
        self.f_name = input("Entrez prénom : ")
        self.b_day = input("Date d'anniversaire : ")
        self.gender = input("Genre : ")
        self.rank = input("Rang : ")
        return self.l_name, self.f_name, self.b_day, self.gender, self.rank, self.score
