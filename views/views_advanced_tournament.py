from models.model_advanced_tournament import ModelAdvancedTournament

class AdvancedTournamentViews:
    def __init__(self):
        self.sorted_paires = []
        pass
        
    def views_round_input(self, sorted_paires):
        self.sorted_paires = sorted_paires
        self.complete_result = []
        for i in range(len(sorted_paires)):
            print("Round 1 :",
                sorted_paires[i][0]['Nom'],
                sorted_paires[i][0]['Prenom'], "contre",
                sorted_paires[i][1]['Nom'],
                sorted_paires[i][1]['Prenom'])
            score_p1 = input(f"Score joueur {sorted_paires[i][0]['Nom']} {sorted_paires[i][0]['Prenom']}: ")
            score_p2 = input(f"Score joueur {sorted_paires[i][1]['Nom']} {sorted_paires[i][1]['Prenom']}: ")
            tour1 = [sorted_paires[i][0]['id_player'],score_p1],[sorted_paires[i][1]['id_player'],score_p2]
            simple_result = (tour1)
            self.complete_result.append(simple_result)
            print(simple_result)
        print("Résultats du round : ", self.complete_result)
        return self.complete_result

    def take_second(self, elem):
        return elem[1]

    def take_first(self, elem):
        return elem[0]
