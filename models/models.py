import os, os.path
from os.path import exists
import datetime
from re import I
from numpy import sort
from tinydb import TinyDB, where

class PlayerModel:
    def __init__(self):
        pass

    def player_id(self):
        return id(PlayerModel)

    def player_db_reg(self, l_name, f_name, b_day, gender, rank): # enregistre les infos joueurs dans la base donnée
        '''
        Enregistre le joueur dans la db
        '''
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/players_data_base")
        except FileExistsError:
            pass
        # ----.json creation----
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json") # obj creation and path
        self.db.default_table_name = "Players" # table name

        self.db.insert({"id_player": self.player_id(),
                        "Nom" : l_name, 
                        "Prenom" : f_name, 
                        "Date de naissance" : b_day,
                        "Genre" : gender, 
                        "Rang" : rank,
                        "Score" : 0.0}) 

        self.db.close()

    def save_round_advance(self, players_infos:list, round:int):
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = f"Round {str(round)}"  # table name
        print("Round :", round)
        for i in range(len(players_infos)):
            #print("players infos", players_infos)
            joueur_1_id    = players_infos[i][0]['id_player']
            joueur_1_score = players_infos[i][0]['Score']
            joueur_2_id    = players_infos[i][1]['id_player']
            joueur_2_score = players_infos[i][1]['Score']
            joueurs = [joueur_1_id, joueur_1_score, joueur_2_id, joueur_2_score]
            print(f"Sauvegarde ronde {i+1} : ", joueurs)
            db_save.insert({f"Ronde {i+1}" : joueurs})

        db_save.close()

    def retrievePlayerFromNumber(self, lst_number):
        nb_player = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        nb_player.default_table_name = 'Players'

        lst_id = []

        for i in lst_number:
            lst_id.append(nb_player.get(doc_id=i)['id_player'])

        return lst_id
                        
class ReportModel:
    def __init__(self) -> None:
        self.db_players = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.path_finished_tournament = "./chess_data_base/tounament/finished_tournaments"

    def allPlayerAlphabeticSort(self):
        '''
        Return list of all player sort by alphabetic order from db
        Format : [{'...':..., '...':..., ...},{},...]
        '''
        apas = self.db_players
        apas.default_table_name = "Players"
        apas_tri = apas.all() 
        apas_tri = sorted(apas_tri, key=lambda x: x['Nom'])
        apas.close()

        return apas_tri

    def allPlayerScoreSort(self):
        '''
        Return list of all player sort by rank from db
        Format : [{'...':..., '...':..., ...},{},...]
        '''
        apss = self.db_players
        apss.default_table_name = "Players"
        apss_tri = apss.all() 
        apss_tri = sorted(apss_tri, key=lambda x: x['Rang'], reverse=True)
        apss.close()
        
        return apss_tri

    def playerAlphabeticSort(self, path_tournament:str):
        '''
        Return sorted list of players by alphabetic order from one tournament
        '''

        players_sort_name = []

        for i in self.idPlayerFromOneTournament(path_tournament):
            players_id = self.informationPlayerFromId(i)
            for n in players_id:
                players_sort_name.append(n)

        players_sort_name = sorted(players_sort_name, key=lambda x: x['Nom'])

        return players_sort_name

    def playerScoreSort(self, path_tournament:str):
        '''
        Return sorted list of players by score from one tournament
        '''
        players_sort_score = []

        for i in self.idPlayerFromOneTournament(path_tournament):
            players_id = self.informationPlayerFromId(i)
            for n in players_id:
                players_sort_score.append(n)

        players_sort_score = sorted(players_sort_score, key=lambda x: x['Rang'], reverse=True)

        return players_sort_score

    def allRondes(self, tournament_path):
        '''
        Return all result from a tournament 
        '''

        #tournament_path = './chess_data_base/tounament/finished_tournaments/tournament_2936352514832_infos.json'

        tables = []

        all_rondes = TinyDB(tournament_path)
        rounds = all_rondes.tables()
        rounds = sorted(rounds)
        rounds = rounds[:-1]

        for i in rounds : 
            all_rondes.default_table_name = i
            table_simple = all_rondes.all()
            tables.append(table_simple)

        return tables

    def nameFinishedTournament(self):
        '''
        Retourne une liste .json présents dans le repertoire 'finished_tournament'
        Format ['...','...',...]
        '''
        l_tournament = []

        for i in os.listdir(self.path_finished_tournament):
            db_tournament = f"./chess_data_base/tounament/finished_tournaments/{i}"
            l_tournament.append(db_tournament)

        return l_tournament

    def finishedTournamentNb(self, number):
        '''
        - Return all informations of tournament select by number
        - Return 3 lists
        - Format : ([infos,tournament,...],[{'Rondes n:[[[...,...][...,...]]]},{}],[[{infos : player}],[{}]])
        '''
        pdb = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        pdb.default_table_name = 'Players'

        inc_01 = 1
        inc_02 = 0

        lst_tournament = self.nameFinishedTournament()

        selct_path = lst_tournament[int(number)-1]

        list_score_player = []
        list_score_player_name = []

    # tournement infos
        finish_infos = TinyDB(selct_path)
        finish_infos.default_table_name = "Save_Input_Tournament"
        infos = finish_infos.all()

    # tournee infos
        finish_infos.default_table_name = "Tournees"
        infos_match = finish_infos.all()

        for i in infos_match:
            coucou = i[f'Ronde {inc_01}']
            for n in coucou:
                for e in n:
                    list_score_player.append(e)
            inc_01 += 1
        
        for i in list_score_player:
            
            list_score_player_name.append(pdb.search(where('id_player') == i[0]))
            
            list_score_player_name[inc_02][0]['Score'] = 0.0
            list_score_player_name[inc_02][0]['Score'] = i[1]
            #print("i", i[1], " ---- ", "ID ", list_score_player_name[inc_02][0]['id_player'], " --- Score ", list_score_player_name[inc_02][0]['Score'])
            inc_02 += 1
        #print(list_score_player_name)
                
        return [infos[0]['Name'],
                infos[0]['Place'],
                infos[0]['Date_start'],
                infos[0]['Date_end'],
                infos[0]['Match'],
                infos[0]['Instance_Rondes'],
                infos[0]['Time']], list_score_player_name

    def allPlayerOfAllPassedTournament(self):
        '''
        Retourne la liste complète d'id joueur ayant participé aux tournois
        Format : [[...,...,...][...,...,...],[],...]
        '''
        l_joueurs_tournois = []

        for i in self.nameFinishedTournament():
            db_temp = TinyDB(i)
            db_temp.default_table_name = "Save_Input_Tournament"
            joueurs = db_temp.all()
            l_joueurs_tournois.append(joueurs[0]['Players'])
            db_temp.close()
        return l_joueurs_tournois

    def idPlayerFromOneTournament(self, path):
        '''
        Return the list of players from the specify tournament 
        '''
        self.db_tp = TinyDB(path)
        self.db_tp.default_table_name = "Save_Input_Tournament"

        players_one_tournament = self.db_tp.all()[0]['Players']
        self.db_tp.close()

        return players_one_tournament

    def informationPlayerFromId(self, idplayer):
        '''
        Return player information from ID player
        Format [{...}]
        '''
        self.db_players.default_table_name = "Players"
        deSerialized_players_1 = self.db_players.search(where('id_player') == idplayer)
        

        return deSerialized_players_1 

class TournamentModel:
    def __init__(self, 
                 t_name = "", 
                 t_place = "", 
                 t_date_start = "", 
                 t_date_end = "",  
                 t_tour = 0, 
                 t_instance_ronde = 0, 
                 t_players = [], 
                 t_time = "", 
                 t_desc = ""):
        
        self.t_name           = t_name
        self.t_place          = t_place
        self.t_date_start     = t_date_start
        self.t_date_end       = t_date_end
        self.t_tour           = t_tour
        self.t_instance_ronde = t_instance_ronde
        self.t_players        = t_players
        self.t_time           = t_time
        self.t_desc           = t_desc

        self.id_round = 1

    def id_tournament(self):
        '''
        Return id object of tournament
        '''
        return id(TournamentModel)

    def save_input_tournament_db_reg(self):
        '''
        Save tournament infos in db
        '''
        # folder creation
        try:
            os.makedirs("./chess_data_base/tounament/actual_tournament")
        except FileExistsError:
            pass

        # .json creation
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        db_save.default_table_name = "Save_Input_Tournament" # table name

        db_save.insert({"id_tournament"  : self.id_tournament(),
                        "Name"           : self.t_name,
                        "Place"          : self.t_place, 
                        "Date_start"     : self.t_date_start,
                        "Date_end"       : self.t_date_end,
                        "Match"          : self.t_tour,
                        "Instance_Rondes": int(self.t_instance_ronde), 
                        "Players"        : self.t_players,
                        "Time"           : self.t_time,
                        "Description"    : self.t_desc})

    def save_round_advance(self, players_infos:list, instance_ronde:int):
        '''
        Save ronde in db
        '''
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        db_save.default_table_name = "Tournees" # table name

        lst_tour = []

        print("Round :", instance_ronde)

        for i in range(len(players_infos)):
            joueur_1_id    = players_infos[i][0]['id_player']
            joueur_1_score = players_infos[i][0]['Score']
            joueur_2_id    = players_infos[i][1]['id_player']
            joueur_2_score = players_infos[i][1]['Score']
            joueurs = [[joueur_1_id, joueur_1_score], [joueur_2_id, joueur_2_score]]
            print(f"Sauvegarde Match {i+1} : ", joueurs)
            lst_tour.append(joueurs)

        db_save.insert({f"Ronde {instance_ronde}" : lst_tour})

        db_save.close()

    def save_finished_tournament(self):
        '''
        - move json file of the finished tournament in 'finished_tournament' forlder
        '''
        ct_id = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        ct_id.default_table_name = "Save_Input_Tournament"
        ct_id_ls = ct_id.all()
        ct_id.close()

        # folder creation
        try:
            os.makedirs("./chess_data_base/tounament/finished_tournaments")
        except FileExistsError:
            pass

        path = "./chess_data_base/tounament/actual_tournament/save_tournament_infos.json"
        path_replace = f"./chess_data_base/tounament/finished_tournaments/{ct_id_ls[0]['Name']}-{ct_id_ls[0]['id_tournament']}.json"
        os.rename(path, path_replace.replace(" ", "_"))

    @staticmethod
    def clear_tournament():
        '''
        delete the actual json file of tournament
        '''
        file_path = "./chess_data_base/tounament/actual_tournament/save_tournament_infos.json"

        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            "no file found at this path"

    def retrieve_tournament(self):
        '''
        - return the information's list of tournament
        - format : [{key:value, key:value, ...}]
        '''
        current_tournament = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        current_tournament.default_table_name = "Save_Input_Tournament"
        tournament = current_tournament.all()

        current_tournament.close()

        return tournament

    def retrieve_round(self): 
        ''' 
        - Return a list with players and score at the last round
        - Format => [{...}{...}{...}...]
        '''
        player_ids = []

        rtt = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")

        if self.current_round() == 0:

            match = self.retrieve_players_input_information()

            # match ormat => [{...}{...}{...}...]
            return match

        else:
            rtt.default_table_name = "Tournees"
            match = rtt.all()
            match = match[self.current_round()-1][f'Ronde {self.current_round()}']

        pdb = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        pdb.default_table_name = "Players"
        
        for n in match:
            for j in n:
                    
                # deserialize
                player = pdb.search(where('id_player') == j[0]) 
                        
                # change score
                player[0]['Score'] = j[1]

                # make new list of player with new score
                player_ids.append(*player)

        rtt.close()

        return player_ids

    def retrieve_all_player_from_db(self):
        '''
        - Retlist of all players from db
        '''
        ap = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        ap.default_table_name = "Players"
        allplayers = ap.all()

        ap.close()
        
        return allplayers

    def retrieve_players_input_information(self): 
        '''
        - Return list of players input from the views
        - format input [...,...]
        - Format output [{...},{...}...] 
        '''
        self.ct = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        self.ct.default_table_name = "Save_Input_Tournament"

        self.current_tournament = self.ct.all()

        # list of id players from infos tournament
        player_ids  = self.current_tournament[0]['Players']

        # --- retrieve players deserializer ---
        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.db.default_table_name = "Players"

        self.players= []

        for i in player_ids:
            deSerialized_players = self.db.search(where('id_player') == i) 
            self.players.append(*deSerialized_players)

        self.ct.close()
        
        return self.players

    def sorted_players(self):
        '''
        - Return sorted list by score
        - Format => [{}{}...]
        '''
        score_final = self.retrieve_round()
                
        score_tri = sorted(score_final, key=lambda x:(x['Score'], x['Rang']), reverse=True)

        return score_tri   

    def current_round(self):
        '''
        Return the actual round
        '''
        cr = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        cr.default_table_name = 'Tournees'

        tables_nb = len(cr.all())

        cr.close()
        
        return tables_nb

    def test_current_tournament(self):
        '''
        - Return True if 'save_tournament_infos.json' exist
        ''' 
        path = "./chess_data_base/tounament/actual_tournament/save_tournament_infos.json" 
        if os.path.exists(path):
            return True
        return False

    def test_current_round(self): 
        '''
        - Return True if there is a round begun
        '''
        round_db = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables = round_db.tables() 
        tables_nb = len(tables)

        round_db.close()

        if tables_nb > 1:
            return True
        return False

coucou = ReportModel()
print(coucou.finishedTournamentNb(3))