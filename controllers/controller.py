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
    def __init__(self, 
                 t_name = "", 
                 t_place = "", 
                 t_date_start = "", 
                 t_date_end = "", 
                 t_tours = 4, 
                 t_instances_rondes = 0, 
                 t_players = [], 
                 t_time = "", 
                 t_desc= ""):
       
        self.t_name       = t_name
        self.t_place      = t_place
        self.t_date_start = t_date_start
        self.t_date_end   = t_date_end
        self.t_round      = t_tours
        self.t_ronde      = t_instances_rondes
        self.t_players    = t_players
        self.t_time       = t_time
        self.t_desc       = t_desc

        self.tournoi_views      = TournamentViews()
        self.tournoi_model      = TournamentModel()
        self.tournoi_player     = PlayerModel()
        self.tournoi_add_player = AddPlayerViews()
        self.clmenu             = MenuViews()

        self.round_1 = []
        self.tournament_infos = []
        self.my_paires = []

    def infos_tournament_by_views(self):
        tournament_infos        = TournamentViews().ask_tounament_infos()
        self.t_name             = tournament_infos[0]
        self.t_place            = tournament_infos[1]
        self.t_date_start       = tournament_infos[2]
        self.t_date_end         = tournament_infos[3]
        self.t_tours            = tournament_infos[4]
        self.t_instances_rondes = tournament_infos[5]
        self.t_players          = tournament_infos[6]
        self.t_time             = tournament_infos[7]
        self.t_desc             = tournament_infos[8]

        return self.t_name, self.t_place, self.t_date_start, self.t_date_end, self.t_tours, self.t_instances_rondes, self.t_players, self.t_time, self.t_desc

    def pairing_first_round(self, list_players):
        '''
        - pair for first round
        '''
        #sorting suivant le rang
        
        tri = []
        tri = sorted(list_players, key=lambda x:x['Rang']) #tri par rang
        
        length_to_split=int(len(tri)/2) #determine le nombre de tour pour la boucle

        for i in range(length_to_split): # fait les paires
            paires_1 = [tri[i], tri[i+length_to_split]]
            self.my_paires.append(paires_1)

        return self.my_paires

    def pairing_other_round(self, list_players):
        '''
        - pair for other round
        '''
        mes_paires_temp = []
        self.my_paires = []

        pair = sorted(list_players, key=lambda x:(x['Score'], x['Rang']))

        mod = 0 
        for i in range(int(len(pair)/2)) :
            mes_paires_temp.append(pair[mod+i])
            mod += 1
            mes_paires_temp.append(pair[mod+i])
            self.my_paires.insert(i,mes_paires_temp)
            mes_paires_temp = []

        return self.my_paires
    
    def my_tournament_console(self):
        if self.tournoi_model.test_current_tournament() == False:
            self.infos_tournament_by_views()
            self.tournoi_write_tournament = TournamentModel(self.t_name,
                                                            self.t_place,
                                                            self.t_date_start,
                                                            self.t_date_end,
                                                            self.t_tours,
                                                            self.t_instances_rondes,
                                                            self.t_players,
                                                            self.t_time,
                                                            self.t_desc)
            self.tournoi_write_tournament.save_input_tournament_db_reg()
        else:
            print("current round controller : ", self.tournoi_model.current_round())
            print("test fichier : ", self.tournoi_model.test_current_tournament())
            infos = TournamentModel().retrieve_tournament()
            self.t_name = infos[0]["Name"]
            self.t_place = infos[0]["Place"]
            self.t_date_start = infos[0]["Date_start"]
            self.t_date_end = infos[0]["Date_end"]
            self.t_tours = infos[0]["Match"]
            self.t_instances_rondes = infos[0]["Instance_Rondes"]
            self.t_players = infos[0]["Players"]
            self.t_time = infos[0]["Time"]
            self.t_desc = infos[0]["Description"]
        
        while self.tournoi_model.current_round() < int(self.t_instances_rondes):

            print("ROUND ACTUEL : ", self.tournoi_model.current_round()+1)

            if self.tournoi_model.current_round()+1 > 1:
                # if existing round
                players = self.tournoi_model.retrieve_round()
                players_pairing = self.pairing_other_round(players)
                players_round = self.tournoi_views.views_round_input(players_pairing, self.tournoi_model.current_round()+1)
                self.tournoi_model.save_round_advance(players_round, self.tournoi_model.current_round()+1)
                print("----------------------------------------------------------")
                input("---------| Appuyer sur 'Entrée' pour continuer |----------")
            else:
                # if there is no round existing
                players = self.tournoi_model.retrieve_players_input_information()
                players_pairing = self.pairing_first_round(players)
                players_round = self.tournoi_views.views_round_input(players_pairing, self.tournoi_model.current_round()+1)
                self.tournoi_model.save_round_advance(players_round, self.tournoi_model.current_round()+1)

        self.tournoi_views.results()
        self.tournoi_model.save_finished_tournament()
     
    def start(self):
        use_gui = False

        #choix_gui_console = typer.confirm("Utiliser l'interface graphique ?")

        # hydrate tournoi retrieve avec les infos tournoi 
        # si pas de tournoi créé, demande les infos et en créé un 
        # si tournoi, récupère les infos dans la db

        self.clmenu.appliTitle()
        choix_gui = self.clmenu.cl_gui()

        # choice between GUI or console views
        if choix_gui == YES :
            use_gui = True
            MainWindow.goMainWindow()
        elif choix_gui == QUIT:
            print("Fin du programme.")
            quit()
        elif choix_gui == NO:
            while True:

                # main window
                choix_j_t = self.clmenu.welcom()

                # player window
                if choix_j_t == PLAYERS:

                    # player loop
                    while choix_j_t == PLAYERS:

                        # Add player window
                        choix_j = self.clmenu.player_menu()
                        if choix_j == ADD_PLAYER: 
                            infos_player = self.tournoi_add_player.ask_player_infos()
                            if infos_player == None:
                                pass
                            else:
                                self.tournoi_player.player_db_reg(infos_player[0],
                                                                    infos_player[1],
                                                                    infos_player[2],
                                                                    infos_player[3],
                                                                    infos_player[4]) 

                        # see player window                       
                        elif choix_j == SEE_PLAYER:
                            self.tournoi_add_player.reg_players()  
                        else: # back
                            break
                        
                # tournament window
                elif choix_j_t == TOURNAMENT:
                    
                    # tournament loop
                    while True: 
                        choix_mt = self.clmenu.tournamentMenu()
                        if choix_mt == NEW_TOURNAMENT:
                            if self.tournoi_model.test_current_tournament() == True:
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

                        # report window
                        elif choix_mt == REPORT:
                            while  True:

                                # player report window
                                choix_r = self.clmenu.rapports()
                                if choix_r == REPORT_PLAYERS:
                                    choix_rj = self.clmenu.rapportsJoueurs()
                                    if choix_rj == RP_ALL_PLAYERS_ALPHABETIC:
                                        self.clmenu.pAllPlayersAlphabetic()
                                    elif choix_rj == RP_ALL_PLAYERS_RANK:
                                        self.clmenu.pAllPlayersClassment()
                                    elif choix_rj == RP_ALL_PLAYERS_T:

                                        choix_rp = self.clmenu.pPlayerTournament()
                                        if choix_rp[0] == 1:
                                            self.clmenu.pTournamentAlphabetic()
                                        elif choix_rp[0] == 2:
                                            self.clmenu.pTournamentScore()
                                        else:
                                            pass
                                    else:
                                        break

                                # tournament report window
                                elif choix_r == REPORT_TOURNAMENT:
                                    choix_rt = self.clmenu.rapportTournois()
                                    
                                    if choix_rt[0] == RT_ALL_IR:
                                        self.clmenu.tMatchTournament()
                                        pass
                                    elif choix_rt[0] == RT_ALL_ROUND:
                                        self.clmenu.tToursTournament()
                                        pass
                                    else:
                                        break
                                else:
                                    break
                        else:
                            break
                else:
                    print("Fin du programme.")
                    quit()
        else:
            print("Quitter")
            quit()
