from models.tournament_model_retrieve import ModelRetrieveTournament

class ViewsTournament:
    def __init__(self, t_name ="", t_place="", t_date ="", t_round=4, t_tourne="",t_players=[], t_time="", t_desc=""):
        self.t_name    = t_name
        self.t_place   = t_place
        self.t_date    = t_date
        self.t_round   = t_round 
        self.t_tourne  = t_tourne
        self.t_players = t_players 
        self.t_time    = t_time
        self.t_desc    = t_desc

        self.complete_result = []

        self.id_round_views = ModelRetrieveTournament().id_round

    def ask_tounament_infos(self):
        self.t_name    = input("Entrez nom : ")
        self.t_place   = input("Entrez lieu : ")
        self.t_date    = input("Entrez date : ")
        self.t_round   = 4
        self.t_tourne  = input("Entrez instances rondes : ")
        self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720,
                          2123311234976, 1988607754144, 1384106246048, 2187293245344]
        self.t_time    = input("Bullet/Blitz/coup rapide : ")
        self.t_desc    = input("Entrez description : ")
        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_tourne, self.t_players, self.t_time, self.t_desc

    def views_round_input(self, sorted_paires, round):
        for i in range(len(sorted_paires)):
            print("Round", round,":",
                  sorted_paires[i][0]['Nom'],
                  sorted_paires[i][0]['Prenom'], "contre",
                  sorted_paires[i][1]['Nom'],
                  sorted_paires[i][1]['Prenom'])
            score_p1 = input(f"Score joueur {sorted_paires[i][0]['Nom']} {sorted_paires[i][0]['Prenom']}: ")
            score_p2 = input(f"Score joueur {sorted_paires[i][1]['Nom']} {sorted_paires[i][1]['Prenom']}: ")
            sorted_paires[i][0]['Score'] = sorted_paires[i][0]['Score'] + float(score_p1)
            sorted_paires[i][1]['Score'] = sorted_paires[i][1]['Score'] + float(score_p2)
            '''tour1 = [sorted_paires[i][0]['id_player'],score_p1],[sorted_paires[i][1]['id_player'],score_p2]
            simple_result = (tour1)
            self.complete_result.append(simple_result)'''
        return sorted_paires 

    def results(self, paires):
        pass