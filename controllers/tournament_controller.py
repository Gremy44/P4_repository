from models import tournament_model_write
from views.views_tournament import ViewsTournament
from models.tournament_model_write import ModelWriteTournament, ModelWritePlayer
from models.tournament_model_retrieve import ModelRetrieveTournament

class TournamentController:
    ''' Déroulé d'un nouveau tournoi : 
    - demande les infos tournois
    - stock les infos tournois dans la db 'save_tournement_infos.json'
    - créé un round 0 avec juste les joueurs qui participent au tournois
      (enregistré dans la db 'save_tournement_infos.json')
    --- pret pour commencer le premier round ---
    Déroulé d'un tour
    - cherche dans la db 'save_tournement_infos.json' le round
    - si aucun round => fais le pairing du premier round 
        - on entre les résulats du tour 
        - les résultats sont écris dans la db 'save_tournement_infos.json'
        - passe au round suivant si pas la fin 
    - sinon récupère les infos du round en cour => fait le pairing  
        - on entre les résulats du tour 
        - les résultats sont écris dans la db 'save_tournement_infos.json'
        - passe au round suivant si pas la fin 
    - si c'est la fin
        - donne les scores
        - rentre les résulats dans une nouvelle db 'tournament.json'
        - supprime le fichier 'save_tournement_infos.json'
    '''
    def __init__(self, t_name = "", t_place = "", t_date = "", t_round = 4, t_ronde = 0, 
                 t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720, 
                              2123311234976, 1988607754144, 1384106246048, 2187293245344], 
                 t_time = "", t_desc= ""):

        self.t_name    = t_name
        self.t_place   = t_place
        self.t_date    = t_date
        self.t_round   = t_round
        self.t_ronde   = t_ronde
        self.t_players = t_players
        self.t_time    = t_time
        self.t_desc    = t_desc

        self.round_1 = []
        self.tournament_infos = []
        self.my_paires = []
       
    def infos_tournament_by_views(self):
        tournament_infos = ViewsTournament().ask_tounament_infos()
        self.t_name    = tournament_infos[0]
        self.t_place   = tournament_infos[1]
        self.t_date    = tournament_infos[2]
        self.t_round   = tournament_infos[3]
        self.t_tourne  = tournament_infos[4]
        self.t_players = tournament_infos[5]
        self.t_time    = tournament_infos[6]
        self.t_desc    = tournament_infos[7]

        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_tourne, self.t_players, self.t_time, self.t_desc

    def pairing_first_round(self, list_players):
        '''
        - Fait les pairs pour le premier round
        '''
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
        '''
        - Fait les pairs pour les rounds autre que le premier
        '''
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

        return self.my_paires


tournoi_controller = TournamentController()
tournoi_views = ViewsTournament()
tournoi_retrieve = ModelRetrieveTournament()
tournoi_players_retrieve = ModelRetrieveTournament()
tournoi_write_player = ModelWritePlayer()

# hydrate tournoi retrieve avec les infos tournoi 
# si pas de tournoi créé, demande les infos et en créé un 
# si tournoi, récupère les infos dans la db

if tournoi_retrieve.test_current_tournament() == True:
    tournoi_retrieve.retrieve_tournament()
else:
    tournoi_controller.infos_tournament_by_views()
    tournoi_write_tournament = ModelWriteTournament(tournoi_controller.t_name,
                                                    tournoi_controller.t_place,
                                                    tournoi_controller.t_date,
                                                    tournoi_controller.t_round,
                                                    tournoi_controller.t_ronde,
                                                    tournoi_controller.t_players,
                                                    tournoi_controller.t_time,
                                                    tournoi_controller.t_desc)
    tournoi_write_tournament.save_input_tournament_db_reg()

while tournoi_players_retrieve.id_round < tournoi_controller.t_round:
    if tournoi_players_retrieve.test_current_round() == True :
        print("round existant")
        players = tournoi_players_retrieve.retrieve_round()
        players_pairing = tournoi_controller.pairing_other_round(players)
        players_round = tournoi_views.views_round_input(players_pairing, tournoi_players_retrieve.id_round)
        tournoi_write_player.save_round_advance(players_round, tournoi_players_retrieve.id_round)
    else:
        print("pas de round existant")
        players = tournoi_players_retrieve.retrieve_players_input_information()
        players_pairing = tournoi_controller.pairing_first_round(players)
        players_round = tournoi_views.views_round_input(players_pairing, tournoi_players_retrieve.id_round+1)
        tournoi_write_player.save_round_advance(players_round, tournoi_players_retrieve.id_round+1)




 








"""tournoi = TournamentController()
mon_tournoi = tournoi.infos_tournament()
# hydrate l'objet avec les valeurs du controller
db_tournoi = ModelWriteTournament(mon_tournoi[0], mon_tournoi[1], mon_tournoi[2], mon_tournoi[3],
                                  mon_tournoi[4], mon_tournoi[5], mon_tournoi[6], mon_tournoi[7])
#db_tournoi.input_tournament_db_reg() # enregistre dans la db
#db_tournoi.save_input_tournament_db_reg() # fait une sauvegarde sur une autre db


recuperation_info = ModelRetrieveTournament()
recuperation_info.test_current_tournament()
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

if recuperation_info.id_round == tournoi.t_round: #fin de partie
    pass
"""








