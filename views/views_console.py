from models.models import PlayerModel, TournamentModel, ReportModel
import controllers.constants
import sys
import os

class AddPlayerViews:
    def __init__(self, l_name = "", f_name = "", b_day = "", gender = "", rank = 0.0):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank
        self.score = 0.0

    def ask_player_infos(self):
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|       _     _             _                        |--")
        print("--|      / \   (_) ___  _   _| |_ ___ _ __             |--")
        print("--|     / _ \  | |/ _ \| | | | __/ _ \ '__|            |--")
        print("--|    / ___ \ | | (_) | |_| | ||  __/ |               |--")
        print("--|   /_/   \_\/ |\___/_\__,_|\__\___|_|               |--")
        print("--|    _   _ |__/     (_) ___  _   _  ___ _   _ _ __   |--")
        print("--|   | | | | '_ \    | |/ _ \| | | |/ _ \ | | | '__|  |--")
        print("--|   | |_| | | | |   | | (_) | |_| |  __/ |_| | |     |--")
        print("--|    \__,_|_| |_|  _/ |\___/ \__,_|\___|\__,_|_|     |--")
        print("--|                 |__/                               |--")
        print("----------------------------------------------------------")
        print("------------------ | Ajouter un joueur | -----------------")
        print("----------------------------------------------------------")

        self.l_name = input(" | - Entrez nom : ")
        self.f_name = input(" | - Entrez prénom : ")
        self.b_day  = input(" | - Date d'anniversaire (jj/mm/aaaa): ")
        self.gender = input(" | - Genre (H/F/N) : ")
        self.rank   = input(" | - Rang : ")
    
        print(" -------------------------------------------------------- ")
        print("|Valider les informations et ajouter à la base de données|")
        print(" -------------------------------------------------------- ")
        print("| - 1 : Valider")
        print("| - 2 : Retour")
        print("| ------------------------------------------------------- ")
        val_player = input("| - Votre choix : ")

        if int(val_player) == 1:
            MenuViews.cls()
            return self.l_name, self.f_name, self.b_day, self.gender, self.rank, self.score
        else:
            MenuViews.cls()
            pass

        

        

    def reg_players(self):
        '''
        Retourne la liste des joueurs enregistrés dans la db
        '''
        tournoi_retrieve = TournamentModel()
        player_from_db = tournoi_retrieve.retrieve_all_player_from_db()
        inc_temp_01 = 1
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|      _                                             |--")
        print("--|     | | ___  _   _  ___ _   _ _ __ ___             |--")
        print("--|  _  | |/ _ \| | | |/ _ \ | | | '__/ __|            |--")
        print("--| | |_| | (_) | |_| |  __/ |_| | |  \__ \            |--")
        print("--|  \___/ \___/ \__,_|\___|\__,_|_|  |___/            |--")
        print("--|                            _     _         __      |--")
        print("--|   ___ _ __  _ __ ___  __ _(_)___| |_ _ __ /_/  ___ |--")
        print("--|  / _ \ '_ \| '__/ _ \/ _` | / __| __| '__/ _ \/ __||--")
        print("--| |  __/ | | | | |  __/ (_| | \__ \ |_| | |  __/\__ \|--")
        print("--|  \___|_| |_|_|  \___|\__, |_|___/\__|_|  \___||___/|--")
        print("--|                      |___/                         |--")
        print("----------------------------------------------------------")
        print("----------------- | Ajouter un joueur | ------------------")
        print("----------------------------------------------------------")
        print("")
        
        # delete the score line useless for the view 
        for i in player_from_db:
            del i['Score']

        for i in player_from_db:
            #data = list(i.items())
            #an_array = np.array(data)
            print()
            print(f'------ | Joueur N°{inc_temp_01} | ------')
            #print(an_array)
            for x, y in i.items():
                print(f" | - {x} : {y} ")
            inc_temp_01 += 1

        print("")
        input("Appuyez sur une touche pour continuer.")
        MenuViews.cls()

class TournamentViews:
    def __init__(self):
        self.id_round_views = TournamentModel().id_round
        self.complete_result = []
        self.t_players = []

        self.id_player = PlayerModel()

    def ask_tounament_infos(self):
        #self.cls()
        print(TournamentModel().current_round())
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|       _   _                                        |--")
        print("--|      | \ | | ___  _   ___   _____  __ _ _   _      |--")
        print("--|      |  \| |/ _ \| | | \ \ / / _ \/ _` | | | |     |--")
        print("--|      | |\  | (_) | |_| |\ V /  __/ (_| | |_| |     |--")
        print("--|      |_|_\_|\___/ \__,_| \_/ \___|\__,_|\__,_|     |--")
        print("--|      |_   _|__  _   _ _ __ _ __   ___ (_)          |--")
        print("--|        | |/ _ \| | | | '__| '_ \ / _ \| |          |--")
        print("--|        | | (_) | |_| | |  | | | | (_) | |          |--")
        print("--|        |_|\___/ \__,_|_|  |_| |_|\___/|_|          |--")
        print("----------------------------------------------------------")
        print("----------- | Entrez les information tournois | ----------")
        print("----------------------------------------------------------")
                                          
        self.t_name             = input(" | - Entrez nom : ")
        self.t_place            = input(" | - Entrez lieu : ")
        self.t_date_start       = input(" | - Entrez date de début : ")
        self.t_date_end         = input(" | - Entrez date de fin : ")
        self.t_tours            = 4
        self.t_instances_rondes = input(" | - Entrez instances rondes : ")
        print(" |   - Test : utiliser une liste déjà faite ?:")
        print(" | 1 - Utiliser liste déjà faite")
        print(" | 2 - Faire ma liste")
        cp = input(" |   - Entrez votre choix : ")
        if int(cp) == 1:
            self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720,
                              2123311234976, 1988607754144, 1384106246048, 2187293245344]
        else:                      
            for i in range(8):
                j_temp = input(f" | - Entrez le N° joueur du joueur N°:{i+1}/8 : ")
                self.t_players.append(int(j_temp))
            print(self.t_players)
            self.t_players = self.id_player.retrievePlayerFromNumber(self.t_players)
            print(self.t_players)
            
        self.t_time    = input(" | - Bullet/Blitz/coup rapide : ")
        self.t_desc    = input(" | - Entrez description : ")

        return self.t_name, self.t_place, self.t_date_start, self.t_date_end, self.t_tours, self.t_instances_rondes, self.t_players, self.t_time, self.t_desc

    def views_round_input(self, sorted_paires, ronde):
        '''
        - input pour les resulats de chaque round
        '''
        #self.cls()
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|             __  __       _       _                 |--")
        print("--|            |  \/  | __ _| |_ ___| |__              |--")
        print("--|            | |\/| |/ _` | __/ __| '_ \             |--")
        print("--|            | |  | | (_| | || (__| | | |            |--")
        print("--|            |_|  |_|\__,_|\__\___|_| |_|            |--")
        print("--|                                                    |--")
        print("----------------------------------------------------------")     
        print("-------------------- | round : ", ronde," | ---------------------")
        print("----------------------------------------------------------")

        for i in range(len(sorted_paires)):
            print("----------------------| Ronde", i+1,": |-----------------------")
            print("----------------------------------------------------------")
            print(sorted_paires[i][0]['Nom'],
                  sorted_paires[i][0]['Prenom'], " |--- VS ---| ",
                  sorted_paires[i][1]['Nom'],
                  sorted_paires[i][1]['Prenom'])
            score_p1 = input(f"| - Score joueur {sorted_paires[i][0]['Nom']} {sorted_paires[i][0]['Prenom']}: ")
            score_p2 = input(f"| - Score joueur {sorted_paires[i][1]['Nom']} {sorted_paires[i][1]['Prenom']}: ")
            sorted_paires[i][0]['Score'] = sorted_paires[i][0]['Score'] + float(score_p1)
            sorted_paires[i][1]['Score'] = sorted_paires[i][1]['Score'] + float(score_p2)
            print("")
        return sorted_paires 

    def results(self):
        self.cls()
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|        _____                            _          |--")
        print("--|       |_   _|__  _   _ _ __ _ __   ___ (_)         |--")
        print("--|         | |/ _ \| | | | '__| '_ \ / _ \| |         |--")
        print("--|         | | (_) | |_| | |  | | | | (_) | |         |--")
        print("--|        _|_|\___/ \__,_|_|  |_| |_|\___/|_|_        |--")
        print("--|       |_   _|__ _ __ _ __ ___ (_)_ __   /_/        |--")
        print("--|         | |/ _ \ '__| '_ ` _ \| | '_ \ / _ \       |--")
        print("--|         | |  __/ |  | | | | | | | | | |  __/       |--")
        print("--|         |_|\___|_|  |_| |_| |_|_|_| |_|\___|       |--")
        print("--|                                                    |--")
        print("----------------------------------------------------------")
                                       
        tournoi = TournamentModel().retrieve_tournament()
        inc_score = 1
        print("------------| Informations sur le tournoi : |-------------")
        print("----------------------------------------------------------")
        print("---------------| Résultats du tournois : |----------------")
        print("")
        score_final = TournamentModel().sorted_players()
        for i in score_final : 
            print(f"{inc_score} -  {i['Nom']} {i['Prenom']} au rang {i['Rang']} avec un score de {i['Score']}")
            inc_score += 1
        tournoi = TournamentModel().retrieve_tournament()
        print("")
        print("----------------------------------------------------------")
        input("---------| Appuyez sur 'entrée' pour continuer |----------")

    @staticmethod
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

class MenuViews:
    def __init__(self) -> None:
        self.cls()

    def appliTitle(self):
        print("---------------------------------------------------------------------------------------")
        print(" _____ _                     _____                                                 _   ")
        print("/  __ \ |                   |_   _|                                               | |  ")
        print("| /  \/ |__   ___  ___ ___    | | ___  _   _ _ __ _ __   __ _ _ __ ___   ___ _ __ | |_ ")
        print("| |   | '_ \ / _ \/ __/ __|   | |/ _ \| | | | '__| '_ \ / _` | '_ ` _ \ / _ \ '_ \| __|")
        print("| \__/\ | | |  __/\__ \__ \   | | (_) | |_| | |  | | | | (_| | | | | | |  __/ | | | |_ ")
        print(" \____/_| |_|\___||___/___/   \_/\___/ \__,_|_|  |_| |_|\__,_|_| |_| |_|\___|_| |_|\__|")
        print("---------------------------------------------------------------------------------------")
        print("-------------------- Bienvenu dans l'application Chess Tournament ---------------------")
        print("---------------------------------------------------------------------------------------")

    def cl_gui(self): 
        print("")
        print(" -------------------------------------------------")
        print("| Souhaitez-vous utiliser l'interface graphique ? |")
        print(" -------------------------------------------------")
        print("| - 1 : Oui")
        print("| - 2 : Non")
        print("| - 3 : Quitter")
        choix_gui = input("| - Votre choix : ")
        self.cls()

        return int(choix_gui)

    def welcom(self):
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|       ____  _                                      |--")
        print("--|      | __ )(_) ___ _ ____   _____ _ __  _   _      |--")
        print("--|      |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| | | |     |--")
        print("--|      | |_) | |  __/ | | \ V /  __/ | | | |_| |     |--")
        print("--|      |____/|_|\___|_| |_|\_/ \___|_| |_|\__,_|     |--")
        print("----------------------------------------------------------")
        print("-------------------------| Menu |-------------------------")                                                   
        print("----------------------------------------------------------")
        print("| - 1 : Joueurs")
        print("| - 2 : Tournoi")
        print("| - 3 : Quitter")
        choix_j_t = input("| - Votre choix : ")
        self.cls()

        return int(choix_j_t)

    def player_menu(self):
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|            _                                       |--")
        print("--|           | | ___  _   _  ___ _   _ _ __ ___       |--")
        print("--|        _  | |/ _ \| | | |/ _ \ | | | '__/ __|      |--")
        print("--|       | |_| | (_) | |_| |  __/ |_| | |  \__ \      |--")
        print("--|        \___/ \___/ \__,_|\___|\__,_|_|  |___/      |--")                                                
        print("----------------------------------------------------------")
        print("--------------------- | Menu Joueurs |--------------------")                                                   
        print("----------------------------------------------------------")
        print("| - 1 : Ajouter un joueur")
        print("| - 2 : Voir les joueurs existants")
        print("| - 3 : Retour")
        choix_j = input("| - Votre choix : ")    
        self.cls()                                      
        
        return int(choix_j)

    def tournamentMenu(self):
        self.cls()
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|         _____                            _         |--")
        print("--|        |_   _|__  _   _ _ __ _ __   ___ (_)        |--")
        print("--|          | |/ _ \| | | | '__| '_ \ / _ \| |        |--")
        print("--|          | | (_) | |_| | |  | | | | (_) | |        |--")
        print("--|          |_|\___/ \__,_|_|  |_| |_|\___/|_|        |--")
        print("----------------------------------------------------------")
        print("---------------------| Menu Tournoi |---------------------")                                                   
        print("----------------------------------------------------------")
        print("| - 1 : Nouveau tournoi")
        print("| - 2 : Reprendre le dernier tournoi")
        print("| - 3 : Rapports de tournois")
        print("| - 4 : Retour")
        choix_t = input("| - Votre choix : ")   
        self.cls()

        return int(choix_t)  

    def rapports(self):
        self.cls()
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|      ____                              _           |--")
        print("--|     |  _ \ __ _ _ __  _ __   ___  _ __| |_ ___     |--")
        print("--|     | |_) / _` | '_ \| '_ \ / _ \| '__| __/ __|    |--")
        print("--|     |  _ < (_| | |_) | |_) | (_) | |  | |_\__ \    |--")
        print("--|     |_| \_\__,_| .__/| .__/ \___/|_|   \__|___/    |--")
        print("--|                |_|   |_|                           |--")
        print("----------------------------------------------------------")
        print("-----------------------| Rapports |-----------------------")
        print("----------------------------------------------------------")
        print("| - 1 : Rapports sur les joueurs")
        print("| - 2 : Rapports sur les tournois")
        print("| - 3 : Retour")
        choix_r = input("| - Votre choix : ")   
        self.cls()

        return int(choix_r)

    def rapportsJoueurs(self):
        self.cls()
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|      ____                              _           |--")
        print("--|     |  _ \ __ _ _ __  _ __   ___  _ __| |_ ___     |--")
        print("--|     | |_) / _` | '_ \| '_ \ / _ \| '__| __/ __|    |--")
        print("--|     |  _ < (_| | |_) | |_) | (_) | |  | |_\__ \    |--")
        print("--|     |_| \_\__,_| .__/| .__/ \___/|_|   \__|___/    |--")
        print("--|         | | ___|_|   |_|___ _   _ _ __ ___         |--")
        print("--|      _  | |/ _ \| | | |/ _ \ | | | '__/ __|        |--")
        print("--|     | |_| | (_) | |_| |  __/ |_| | |  \__ \        |--")
        print("--|      \___/ \___/ \__,_|\___|\__,_|_|  |___/        |--")
        print("----------------------------------------------------------")
        print("-------------------| Rapports Joueurs |-------------------")
        print("----------------------------------------------------------")                                   
        print("| - 1 : Tous les joueurs par ordre alphabétique")
        print("| - 2 : Tous les joueurs par classement")
        print("| - 3 : Tous les joueurs d'un tournoi par ordre alphabétique")
        print("| - 4 : Tous les joueurs d'un tournoi par classement")
        print("| - 5 : Retour")
        choix_rj = input("| - Votre choix : ")

        return choix_rj

    def rapportTournois(self):
        self.cls()
        inc_1 = 1
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|      ____                              _           |--")
        print("--|     |  _ \ __ _ _ __  _ __   ___  _ __| |_ ___     |--")
        print("--|     | |_) / _` | '_ \| '_ \ / _ \| '__| __/ __|    |--")
        print("--|     |  _ < (_| | |_) | |_) | (_) | |  | |_\__ \    |--")
        print("--|     |_|_\_\__,_| .__/| .__/ \___/|_|  _\__|___/    |--")
        print("--|     |_   _|__  |_| _ |_|_ _ __   ___ (_)___        |--")
        print("--|       | |/ _ \| | | | '__| '_ \ / _ \| / __|       |--")
        print("--|       | | (_) | |_| | |  | | | | (_) | \__ \       |--")
        print("--|       |_|\___/ \__,_|_|  |_| |_|\___/|_|___/       |--")
        print("----------------------------------------------------------")
        print("------------------| Liste des tournois |------------------")
        print("----------------------------------------------------------")                                   
        liste_tournament = ReportModel().nameFinishedTournament()
        for i in liste_tournament:
            print(f"--| Tournois N°{inc_1} : ", i[49:-5])
            inc_1 += 1
        print("----------------------------------------------------------")
        print("------------------| Liste des tournois |------------------") 
        print("| - 1 : Liste de tous les matchs d'un tournoi")
        print("| - 2 : Liste de tous les tours d'un tournoi")
        print("| - 3 : Retour")
        choix_rt = input("| - Votre choix : ")
        choix_rt = int(choix_rt)
        if choix_rt == 1:
            print("----------------------------------------------------------")
            print("-------------| Choisissez le N° du tournois |-------------")
            self.choix_nb_tournament = input("N° de tournois : ")
            return choix_rt, self.choix_nb_tournament
        elif choix_rt == 2:
            print("----------------------------------------------------------")
            print("-------------| Choisissez le N° du tournois |-------------")
            self.choix_nb_tournament = input("N° de tournois : ")
            return choix_rt, self.choix_nb_tournament
        return choix_rt, -1                                
        
    def tToursTournament(self):
        self.cls()
        infos_tournoi = ReportModel().finishedTournamentNb(self.choix_nb_tournament)
        inc_01 = 0
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("--|        _     _     _             _                 |--")
        print("--|       | |   (_)___| |_ ___    __| | ___  ___       |--")
        print("--|       | |   | / __| __/ _ \  / _` |/ _ \/ __|      |--")
        print("--|       | |___| \__ \ ||  __/ | (_| |  __/\__ \      |--")
        print("--|       |_____|_|___/\__\___|  \__,_|\___||___/      |--")
        print("--|       | |_ ___  _   _ _ __ ___                     |--")
        print("--|       | __/ _ \| | | | '__/ __|                    |--")
        print("--|       | || (_) | |_| | |  \__ \                    |--")
        print("--|        \__\___/ \__,_|_|  |___/                    |--")
        print("----------------------------------------------------------")
        print("-----------------| Informations Tournoi |-----------------") 
        print("-----------------------| Tour N°1 |-----------------------")                                            
        print("--| Nom du tournoi : ", infos_tournoi[0][0])
        print("--| Lieu du tournoi : ", infos_tournoi[0][1])
        print("--| Début : ", infos_tournoi[0][2], " |---| Fin : ", infos_tournoi[0][3])
        print("--| Tours : ", infos_tournoi[0][4], " |---| Rondes : ", infos_tournoi[0][5])
        print("--| Gestion du temps : ", infos_tournoi[0][6])
        print("------------------| Informations tours |------------------")
        for i in range(infos_tournoi[0][5]):
            ("----------------------------------------------------------")
            print(f"-----------------------| Tour N°{i} |-----------------------")
            for n in range(infos_tournoi[0][4]*2):
                print(infos_tournoi[1][inc_01])
                inc_01 += 1
        print(infos_tournoi)
        input("Appuyez sur 'Entrée' pour continuer")

    def existing_tournament(self):
        """
        vue pour demander confirmation de créer un nouveau tournoi si tournoi existant
        """
        print("----------------------------------------------------------")
        print("|   Un tournoi existant à été trouvé,                    |")
        print("|   voulez-vous en commencer un nouveau quand même ?     |")
        print("----------------------------------------------------------")
        print("| - 1 : Oui")
        print("| - 2 : Non")
        choix_nm = input("| - Votre choix : ")

        return int(choix_nm)  

    def start_tournament(self):
        self.cls()
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        print("-  ____                                                   -")
        print("- / ___|___  _ __ ___  _ __ ___   ___ _ __   ___ ___ _ __ -")
        print("-| |   / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / __/ _ \ '__|-")
        print("-| |__| (_) | | | | | | | | | | |  __/ | | | (_|  __/ |   -")
        print("- \____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\___\___|_|   -")
        print("-                                                         -")
        print("-----------------------------------------------------------")
        input("----| Appuyer sur 'entrée' pour démarrer le tournoi. |-----")
        self.cls()

    def resume_tournament(self):
        print("-----------------------------------------------------------")
        print("-----------------------------------------------------------")
        print("--|    ____                               _             |--")
        print("--|   |  _ \ ___ _ __  _ __ ___ _ __   __| |_ __ ___    |--")
        print("--|   | |_) / _ \ '_ \| '__/ _ \ '_ \ / _` | '__/ _ \   |--")
        print("--|   |  _ <  __/ |_) | | |  __/ | | | (_| | | |  __/   |--")
        print("--|   |_| \_\___| .__/|_|  \___|_| |_|\__,_|_|  \___|   |--")
        print("--|             |_|                                     |--")
        print("--|                                                     |--")
        print("-----------------------------------------------------------")
        input("----| Appuyer sur 'entrée' pour reprender le tournoi. |----")
        self.cls()

    def no_tournament(self):
        print("-----------------------------------------------------------")
        print("---------------| Pas de tournoi commencé |-----------------")
        print("-----------------------------------------------------------")
        input("----------| Appuyer sur 'entrée' pour continuer |----------")
                                                                                
    @staticmethod
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

