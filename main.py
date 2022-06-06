import os
from models.mod_tournament import Tournament
from controllers.functions import ask_informations_tournament, ask_informations_player
from views.players import Create_Players

#1. Créer un nouveau tournoi.
#2. Ajouter huit joueurs.
#3. L'ordinateur génère des paires de joueurs pour le premier tour.
#4. Lorsque le tour est terminé, entrez les résultats.
#5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.

#ti = ask_informations_tournament()

#tournois_1 = Tournament(ti[0], ti[1], ti[2], int(ti[3]), int(ti[4]), int(ti[5]), ti[6], ti[7])
#tournois_1.reg_infos_tournament()


ij = ask_informations_player()
player_1 = Create_Players(ij[0], ij[1], ij[2], ij[3], int(ij[4]))

id1 = id(player_1)
print(id1)

player_1.reg_infos_players(id1)

