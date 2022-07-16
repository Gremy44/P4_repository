import os, os.path
import datetime
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
                        
class TournamentModel:
    def __init__(self, t_name = "", t_place = "", t_date_start = "",t_date_end = "",  t_round = 4, t_ronde = 4, t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720, 2123311234976, 1988607754144, 1384106246048, 2187293245344], t_time = "", t_desc = ""):
        
        self.t_name       = t_name
        self.t_place      = t_place
        self.t_date_start = t_date_start
        self.t_date_end   = t_date_end
        self.t_round      = t_round
        self.t_ronde      = t_ronde
        self.t_players    = t_players
        self.t_time       = t_time
        self.t_desc       = t_desc

        self.id_round = 0

    def id_tournament(self):
        return id(TournamentModel)

    def save_input_tournament_db_reg(self):
        '''
        Save tournament infos in db
        '''
        # ----directory creation----
        try:
            os.makedirs("./chess_data_base/tounament/actual_tournament")
        except FileExistsError:
            pass

        # ----.json creation----
        db_save = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json") # obj creation and path
        db_save.default_table_name = "Save_Input_Tournament" # table name
        db_save.insert({"id_tournament" : self.id_tournament(),
                        "Name"          : self.t_name,
                        "Place"         : self.t_place, 
                        "Date_start"    : self.t_date_start,
                        "Date_end"      : self.t_date_end,
                        "Round"         : self.t_round,
                        "Rondes"        : self.t_ronde, 
                        "Players"       : self.t_players,
                        "Time"          : self.t_time,
                        "Description"   : self.t_desc})

        db_save.close()

    def save_finished_tournament(self):
        '''
        - move json file of the finished tournament in 'finished_tournament' forlder
        '''
        ct_id = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        ct_id.default_table_name = "Save_Input_Tournament"
        ct_id_ls = ct_id.all()
        ct_id.close()
        # ----directory creation----
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
        - retourne la liste avec les informations du tournoi
        - format : [{key:value, key:value, ...}]
        '''
        current_tournament = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        current_tournament.default_table_name = "Save_Input_Tournament"
        tournament = current_tournament.all()

        current_tournament.close()

        return tournament
    
    def retrieve_all_player_from_db(self):
        '''
        - Retourne liste de tous les joueurs de la db
        '''
        ap = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        ap.default_table_name = "Players"
        allplayers = ap.all()

        ap.close()
        
        return allplayers

    def retrieve_players_input_information(self): 
        '''
        - Retourne liste joueur ordre input tournoi
        - Format [[{...}],[{...}]...]
        '''
        self.ct = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        self.ct.default_table_name = "Save_Input_Tournament"
        self.current_tournament = self.ct.all()

        #self.name   = self.current_tournament[0]['Name']
        #self.place  = self.current_tournament[0]['Place']
        #self.date   = self.current_tournament[0]['Date']
        #self.round  = self.current_tournament[0]['Round']
        #self.tourne = self.current_tournament[0]['Tourne']
        player_ids  = self.current_tournament[0]['Players']
        #self.time   = self.current_tournament[0]['Time']
        #self.desc   = self.current_tournament[0]['Description']

        # --- retrieve players deserializer ---

        self.db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        self.db.default_table_name = "Players"
        self.players= []
        for i in player_ids:
            deSerialized_players = self.db.search(where('id_player') == i) 
            self.players.append(deSerialized_players)

        self.ct.close()
        
        return self.players

    def current_round(self):
        '''
        Retourne le round actuel
        '''
        cr = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables_nb = len(cr.tables())-1

        cr.close()
        
        return tables_nb

    def test_current_tournament(self):
        '''
        - Retourne True si fichier infos tournoi existe
        ''' 
        path = "./chess_data_base/tounament/actual_tournament/save_tournament_infos.json" 
        if os.path.exists(path):
            return True
        return False

    def test_current_round(self): 
        '''
        - Retourne True si des rounds ont étés commencés
        '''
        round_db = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables = round_db.tables() # donne les tables dans le fichier
        tables_nb = len(tables)
        if tables_nb > 1:
            return True
        return False

    def retrieve_round(self): 
        ''' 
        - Retourne une liste avec les joueurs et les scores au dernier round
        - Format => [[{...}{...}][{...}{...}]...]
        '''
        compt_1 = 1
        
        rtt = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        tables_name = rtt.tables() # donne les tables dans le fichier
        self.id_round = len(tables_name)
        ma_table = rtt.table(f'Round {self.id_round-1}').all() # donne les infos de la dernière table

        pdb = TinyDB("./chess_data_base/players_data_base/players_data_base.json")
        pdb.default_table_name = "Players"

        player_ids = []
        self.players = []

        for i in ma_table:
            #print("Table actuelle : ", i)
            #deserialise les joueurs
            deSerialized_players_1 = pdb.search(where('id_player') == i[f"Ronde {compt_1}"][0]) 
            deSerialized_players_2 = pdb.search(where('id_player') == i[f"Ronde {compt_1}"][2])
            #créé la liste des joueurs
            player = [*deSerialized_players_1, *deSerialized_players_2]
            #ajoute leur score actuel
            player[0]['Score'] = i[f"Ronde {compt_1}"][1]
            player[1]['Score'] = i[f"Ronde {compt_1}"][3]
            player_ids.append(player)
            compt_1 += 1

        rtt.close()

        return player_ids

    def sorted_players(self):
        '''
        - Retourne la liste trié par score des joueurs
        - Format => [{}{}...]
        '''
        score_non_tri = []
        score_final = self.retrieve_round()
        for i in score_final:
            for n in i:
                score_non_tri.append(n)
        score_tri = sorted(score_non_tri, key=lambda x:(x['Score'], x['Rang']), reverse=True)
        return score_tri   

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

        tournament_path = './chess_data_base/tounament/finished_tournaments/tournament_2936352514832_infos.json'

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

class TournamentModel2:
    def __init__(self, 
                 t_name = "", 
                 t_place = "", 
                 t_date_start = "", 
                 t_date_end = "",  
                 t_tour = 4, 
                 t_instance_ronde = 4, 
                 t_players = [3042972155808, 
                              2520259116960, 
                              2835596394400, 
                              2498757410720, 
                              2123311234976, 
                              1988607754144, 
                              1384106246048, 
                              2187293245344], 
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

        self.id_round = 0

        self.tournament_infos_from_db = TinyDB("./chess_data_base/tounament/actual_tournament/save_tournament_infos.json")
        self.players_infos_from_db = TinyDB("./chess_data_base/players_data_base/players_data_base.json")

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
        db_save = self.tournament_infos_from_db
        db_save.default_table_name = "Save_Input_Tournament" # table name

        db_save.insert({"id_tournament"  : self.id_tournament(),
                        "Name"           : self.t_name,
                        "Place"          : self.t_place, 
                        "Date_start"     : self.t_date_start,
                        "Date_end"       : self.t_date_end,
                        "Match"          : self.t_tour,
                        "Instance_Rondes": self.t_instance_ronde, 
                        "Players"        : self.t_players,
                        "Time"           : self.t_time,
                        "Description"    : self.t_desc})

        db_save.close()

    def save_round_advance(self, players_infos:list, instance_ronde:int):
        '''
        Save ronde in db
        '''
        db_save = self.tournament_infos_from_db
        db_save.default_table_name = "Tournees" # table name

        lst_tour = []

        print("Round :", instance_ronde)

        for i in range(len(players_infos)):
            #print("players infos", players_infos)
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
        ct_id = self.tournament_infos_from_db
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
        current_tournament = self.tournament_infos_from_db
        current_tournament.default_table_name = "Save_Input_Tournament"
        tournament = current_tournament.all()

        current_tournament.close()

        return tournament

    def retrieve_round(self): 
        ''' 
        - Return a list with players and score at the last round
        - Format => [{...}{...}{...}...]
        '''
        rtt = self.tournament_infos_from_db
        rtt.default_table_name = "Tournees"

        match = rtt.all()
        match = match[self.current_round()-1]
        
        pdb = self.players_infos_from_db
        pdb.default_table_name = "Players"

        player_ids = []

        for i in match.values():
            for n in i:
                for j in n:
                    # deserialize
                    player = pdb.search(where('id_player') == j[0]) 
                    
                    # change score
                    player[0]['Score'] = j[1]

                    # make new list of player with new score
                    player_ids.append(*player)

        return player_ids

    def retrieve_all_player_from_db(self):
        '''
        - Retlist of all players from db
        '''
        ap = self.players_infos_from_db
        ap.default_table_name = "Players"
        allplayers = ap.all()

        ap.close()
        
        return allplayers

    def retrieve_players_input_information(self): 
        '''
        - Return list of players input from the views
        - Format [{...},{...}...]
        '''
        self.ct = self.tournament_infos_from_db
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

    def current_round(self):
        '''
        Return the actual round
        '''
        cr = self.tournament_infos_from_db
        tables_nb = len(cr.tables())-1

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
        - Return True if there a round begun
        '''
        round_db = self.tournament_infos_from_db
        tables = round_db.tables() # donne les tables dans le fichier
        tables_nb = len(tables)
        if tables_nb > 1:
            return True
        return False
