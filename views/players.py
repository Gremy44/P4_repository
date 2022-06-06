from tinydb import TinyDB
import os
class Create_Players():
    def __init__(self, l_name:str="Jhon", f_name:str="Doe", b_day:str="00/00/00", gender:str="N", ranking:int=0):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.ranking = ranking

    def reg_infos_players(self,ident):# Player database
        # directory creation
        try:
            os.makedirs("../P4/models/player_data_base")
        except FileExistsError:
            pass

        # .json creation
        db = TinyDB(f'../P4/models/player_data_base/player_data_base.json')
        db.default_table_name = ident
        db.update(all(db))
        db.insert({"Nom" : self.l_name, "Prenom" : self.f_name, "Date de naissance" : self.b_day,
                   "Genre" : self.gender, "Rang" : self.ranking})
        return print(ident)
    




