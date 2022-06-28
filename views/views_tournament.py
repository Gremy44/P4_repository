from models.tournament_model_retrieve import ModelRetrieveTournament

class ViewsTournament:
    def __init__(self):
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
        '''
        - input pour les resulats de chaque round
        '''
        print("round : ", round)
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

        return sorted_paires 

    def results(self):
        pass