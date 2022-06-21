from controllers.controller_adavance_tournament import AdvanceTournamentController
from models.model_advanced_tournament import ModelAdvancedTournament
from models.model_new_tournament import ModelNewTournament
from models.models_save_round import SaveAdvanceTournamentModel
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
tn.new_tournament_infos()
tn.input_tournament_db_reg()
tn.save_input_tournament_db_reg()
"""

ta = ModelAdvancedTournament() 
tn = AdvancedTournamentViews()
td = AdvanceTournamentController()
ta.retrieve_tournament() # recupère les infos dans la db
ta.pairing_first_round() # fait les paires
for i in range((len(ta.my_paires))):
    if i == 0:
        tn.views_round_input(ta.my_paires)
        td.joueur_extra_infos()
        #ta.save_advance()
    print("tour : ", i)

#SaveAdvanceTournamentModel().save_advance()
