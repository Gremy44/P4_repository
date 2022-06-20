from models.model_advanced_tournament import ModelAdvancedTournament
from models.model_new_tournament import ModelNewTournament
from views.views_add_player import AddPlayerViews
from views.views_advanced_tournament import AdvancedTournamentViews
from controllers.controller_add_player import AddPlayerController
from models.model_add_player import AddPlayerModel


"""
#Nouveau joueur
jv = AddPlayerModel()
jv.player_infos()
jv.player_db_reg()
"""

"""
#Nouveau tournois
tn = ModelNewTournament()
tn.ask_tounament_infos()
tn.input_tournament_db_reg()
"""

"""
ta = ModelAdvancedTournament()
ta.retrieve_tournament()
it = AdvancedTournamentViews(ta.pairing_first_round())
it.views_round_input()"""