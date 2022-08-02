from models.models import PlayerModel, TournamentModel, ReportModel
from views.views_console import AddPlayerViews, MenuViews, TournamentViews
from views.views_gui import AddPlayers, MainWindow
import controllers.constants as constants
import time


class InputVerification:
    """
    - Test the input
    """

    def test_num(self, mon_input, min, max):
        """
        - Test numeric value in the interval
        """
        while True:
            if mon_input.isdigit() and int(mon_input) >= min and int(mon_input) <= max:
                return int(mon_input)
            else:
                print("----------------------------------------------------------")
                mon_input = input(f"--| Entrez un chiffre valide compris entre {min} et {max} : ")

    def test_alpha(self, mon_input: str):
        """
        - Test alphabetic string
        """
        inp_tmp = mon_input.replace(" ", "")

        while True:
            if inp_tmp.isalpha():
                return mon_input
            else:
                mon_input = input("N'entrez que des lettres svp : ")

    def test_alpha_one_letter(self, mon_input):
        """
        - Test gender
        """
        while True:
            if mon_input.capitalize() == 'H' or mon_input.capitalize() == 'F' or mon_input.capitalize() == 'N':
                if len(mon_input) == 1:
                    return mon_input
                else:
                    mon_input = input("N'entrez seulement que 'H' ou 'F' ou 'N': ")
            else:
                mon_input = input("N'entrez seulement que 'H' ou 'F' ou 'N': ")

    def test_date(self, mon_input):
        """
        - Test date format
        """
        while True:
            if len(mon_input) == 10 and mon_input.count("/") == 2:
                if mon_input.replace("/", "").isdigit() is True:
                    return mon_input
                else:
                    mon_input = input("Entrez une date au format 'jj/mm/aaaa' : ")
            else:
                mon_input = input("Entrez une date au format 'jj/mm/aaaa' : ")

    def test_tournament(self, mon_input):
        """
        - Test value in tournament
        """
        while True:
            if mon_input == '0' or mon_input == '0.5' or mon_input == '1':
                return float(mon_input)
            else:
                print("----------------------------------------------------------")
                mon_input = input("--| Entrez une valeur valide ('0'/'0.5'/'1') : ")


class AddPlayerController:
    def __init__(self) -> None:
        pass

    def add_player(self):  # add new player to db
        add_player_view = MenuViews()
        infos_player = add_player_view.ask_player_infos()
        PlayerModel().player_db_reg(infos_player[0], infos_player[1],
                                    infos_player[2], infos_player[3],
                                    infos_player[4])

    def add_player_GUI(self):
        add_player_view = AddPlayers.send_add_player_infos()
        PlayerModel().player_db_reg(add_player_view[0], add_player_view[1],
                                    add_player_view[2], add_player_view[3],
                                    add_player_view[4])


class TournamentController:
    def __init__(self):
        self.tournoi_views = TournamentViews()
        self.tournoi_model = TournamentModel()
        self.tournoi_report = ReportModel()
        self.tournoi_player = PlayerModel()
        self.tournoi_add_player = AddPlayerViews()
        self.clmenu = MenuViews()

        self.infos_match = self.tournoi_model.retrieve_round()

    def infos_tournament_by_views(self):
        tournament_infos = TournamentViews().ask_tounament_infos()
        self.t_name = tournament_infos[0]
        self.t_place = tournament_infos[1]
        self.t_date_start = tournament_infos[2]
        self.t_date_end = tournament_infos[3]
        self.t_tours = tournament_infos[4]
        self.t_instances_rondes = tournament_infos[5]
        self.t_players = tournament_infos[6]
        self.t_time = tournament_infos[7]
        self.t_desc = tournament_infos[8]

    def pairing_first_round(self):
        '''
        - pair for first round
        '''
        my_paires = []

        # sorting suivant le rang

        tri = []
        tri = sorted(self.infos_match, key=lambda x: x['Rang'])  # tri par rang

        # determine le nombre de tour pour la boucle
        length_to_split = int(len(tri) / 2)

        for i in range(length_to_split):  # fait les paires
            paires_1 = [tri[i], tri[i + length_to_split]]
            my_paires.append(paires_1)

        return my_paires

    def pairing_other_round(self):
        '''
        - pair for other round
        '''
        mes_paires_temp = []
        my_paires = []

        pair = sorted(self.infos_match, key=lambda x: (x['Score'], x['Rang']))

        mod = 0
        for i in range(int(len(pair) / 2)):
            mes_paires_temp.append(pair[mod + i])
            mod += 1
            mes_paires_temp.append(pair[mod + i])
            my_paires.insert(i, mes_paires_temp)
            mes_paires_temp = []

        return my_paires

    def dateHourBegin(self):
        date_hour_begin = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return date_hour_begin

    def dateHourEnd(self):
        date_hour_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return date_hour_end

    def my_tournament_console(self):
        if not self.tournoi_model.test_current_tournament():

            # Hydrate object if there is no existing round
            self.infos_tournament_by_views()
            self.tournoi_write_tournament = TournamentModel(self.t_name,
                                                            self.t_place,
                                                            self.t_date_start,
                                                            self.t_date_end,
                                                            self.t_tours,
                                                            self.t_instances_rondes,
                                                            self.t_players,
                                                            self.t_time,
                                                            self.t_desc)
            self.tournoi_write_tournament.save_input_tournament_db_reg()
        else:

            # Retrieve and hydrate function if there is existing round
            infos = self.tournoi_model.retrieve_tournament()

            self.t_name = infos[0]["Name"]
            self.t_place = infos[0]["Place"]
            self.t_date_start = infos[0]["Date_start"]
            self.t_date_end = infos[0]["Date_end"]
            self.t_tours = infos[0]["Match"]
            self.t_instances_rondes = infos[0]["Instance_Rondes"]
            self.t_players = infos[0]["Players"]
            self.t_time = infos[0]["Time"]
            self.t_desc = infos[0]["Description"]

        while self.tournoi_model.current_round() < int(self.t_instances_rondes):

            # print("ROUND ACTUEL : ", self.tournoi_model.current_round()+1)

            if self.tournoi_model.current_round() + 1 > 1:
                # if existing round
                date_hour_bgn = self.dateHourBegin()  # save date hour begin in var
                players_pairing = self.pairing_other_round()  # make pairs
                players_round = self.tournoi_views.views_round_input(
                    players_pairing, self.tournoi_model.current_round() + 1)  # display + input
                date_hour_end = self.dateHourEnd()  # save date hour end in var
                self.tournoi_model.save_round_advance(
                    players_round, self.tournoi_model.current_round() + 1, date_hour_bgn, date_hour_end)

                print("----------------------------------------------------------")
                input("---------| Appuyer sur 'Entrée' pour continuer |----------")
            else:
                # if there is no round existing
                date_hour_bgn = self.dateHourBegin()
                players_pairing = self.pairing_first_round()
                players_round = self.tournoi_views.views_round_input(
                    players_pairing, self.tournoi_model.current_round() + 1)
                date_hour_end = self.dateHourEnd()
                self.tournoi_model.save_round_advance(
                    players_round, self.tournoi_model.current_round() + 1, date_hour_bgn, date_hour_end)

                print("----------------------------------------------------------")
                input("---------| Appuyer sur 'Entrée' pour continuer |----------")

        self.tournoi_views.results()
        self.tournoi_model.save_finished_tournament()

    def start(self):
        """
        - Console interface operation
        """
        self.clmenu.appliTitle()
        choix_gui = self.clmenu.cl_gui()

        # choice between GUI or console views
        if choix_gui == constants.YES:
            MainWindow.goMainWindow()
        elif choix_gui == constants.QUIT:
            print("Fin du programme.")
            quit()
        elif choix_gui == constants.NO:
            while True:

                # main window
                choix_j_t = self.clmenu.welcom()

                # player window
                if choix_j_t == constants.PLAYERS:

                    # player loop
                    while choix_j_t == constants.PLAYERS:

                        # Add player window
                        choix_j = self.clmenu.player_menu()
                        if choix_j == constants.ADD_PLAYER:
                            infos_player = self.clmenu.ask_player_infos()
                            if infos_player is None:
                                pass
                            else:
                                self.tournoi_player.player_db_reg(infos_player[0],
                                                                  infos_player[1],
                                                                  infos_player[2],
                                                                  infos_player[3],
                                                                  infos_player[4])

                        # see player window
                        elif choix_j == constants.SEE_PLAYER:
                            self.clmenu.reg_players()
                        else:  # back
                            break

                # tournament window
                elif choix_j_t == constants.TOURNAMENT:

                    # tournament loop
                    while True:
                        choix_mt = self.clmenu.tournamentMenu()
                        if choix_mt == constants.NEW_TOURNAMENT:
                            if self.tournoi_model.test_current_tournament() is True:
                                choix_nm = self.clmenu.existing_tournament()
                                if int(choix_nm) == constants.ERASE_LAST_FOUND_TOURNAMENT:
                                    self.tournoi_model.clear_tournament()
                                    self.my_tournament_console()
                                else:
                                    pass
                            else:
                                self.my_tournament_console()
                        elif choix_mt == constants.RETRIEVE_TOURNAMENT:
                            if self.tournoi_model.test_current_tournament() is True:
                                self.my_tournament_console()
                            else:
                                self.clmenu.no_tournament()

                        # report window
                        elif choix_mt == constants.REPORT:
                            while True:

                                # player report window
                                choix_r = self.clmenu.rapports()
                                if choix_r == constants.REPORT_PLAYERS:
                                    choix_rj = self.clmenu.rapportsJoueurs()
                                    if choix_rj == constants.RP_ALL_PLAYERS_ALPHABETIC:
                                        self.clmenu.pAllPlayersAlphabetic()
                                    elif choix_rj == constants.RP_ALL_PLAYERS_RANK:
                                        self.clmenu.pAllPlayersClassment()
                                    elif choix_rj == constants.RP_ALL_PLAYERS_T:

                                        choix_rp = self.clmenu.pPlayerTournament()
                                        if choix_rp[0] == 1:
                                            self.clmenu.pTournamentAlphabetic()
                                        elif choix_rp[0] == 2:
                                            self.clmenu.pTournamentScore()
                                        else:
                                            pass
                                    else:
                                        break

                                # tournament report window
                                elif choix_r == constants.REPORT_TOURNAMENT:
                                    choix_rt = self.clmenu.rapportTournois()

                                    if choix_rt[0] == constants.RT_ALL_IR:
                                        self.clmenu.tMatchTournament()
                                        pass
                                    elif choix_rt[0] == constants.RT_ALL_ROUND:
                                        self.clmenu.tToursTournament()
                                        pass
                                    else:
                                        break
                                else:
                                    break
                        else:
                            break
                else:
                    print("Fin du programme.")
                    quit()
        else:
            print("Quitter")
            quit()
