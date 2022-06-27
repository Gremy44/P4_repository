#from controllers.controller_add_player import AddPlayerController
#from controllers.tournament_controller import TournamentController

"""
#Nouveau joueur
run = AddPlayerController()
run.add_player()
"""

"""
#Nouveau tournois
tn = ModelNewTournament()
tn.new_tournament_infos()
tn.input_tournament_db_reg()
tn.save_input_tournament_db_reg()
"""

"""ta = ModelAdvancedTournament() 
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

#SaveAdvanceTournamentModel().save_advance()"""

exec(open("./controllers/tournament_controller.py").read())
#exec(open("./controllers/controller_add_player.py").read()) #add player