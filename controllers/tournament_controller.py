from views.views_tournament import ViewsTournament
from models.tournament_model_write import ModelWriteTournament
from models.tournament_model_retrieve import ModelRetrieveTournament

class TournamentController:
    def __init__(self):
        self.t_name    = ""
        self.t_place   = ""
        self.t_date    = ""
        self.t_round   = ""
        self.t_tourne  = ""
        self.t_players = []
        self.t_time    = ""
        self.t_desc    = ""

        self.round_1 = []
        self.tournament_infos = []
        self.my_paires = []
       

    def infos_tournament(self):
        self.tournament_infos = ViewsTournament().ask_tounament_infos()

        self.t_name    = self.tournament_infos[0]
        self.t_place   = self.tournament_infos[1]
        self.t_date    = self.tournament_infos[2]
        self.t_round   = self.tournament_infos[3]
        self.t_tourne  = self.tournament_infos[4]
        self.t_players = self.tournament_infos[5]
        self.t_time    = self.tournament_infos[6]
        self.t_desc    = self.tournament_infos[7]

        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_tourne, self.t_players, self.t_time, self.t_desc

    def pairing_first_round(self, list_players):
        #sorting suivant le rang
        tri_temp = []
        tri = []
        tri_temp = sorted(list_players, key=lambda x:x[0]['Rang']) #tri par rang
        
        for i in tri_temp: # substract 1 level of array
            for n in i:
                tri.append(n)
        
        length_to_split=int(len(tri)/2) #determine le nombre de tour pour la boucle
        for i in range(length_to_split): # fait les paires
            paires_1 = [tri[i], tri[i+length_to_split]]
            self.my_paires.append(paires_1)

        return self.my_paires

    def pairing_other_round(self, list_players):
        tri_temp = []
        mes_paires_temp = []
        self.my_paires = []

        for i in list_players:
            for n in i:
                tri_temp.append(n)

        pair = sorted(tri_temp, key=lambda x:(x['Score'], x['Rang']))

        mod = 0 
        for i in range(int(len(pair)/2)) :
            mes_paires_temp.append(pair[mod+i])
            mod += 1
            mes_paires_temp.append(pair[mod+i])
            self.my_paires.insert(i,mes_paires_temp)
            mes_paires_temp = []
        
    def round(self):
        self.round_1 = ViewsTournament().views_round_input(self.my_paires, recuperation_info.id_round+1)
        return self.round_1


tournoi = TournamentController()
mon_tournoi = tournoi.infos_tournament()
# hydrate l'objet avec les valeurs du controller
db_tournoi = ModelWriteTournament(mon_tournoi[0], mon_tournoi[1], mon_tournoi[2], mon_tournoi[3],
                                  mon_tournoi[4], mon_tournoi[5], mon_tournoi[6], mon_tournoi[7])
#db_tournoi.input_tournament_db_reg() # enregistre dans la db
#db_tournoi.save_input_tournament_db_reg() # fait une sauvegarde sur une autre db

recuperation_info = ModelRetrieveTournament()
infos_tournoi = recuperation_info.retrieve_tournament()
players = recuperation_info.retrieve_players()


while recuperation_info.id_round < tournoi.t_round:

    if recuperation_info.id_round == 0:
        pairing_1 = tournoi.pairing_first_round(players)
        #db_tournoi.save_tournament_advance(pairing_1, recuperation_info.id_round)
        r_1 = tournoi.round()
        recuperation_info.id_round += 1
    else:
        #db_tournoi.save_tournament_advance(r_1, recuperation_info.id_round)
        pairing_2 = tournoi.pairing_other_round(infos_tournoi)
        r_1 = tournoi.round()
        recuperation_info.id_round += 1

# regarder le déroulé du script et de la boucle pour la faire fonctionner comme elle devrait
"""for recuperation_info.id_round in range(tournoi.t_round):
    if recuperation_info.id_round == 0:
        print(" cest zero")
        pairing_1 = tournoi.pairing_first_round(players)
        #db_tournoi.save_tournament_advance(pairing_1, i)
        r_1 = tournoi.round()
        #print(r_1)
    else:
        print("cest ok")
        #db_tournoi.save_tournament_advance(r_1, i)
        pairing_2 = tournoi.pairing_other_round(r_1)
        r_1 = tournoi.round()"""








