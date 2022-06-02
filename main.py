from models.mod_tournament import Tournament
from views.tournaments import ask_informations_tournois

class Tournois:
    def __init__(self):
        pass

infos_tournois = ask_informations_tournois()

tournoi_1 = Tournament(infos_tournois[0], infos_tournois[1], infos_tournois[2],
                       infos_tournois[3], infos_tournois[4], infos_tournois[5],
                       infos_tournois[6], infos_tournois[7])

tournoi_1.reg_infos_tournament()
