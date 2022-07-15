from models.models import PlayerModel, TournamentModel, ReportModel
from views.views_console import AddPlayerViews, TournamentModel, MenuViews, TournamentViews
from views.views_gui import AddPlayers, MainWindow
from controllers.constants import *

class AddPlayerController:
    def __init__(self) -> None:
        pass
    
    def add_player(self): # add new player to db
        add_player_view = AddPlayerViews()
        infos_player = add_player_view.ask_player_infos()
        PlayerModel().player_db_reg(infos_player[0], infos_player[1],
                                       infos_player[2], infos_player[3],
                                       infos_player[4])

    def add_player_GUI(self):
        add_player_view = AddPlayers.send_add_player_infos()
        PlayerModel().player_db_reg(add_player_view[0], add_player_view[1],
                                       add_player_view[2], add_player_view[3],
                                       add_player_view[4])

class TournamentController:
    ''' Déroulé d'un nouveau tournoi : 
    - demande les infos tournois
    - stock les infos tournois dans la db 'save_tournement_infos.json'
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
                 t_players = [], 
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
        tournament_infos = TournamentViews().ask_tounament_infos()
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
    
    def my_tournament_console(self):
        if self.tournoi_model.test_current_tournament() == True:
            self.tournoi_model.retrieve_tournament()
        else:
            self.infos_tournament_by_views()
            self.tournoi_write_tournament = TournamentModel(self.t_name,
                                                            self.t_place,
                                                            self.t_date,
                                                            self.t_round,
                                                            self.t_ronde,
                                                            self.t_players,
                                                            self.t_time,
                                                            self.t_desc)
            self.tournoi_write_tournament.save_input_tournament_db_reg()

        while self.tournoi_model.current_round() < self.t_round:
            print(self.tournoi_model.current_round())
            if self.tournoi_model.test_current_round() == True :
                print("round existant")
                players = self.tournoi_model.retrieve_round()
                players_pairing = self.pairing_other_round(players)
                players_round = self.tournoi_views.views_round_input(players_pairing, self.tournoi_model.id_round)
                print(players_round, '---', self.tournoi_model.id_round)
                self.tournoi_player.save_round_advance(players_round, self.tournoi_model.id_round)
                print("----------------------------------------------------------")
                input("---------| Appuyer sur 'Entrée' pour continuer |----------")
            else:
                print("pas de round existant")
                players = self.tournoi_model.retrieve_players_input_information()
                players_pairing = self.pairing_first_round(players)
                players_round = self.tournoi_views.views_round_input(players_pairing, self.tournoi_model.id_round+1)
                self.tournoi_player.save_round_advance(players_round, self.tournoi_model.id_round+1)

        self.tournoi_views.results()
        self.tournoi_model.save_finished_tournament()
     
    def start(self):
        self.tournoi_views = TournamentViews()
        self.tournoi_model = TournamentModel()
        self.tournoi_player = PlayerModel()
        self.tournoi_add_player = AddPlayerViews()
        self.clmenu = MenuViews()
        
        use_gui = False

        #choix_gui_console = typer.confirm("Utiliser l'interface graphique ?")

        # hydrate tournoi retrieve avec les infos tournoi 
        # si pas de tournoi créé, demande les infos et en créé un 
        # si tournoi, récupère les infos dans la db

        self.clmenu.appliTitle()
        choix_gui = self.clmenu.cl_gui()


        if choix_gui == YES :
            use_gui = True
            MainWindow.goMainWindow()
        elif choix_gui == QUIT:
            print("Fin du programme.")
            quit()
        elif choix_gui == NO:
            while True:
                choix_j_t = self.clmenu.welcom() # print welcom views
                if choix_j_t == PLAYERS:
                    while choix_j_t == PLAYERS:
                        choix_j = self.clmenu.player_menu()
                        if choix_j == ADD_PLAYER: # add player
                            infos_player = self.tournoi_add_player.ask_player_infos()
                            if infos_player == None:
                                pass
                            else:
                                self.tournoi_player.player_db_reg(infos_player[0],
                                                                    infos_player[1],
                                                                    infos_player[2],
                                                                    infos_player[3],
                                                                    infos_player[4])                        
                        elif choix_j == SEE_PLAYER: # view player reg
                            self.tournoi_add_player.reg_players()  
                        else: # back
                            break
                elif choix_j_t == TOURNAMENT:
                    while choix_j_t == TOURNAMENT: # boucle du menu tournoi
                        choix_mt = self.clmenu.tournamentMenu()
                        if choix_mt == NEW_TOURNAMENT:
                            if self.tournoi_model.test_current_tournament() == True: # si tounoi existant
                                choix_nm = self.clmenu.existing_tournament()
                                if int(choix_nm) == ERASE_LAST_FOUND_TOURNAMENT:
                                    self.tournoi_model.clear_tournament()
                                    self.my_tournament_console()
                                else:
                                    pass 
                            else:  
                                self.my_tournament_console()   
                        elif choix_mt == RETRIEVE_TOURNAMENT:
                            if self.tournoi_model.test_current_tournament() == True:
                                self.my_tournament_console()
                            else:
                                self.clmenu.no_tournament()
                        else:
                            break
                else:
                    print("Fin du programme.")
                    quit()
        else:
            print("mauvais paramètre")
            quit()




    