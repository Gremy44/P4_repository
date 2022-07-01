from models.tournament_model_write import ModelRetrieveTournament


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

class ViewsTournament:
    def __init__(self):
        self.complete_result = []
        self.id_round_views = ModelRetrieveTournament().id_round

    def ask_tounament_infos(self):
        self.t_name    = input("Entrez nom : ")
        self.t_place   = input("Entrez lieu : ")
        self.t_date    = input("Entrez date : ")
        self.t_round   = 4
        self.t_rondes  = input("Entrez instances rondes : ")
        self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720,
                          2123311234976, 1988607754144, 1384106246048, 2187293245344]
        self.t_time    = input("Bullet/Blitz/coup rapide : ")
        self.t_desc    = input("Entrez description : ")

        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_rondes, self.t_players, self.t_time, self.t_desc

    def views_round_input(self, sorted_paires, ronde):
        '''
        - input pour les resulats de chaque round
        '''
        print("round : ", ronde)
        for i in range(len(sorted_paires)):
            print("Ronde", ronde,":",
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
        tournoi = ModelRetrieveTournament().retrieve_tournament()
        inc_score = 1
        print("--- Tournoi terminé ---")
        print("Informations sur le tournoi :")
        print()
        print("Résultats du tournois :")
        score_final = ModelRetrieveTournament().sorted_players()
        for i in score_final : 
            print(f"{inc_score} -  {i['Nom']} {i['Prenom']} au rang {i['Rang']} avec un score de {i['Score']}")
            inc_score += 1
        tournoi = ModelRetrieveTournament().retrieve_tournament()

