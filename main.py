from controllers.tournament_controller import TournamentController
from models.tournament_model_write import AddPlayerModel, ModelRetrieveTournament, ModelWritePlayer, ModelWriteTournament
from views.views_tournament import AddPlayerViews, ClMenu, MainWindow, ViewsTournament

def my_tournament():
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

    while tournoi_retrieve.current_round() < tournoi_controller.t_round:
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

    tournoi_views.results()
    tournoi_finished.save_finished_tournament()
    

tournoi_controller = TournamentController()
tournoi_views = ViewsTournament()
tournoi_retrieve = ModelRetrieveTournament()
tournoi_players_retrieve = ModelRetrieveTournament()
tournoi_write_player = ModelWritePlayer()
tournoi_finished = ModelWriteTournament()
tournoi_add_player = AddPlayerViews()
tournoi_add_player_model = AddPlayerModel()
clmenu = ClMenu()

use_gui = False

#choix_gui_console = typer.confirm("Utiliser l'interface graphique ?")

# hydrate tournoi retrieve avec les infos tournoi 
# si pas de tournoi créé, demande les infos et en créé un 
# si tournoi, récupère les infos dans la db

clmenu.appliTitle()
choix_gui = clmenu.cl_gui()


if choix_gui == 1 :
    use_gui = True
    MainWindow.goMainWindow()
elif choix_gui == 3:
    print("Fin du programme.")
    quit()
else:
    while True:
        choix_j_t = clmenu.welcom()
        if choix_j_t == 1:
            while choix_j_t == 1:
                choix_j = clmenu.player_menu()
                if choix_j == 1: # add player
                    infos_player = tournoi_add_player.ask_player_infos()
                    if infos_player == None:
                        pass
                    else:
                        tournoi_add_player_model.player_db_reg(infos_player[0],
                                                            infos_player[1],
                                                            infos_player[2],
                                                            infos_player[3],
                                                            infos_player[4])                        
                elif choix_j == 2: # view player reg
                    tournoi_add_player.reg_players()  
                else: # back
                    break
        elif choix_j_t == 2:
            while choix_j_t == 2: # boucle du menu tournoi
                choix_mt = clmenu.tournamentMenu()
                if choix_mt == 1:
                    if tournoi_retrieve.test_current_tournament() == True: # si tounoi existant
                        choix_nm = clmenu.existing_tournament()
                        if int(choix_nm) == 1:
                            tournoi_finished.clear_tournament()
                            my_tournament()
                        else:
                            pass 
                    else:  
                        my_tournament()   
                elif choix_mt == 2:
                    if tournoi_retrieve.test_current_tournament() == True:
                        my_tournament()
                    else:
                        clmenu.no_tournament()
                else:
                    break
        else:
            print("Fin du programme.")
            quit()


