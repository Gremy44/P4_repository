class ViewsNewTournament:
    def __init__(self, t_name ="", t_place="", t_date ="", t_round=4, t_tourne="",t_players=[], t_time="", t_desc=""):
        self.t_name = t_name
        self.t_place = t_place
        self.t_date = t_date
        self.t_round = t_round 
        self.t_tourne = t_tourne
        self.t_players = t_players 
        self.t_time = t_time
        self.t_desc = t_desc

    def ask_tounament_infos(self):
        self.t_name = input("Entrez nom : ")
        self.t_place = input("Entrez lieu : ")
        self.t_date = input("Entrez date : ")
        self.t_round = 4
        self.t_tourne = input("Entrez instances rondes : ")
        self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720, 2123311234976, 1988607754144, 1384106246048, 2187293245344]
        self.t_time = input("Bullet/Blitz/coup rapide : ")
        self.t_desc = input("Entrez description : ")
        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_tourne, self.t_players, self.t_time, self.t_desc