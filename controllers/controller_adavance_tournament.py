from views.views_advanced_tournament import AdvancedTournamentViews

class AdvanceTournamentController():
    def __init__(self) -> None:
        pass

    def infos_round(self):
        return AdvancedTournamentViews().sorted_paires

    def joueur_extra_infos(self):
        inc_1 = 0
        inc_2 = 0
        for i in AdvancedTournamentViews().views_round_input(ta.my_paires): #ajoute les points aux infos joueurs
            for n in i:
                n["Points"] = AdvancedTournamentViews().complete_result[inc_1][inc_2][1]
                inc_2 += 1
                inc_2 = inc_2%2
            inc_1 += 1   
        print(AdvancedTournamentViews().sorted_paires)
        return AdvancedTournamentViews().sorted_paires

