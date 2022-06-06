#for import script from other repertory
from itertools import permutations
import os, sys
import random
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from tinydb import TinyDB, Query

from controllers.functions import create_directory


class Tournament:
    def __init__(self, name, place, date, nb_round, rondes, player, time, description):
        self.name = name
        self.place = place
        self.date = date
        self.nb_round = nb_round
        self.rondes = rondes
        self.player = player
        self.time = time
        self.description = description

    def reg_infos_tournament(self):
        
        create_directory("../P4/models/tournament_datas")

        db = TinyDB(f'../P4/models/tournament_datas/{self.name}.json')
        #db.update(all(db))
        db.insert({"Nom" : self.name, "Lieu" : self.place, "Date" : self.date,
                   "Nombre de tours" : self.nb_round, "Rondes" : self.rondes,
                   "Nombre de joueurs" : self.player, "Temps" : self.time,
                   "Description" : self.description})
        return print(self.name)

    


