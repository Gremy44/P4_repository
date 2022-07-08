from controllers.tournament_controller import TournamentController
from models.tournament_model_write import ModelRetrieveTournament, ModelWritePlayer, ModelWriteTournament
from views.views_tournament import MainWindow, ViewsTournament
import typer

tournoi_controller = TournamentController()
tournoi_views = ViewsTournament()
tournoi_retrieve = ModelRetrieveTournament()
tournoi_players_retrieve = ModelRetrieveTournament()
tournoi_write_player = ModelWritePlayer()
tournoi_finished = ModelWriteTournament()

choix_gui_console = typer.confirm("Utiliser l'interface graphique ?")

if choix_gui_console :
    MainWindow.goGui()

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