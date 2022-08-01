from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QRadioButton, QLineEdit, QSpinBox, QDateEdit, QTextEdit, QLabel, QTableWidget, QTabWidget, QDoubleSpinBox, QPlainTextEdit
from PyQt6 import uic, QtWidgets
from models.models import PlayerModel, TournamentModel, ReportModel
import time
import sys


class ControllerGui(QMainWindow):
    def __init__(self) -> None:
        super(ControllerGui, self).__init__()

        self.tournoi_model = TournamentModel()
        self.tournoi_player = PlayerModel()

        self.list_players = self.tournoi_model.retrieve_players_input_information()
        self.list_player_other_round = self.tournoi_model.retrieve_round()
        self.actual_round = self.tournoi_model.current_round()
        self.my_paires = []

    def pairing_first_round(self):
        '''
        - Fait les pairs pour le premier round
        '''
        # sorting suivant le rang
        tri_temp = []
        tri = []
        # tri par rang
        tri = sorted(self.list_players, key=lambda x: x['Rang'])

        length_to_split = int(len(tri)/2)  # determine le nombre de tour pour la boucle

        for i in range(length_to_split):  # fait les paires
            paires_1 = [tri[i], tri[i+length_to_split]]
            self.my_paires.append(paires_1)

        return self.my_paires

    def pairing_other_round(self):
        '''
        - Fait les pairs pour les rounds autre que le premier
        '''
        tri_temp = []
        mes_paires_temp = []
        self.my_paires = []

        pair = sorted(self.list_player_other_round, key=lambda x: (x['Score'], x['Rang']))

        mod = 0
        for i in range(int(len(pair)/2)):
            mes_paires_temp.append(pair[mod+i])
            mod += 1
            mes_paires_temp.append(pair[mod+i])
            self.my_paires.insert(i, mes_paires_temp)
            mes_paires_temp = []

        return self.my_paires

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load the UI file
        uic.loadUi('./views/qt_ux/main_window.ui', self)

        # Define my widgets
        self.btn_players = self.findChild(QPushButton, "mw_joueurs")
        self.btn_tournaments = self.findChild(QPushButton, "mw_tournois")
        self.btn_quit = self.findChild(QPushButton, "mw_quitter")

        # Connecting to actions
        self.btn_players.clicked.connect(self.btnPlayers)
        self.btn_tournaments.clicked.connect(self.btnTournaments)
        self.btn_quit.clicked.connect(self.btnQuit)

        # Show the app
        self.show()

    def btnPlayers(self):
        self.t_to_players = PlayersWindow()
        self.t_to_players.show()
        self.close()

    def btnTournaments(self):
        self.t_to_tournament = Tournament()
        self.t_to_tournament.show()
        self.close()

    def btnQuit(self):
        self.close()

    @staticmethod
    def goMainWindow():
        app = QApplication(sys.argv)  # instantiate

        main_window = MainWindow()

        sys.exit(app.exec())  # execute

class PlayersWindow(QMainWindow):
    def __init__(self):
        super(PlayersWindow, self).__init__()

    # Load the UI file
        uic.loadUi('./views/qt_ux/players.ui', self)

    # Define widgets
        self.btn_addplayers = self.findChild(QPushButton, "AddPlayer")
        self.btn_seeplayers = self.findChild(QPushButton, "ListPlayers")
        self.btn_back = self.findChild(QPushButton, "Back")

    # Connecting to actions
        self.btn_addplayers.clicked.connect(self.btnAddPlayers)
        self.btn_seeplayers.clicked.connect(self.btnSeePlayers)
        self.btn_back.clicked.connect(self.btnBack)

    def btnAddPlayers(self):
        self.t_to_addplayers = AddPlayers()
        self.t_to_addplayers.show()
        self.close()

    def btnSeePlayers(self):
        self.t_to_seeplayers = PlayerList()
        self.t_to_seeplayers.show()
        self.close()

    def btnBack(self):
        self.t_to_back_main = MainWindow()
        self.t_to_back_main.show()
        self.close()

class AddPlayers(QMainWindow):
    def __init__(self):
        super(AddPlayers, self).__init__()

        self.gender = ""

        # Load the UI file
        uic.loadUi('./views/qt_ux/add_players.ui', self)

        # Define widgets
        self.line_l_name = self.findChild(QLineEdit, "p_l_name")
        self.line_f_name = self.findChild(QLineEdit, "p_f_name")
        self.date_bday = self.findChild(QDateEdit, "p_bday")
        self.rbtn_gender_h = self.findChild(QRadioButton, "rb_h")
        self.rbtn_gender_f = self.findChild(QRadioButton, "rb_f")
        self.rbtn_gender_n = self.findChild(QRadioButton, "rb_n")
        self.sb_rank = self.findChild(QSpinBox, "p_rank")
        self.btn_add = self.findChild(QPushButton, "add_player")
        self.btn_back = self.findChild(QPushButton, "add_player_back")

        # Connecting to actions
        self.btn_add.clicked.connect(self.btnAdd)
        self.btn_back.clicked.connect(self.btnBack)

    def btnAdd(self):
        self.t_to_players = PlayersWindow()
        self.send_add_player_infos()
        self.t_to_players.show()
        self.close()

    def btnBack(self):
        self.t_to_back_players = PlayersWindow()
        self.t_to_back_players.show()
        self.close()

    def send_add_player_infos(self):
        if self.rbtn_gender_h.isChecked() is True:
            self.gender = "H"
        elif self.rbtn_gender_f.isChecked() is True:
            self.gender = "F"
        else:
            self.gender = "N"

        self.sb_rank = str("{:04d}".format(int(self.sb_rank.text())))

        PlayerModel().player_db_reg(
            self.line_l_name.text(),
            self.line_f_name.text(),
            self.date_bday.text(),
            self.gender,
            self.sb_rank)

class PlayerList(QMainWindow):
    def __init__(self):
        super(PlayerList, self).__init__()

        # Load the UI file
        uic.loadUi('./views/qt_ux/player_list_view.ui', self)

        # Define widgets
        self.btn_back = self.findChild(QPushButton, "back")
        self.list_db = self.findChild(QTableWidget, "tableWidget")

        # Connecting to actions
        self.btn_back.clicked.connect(self.btnBack)

        # List Widget
        self.get_data()

    def get_data(self):
        players = TournamentModel().retrieve_all_player_from_db()
        row = 0
        self.tableWidget.setRowCount(len(players))
        for p in players:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(p['Nom']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p['Prenom']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p['Date de naissance']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(p['Genre']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(p['Rang']))
            row += 1

    def btnBack(self):
        self.t_to_back_players = PlayersWindow()
        self.t_to_back_players.show()
        self.close()

class Tournament(QMainWindow):
    def __init__(self):
        super(Tournament, self).__init__()

        # Load the UI file
        uic.loadUi('./views/qt_ux/tournament.ui', self)

        # Define widgets
        self.btn_new_tournament = self.findChild(QPushButton, "new_tournament")
        self.btn_resume_tournament = self.findChild(QPushButton, "resume_tournament")
        self.btn_reports = self.findChild(QPushButton, "reports")
        self.btn_back = self.findChild(QPushButton, "back")
        self.lbl_existing_t = self.findChild(QLabel, "label_2")

        # Connecting to actions
        self.btn_new_tournament.clicked.connect(self.btnNewT)
        self.btn_resume_tournament.clicked.connect(self.btnResumeT)
        self.btn_reports.clicked.connect(self.btnReports)
        self.btn_back.clicked.connect(self.btnBack)

        # state
        self.btn_resume_tournament.setEnabled(False)

        # Display message if there is an existing tournament
        if TournamentModel().test_current_tournament():
            self.lbl_existing_t.setText("Un tournoi existant à été trouvé")
            self.btn_resume_tournament.setEnabled(True)

    def btnNewT(self):
        self.t_to_newtournament = NewTournament()
        self.t_to_newtournament.show()
        self.close()

    def btnResumeT(self):
        self.t_to_resume_tournament = Resume()
        self.t_to_resume_tournament.show()
        self.close()

    def btnReports(self):
        self.t_to_report = ReportMain()
        self.t_to_report.show()
        self.close()

    def btnBack(self):
        self.t_to_back_main = MainWindow()
        self.t_to_back_main.show()
        self.close()

class NewTournament(QMainWindow):
    def __init__(self):
        super(NewTournament, self).__init__()

        # Variables
        self.time = ""
        self.date = ""

        # Load the UI file
        uic.loadUi('./views/qt_ux/new_tournament.ui', self)

        # Define widgets
        self.line_t_name = self.findChild(QLineEdit, "tournament_name")
        self.line_t_place = self.findChild(QLineEdit, "tournament_place")
        self.date_t_begin = self.findChild(QDateEdit, "tournament_begin")
        self.date_t_end = self.findChild(QDateEdit, "tournament_end")
        self.sb_t_round = self.findChild(QSpinBox, "tournament_round")
        self.sb_t_ronde = self.findChild(QSpinBox, "tournament_rondes")
        self.btn_players = self.findChild(QPushButton, "tournament_players")
        self.rbtn_blitz = self.findChild(QRadioButton, "qbt_blitz")
        self.rbtn_bullet = self.findChild(QRadioButton, "qbt_bullet")
        self.rbtn_cr = self.findChild(QRadioButton, "qbt_cr")
        self.desc = self.findChild(QTextEdit, "tournament_description")
        self.btn_validation = self.findChild(QPushButton, "tournament_validation")
        self.btn_back = self.findChild(QPushButton, "back")
        self.lbl_info = self.findChild(QLabel, "label_11")

        # Connecting to actions
        self.btn_players.clicked.connect(self.btnSelPlayers)
        self.btn_validation.clicked.connect(self.btnValidation)
        self.btn_back.clicked.connect(self.btnBack)

    def btnSelPlayers(self):
        self.lplayer = PlayerListSel()
        self.lplayer.show()

    def btnValidation(self):

        TournamentModel().clear_tournament()

        validation = 1

        try:
            self.player_to_db(self.lplayer.my_players)
        except AttributeError:
            self.lbl_info.setText("Veuillez remplir tous les champs avant de valider")
            validation = 0

        if validation == 1:
            id_players = self.player_to_db(self.lplayer.my_players)

            if self.rbtn_blitz.isChecked() is True:
                self.time = "Blitz"
            elif self.rbtn_bullet.isChecked() is True:
                self.time = "Bullet"
            else:
                self.time = "Coup rapide"

            tournoi_infos = TournamentModel(self.line_t_name.text(),
                                            self.line_t_place.text(),
                                            self.date_t_begin.text(),
                                            self.date_t_end.text(),
                                            int(self.sb_t_round.text()),
                                            int(self.sb_t_ronde.text()),
                                            id_players,
                                            self.time,
                                            self.desc.toPlainText()
                                            )

            tournoi_infos.save_input_tournament_db_reg()

            self.bplayer = Begin()
            self.bplayer.show()
            self.close()

    def btnBack(self):
        self.t_to_back_tournament = Tournament()
        self.t_to_back_tournament.show()
        self.close()

    def player_to_db(self, players_lst_from_gui: dict):
        """
        Return id players to db
        """
        id_player = []

        all_players = TournamentModel().retrieve_all_player_from_db()

        for i, n in zip(players_lst_from_gui.items(), all_players):
            if i[1] is True:
                id_player.append(n['id_player'])

        return id_player

class PlayerListSel(QMainWindow):
    def __init__(self):
        super(PlayerListSel, self).__init__()

        # variables
        self.players = TournamentModel().retrieve_all_player_from_db()
        self.element_true = 0
        self.my_players = {}

        for i in range(len(self.players)):
            self.my_players[i] = False

        # Load the UI file
        uic.loadUi('./views/qt_ux/player_list_sel.ui', self)

        # Define widgets
        self.lbl_player_sel = self.findChild(QLabel, "nb_player_sel")
        self.btn_validate = self.findChild(QPushButton, "back")
        self.list_db = self.findChild(QTableWidget, "tableWidget")

        # Connecting to actions
        self.btn_validate.clicked.connect(self.btnValidate)

        # List Widget
        self.get_data()

        # sel_table = QTableWidget()
        self.list_db.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected, deselected):
        a = None
        b = None
        self.element_true = 0

        for ix in selected.indexes():
            a = ix.row()

        for ix in deselected.indexes():
            b = ix.row()

        self.my_players[a] = True
        self.my_players[b] = False

        del self.my_players[None]  # del last key egual to none

        # return nb of select elements
        for i in self.my_players:
            if self.my_players[i] is True:
                self.element_true += 1

        self.lbl_player_sel.setText(f"{self.element_true} éléments sélectionnés sur 8")

        if self.element_true != 8:
            self.btn_validate.setFlat(True)
        else:
            self.btn_validate.setFlat(False)

    def get_data(self):
        row = 0
        self.tableWidget.setRowCount(len(self.players))
        for p in self.players:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(p['Nom']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p['Prenom']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p['Date de naissance']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(p['Genre']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(p['Rang']))
            row += 1

    def btnValidate(self):
        if self.element_true == 8:
            self.close()
            return self.my_players

class Begin(QMainWindow):
    def __init__(self):
        super(Begin, self).__init__()

    # Load the UI file
        uic.loadUi('./views/qt_ux/begin.ui', self)

    # Define widgets
        self.btn_validate = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_validate.clicked.connect(self.btnBegin)

    def btnBegin(self):

        self.n = QWRoundEmpty()
        self.n.show()
        self.close()

class QWRound(QMainWindow):
    def __init__(self):
        super(QWRound, self).__init__()

        self.validate_round = False

    # Load the UI file
        uic.loadUi('./views/qt_ux/mw_qw_round.ui', self)

    # Define widgets
        self.lbl_round = self.findChild(QLabel, "label")
        self.lbl_player_1 = self.findChild(QLabel, "label_3")
        self.lbl_player_2 = self.findChild(QLabel, "label_4")
        self.s_p_1 = self.findChild(QDoubleSpinBox, "doubleSpinBox_3")
        self.s_p_2 = self.findChild(QDoubleSpinBox, "doubleSpinBox_4")
        self.btn_v_round = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_v_round.setCheckable(True)
        self.btn_v_round.clicked.connect(self.btn_validate_round)

    def btn_validate_round(self):
        if self.btn_v_round.isChecked():
            btn = True
            self.s_p_1.setEnabled(False)
            self.s_p_2.setEnabled(False)
        else:
            btn = False
            self.s_p_1.setEnabled(True)
            self.s_p_2.setEnabled(True)
        return btn

class QWRoundEmpty(QMainWindow):
    def __init__(self):
        super(QWRoundEmpty, self).__init__()

    # Variables
        self.tournament_models = TournamentModel()
        self.players_models = PlayerModel()
        self.ctr_gui = ControllerGui()

        self.rondes = self.tournament_models.retrieve_tournament()[0]["Instance_Rondes"]
        self.rounds = self.tournament_models.retrieve_tournament()[0]["Match"]
        self.test_round = self.tournament_models.test_current_round()

        self.date_hour_bgn = ""
        self.date_hour_end = ""

        inc = 0

        if self.ctr_gui.actual_round < self.rondes:

        # Load the UI file
            uic.loadUi('./views/qt_ux/round_empty.ui', self)

        # Define Widgets

            self.tab_match = self.findChild(QTabWidget, "tabWidget")
            self.btn_validate_all_rondes = self.findChild(QPushButton, "pushButton_2")
            self.lbl_warning = self.findChild(QLabel, "label")

        # Connecting to actions
            self.tab_match.currentChanged.connect(self.tabChanged)
            self.btn_validate_all_rondes.clicked.connect(self.btnValidatAllRondes)

        # Instancing interface
            self.date_hour_bgn = self.dateHourBegin()

            if self.test_round is False:  # si pas de round
                self.my_players = self.ctr_gui.pairing_first_round()
            else:
                self.my_players = self.ctr_gui.pairing_other_round()
            for i in range(self.rounds):

                self.tab_match.addTab(QWRound(), f"Match {i+1}")

                self.tab_match.widget(i).lbl_round.setText(f"Round {self.ctr_gui.actual_round+1}")  # set round number

                self.tab_match.widget(i).lbl_player_1.setText(
                    f"{self.my_players[i][0]['Prenom']}\nScore : {self.my_players[i][0]['Score']}")  # set name p1
                self.tab_match.widget(i).lbl_player_2.setText(
                    f"{self.my_players[i][1]['Prenom']}\nScore : {self.my_players[i][1]['Score']}")  # set name p2

                inc += 2
        else:
            print("ici : ", self.ctr_gui.actual_round, " < ", self.rounds)
            print("coucoufinish")
            self.t_to_finish = Results()
            self.t_to_finish.show()
            self.close()

    def dateHourBegin(self):
        date_hour_begin = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return date_hour_begin

    def dateHourEnd(self):
        date_hour_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return date_hour_end

    def tabChanged(self):
        ind = self.tab_match.currentIndex()
        ind_2 = self.tab_match.widget(ind).btn_validate_round()
        print(ind_2)

        return ind

    def btnValidatAllRondes(self):
        lst_val = []

        for i in range(self.rounds):
            lst_val.append(self.tab_match.widget(i).btn_validate_round())

        if all(lst_val):  # if the 4 buttons are validate

            self.date_hour_end = self.dateHourEnd()

            for i in range(self.rounds):
                score_p1 = self.tab_match.widget(i).s_p_1.text().replace(',', '.')
                score_p2 = self.tab_match.widget(i).s_p_2.text().replace(',', '.')

                # change score for the round
                self.my_players[i][0]['Score'] = self.my_players[i][0]['Score'] + float(score_p1)
                self.my_players[i][1]['Score'] = self.my_players[i][1]['Score'] + float(score_p2)

            self.tournament_models.save_round_advance(
                self.my_players, self.ctr_gui.actual_round+1, self.date_hour_bgn, self.date_hour_end)

            self.t_to_round = QWRoundEmpty()
            self.t_to_round.show()
            self.close()

            return self.my_players

        else:
            self.lbl_warning.setText("Valider toutes les rondes pour pouvoir valider le round")

class Results(QMainWindow):
    def __init__(self):
        super(Results, self).__init__()

    # Variables
        self.tournament = TournamentModel()
        self.tournament_infos = self.tournament.sorted_players()
        print(self.tournament_infos)

    # Load the UI file
        uic.loadUi('./views/qt_ux/results.ui', self)

    # Define widgets
        self.btn_new_tournament = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_new_tournament.clicked.connect(self.btnFinish)

    # result list
        self.getData()

    def btnFinish(self):
        self.tournament.save_finished_tournament()
        self.t_to_tournament = Tournament()
        self.t_to_tournament.show()
        self.close()

    def getData(self):
        row = 0
        self.tableWidget.setRowCount(len(self.tournament_infos))
        for p in self.tournament_infos:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(p['Nom']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p['Prenom']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p['Rang']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(p['Score'])))
            row += 1

class Resume(QMainWindow):
    def __init__(self):
        super(Resume, self).__init__()

    # Load the UI file
        uic.loadUi('./views/qt_ux/resume.ui', self)

    # Define widgets
        self.btn_new_tournament = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_new_tournament.clicked.connect(self.btnResume)

    def btnResume(self):
        self.t_to_round = QWRoundEmpty()
        self.t_to_round.show()
        self.close()

class ReportMain(QMainWindow):
    def __init__(self):
        super(ReportMain, self).__init__()
    # set variables
        self.players = TournamentModel().retrieve_all_player_from_db()
        self.players = sorted(self.players, key=lambda x: x['Nom'])

        self.tournament = ReportModel().passedTournamentInfos()
        self.player_or_rank = True

        self.my_tournament = []
        for i in range(len(self.tournament)):
            self.my_tournament.append(False)

        self.a = -1
        self.b = -1
        self.element_true = 0

    # Load the UI file
        uic.loadUi('./views/qt_ux/reports.ui', self)

    # Define widgets
        self.rbtn_alphabetic = self.findChild(QRadioButton, "radioButton")
        self.rbtn_rank = self.findChild(QRadioButton, "radioButton_2")

        self.table_players = self.findChild(QTableWidget, "tableWidget")
        self.table_tournament = self.findChild(QTableWidget, "tableWidget_2")

        self.btn_tournament_player = self.findChild(QPushButton, "pushButton_3")
        self.btn_tournament_rondes = self.findChild(QPushButton, "pushButton_4")
        self.btn_tournament_match = self.findChild(QPushButton, "pushButton_5")

        self.btn_back = self.findChild(QPushButton, "pushButton")

    # List Widget

        self.get_data_player_table()
        self.get_data_tournament_table()

    # Connecting to actions
        self.rbtn_alphabetic.clicked.connect(self.rbtnChange)
        self.rbtn_rank.clicked.connect(self.rbtnChange)

        self.btn_tournament_player.clicked.connect(self.btnPlayer)
        self.btn_tournament_rondes.clicked.connect(self.btnRondes)
        self.btn_tournament_match.clicked.connect(self.btnMatch)

        self.btn_back.clicked.connect(self.btnBack)

    # sel_table = QTableWidget()
        self.table_tournament.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def rbtnChange(self):
        if self.rbtn_alphabetic.isChecked() is True:
            self.players = sorted(self.players, key=lambda x: x['Nom'])
            self.get_data_player_table()
        else:
            self.players = sorted(self.players, key=lambda x: x['Rang'], reverse=True)
            self.get_data_player_table()

    # get data first table
    def get_data_player_table(self):
        row = 0

        self.tableWidget.setRowCount(len(self.players))
        for p in self.players:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(p['Nom']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p['Prenom']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p['Date de naissance']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(p['Genre']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(p['Rang']))
            row += 1

    def get_data_tournament_table(self):
        row = 0

        self.tableWidget_2.setRowCount(len(self.tournament))
        for p in self.tournament:
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(p['Name']))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(p['Place']))
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(p['Date_start']))
            row += 1

    def on_selectionChanged(self, selected, deselected):  # return value of selected line

        for ix in selected.indexes():
            self.a = ix.row()

        for ix in deselected.indexes():
            self.b = ix.row()

        self.my_tournament[self.a] = True
        self.my_tournament[self.b] = False

        return self.a

    def btnPlayer(self):
        self.t_to_report_player = RPlayersTournament(self.a)
        self.t_to_report_player.show()

    def btnRondes(self):
        self.t_to_rondes = Rondes(self.a)
        self.t_to_rondes.show()

    def btnMatch(self):
        self.t_to_matchs = Matchs(self.a)
        self.t_to_matchs.show()

    def btnBack(self):
        self.t_to_tournament = Tournament()
        self.t_to_tournament.show()
        self.close()

class RPlayersTournament(QMainWindow):
    def __init__(self, value_a):
        super(RPlayersTournament, self).__init__()

        self.retrieve_infos = ReportModel().finishedTournamentNb(value_a+1)
        self.slice_r_i = self.retrieve_infos[1][-8:]

    # Load the UI file
        uic.loadUi('./views/qt_ux/report_players_tournament.ui', self)

    # Define widgets
        self.rbtn_alphabetic = self.findChild(QRadioButton, "radioButton")
        self.rbtn_rank = self.findChild(QRadioButton, "radioButton_2")

        self.table_player = self.findChild(QTableWidget, "tableWidget")

        self.btn_back = self.findChild(QPushButton, "pushButton")

        self.lbl_tournament_name = self.findChild(QLabel, "label_2")

    # Connecting to actions
        self.rbtn_alphabetic.clicked.connect(self.rbtnChange)
        self.rbtn_rank.clicked.connect(self.rbtnChange)

        self.btn_back.clicked.connect(self.btnBack)

    # List Widget
        self.get_data_player_table()

        self.lbl_tournament_name.setText(self.retrieve_infos[0][0])

    def rbtnChange(self):
        if self.rbtn_alphabetic.isChecked() is True:
            self.slice_r_i = sorted(self.slice_r_i, key=lambda x: x[0])
            self.get_data_player_table()
        else:
            self.slice_r_i = sorted(self.slice_r_i, key=lambda x: x[5], reverse=True)
            self.get_data_player_table()

    def get_data_player_table(self):
        row = 0

        self.tableWidget.setRowCount(8)
        for p in self.slice_r_i:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(p[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(p[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(p[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(p[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(p[4]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(p[5])))
            row += 1

    def btnBack(self):
        self.close()

class Rondes(QMainWindow):
    def __init__(self, value_a):
        super(Rondes, self).__init__()

    # Variables
        infos_tournoi = ReportModel().finishedTournamentNb(value_a+1)

        report_rondes_text = ""

        inc_01 = 1

    # Load the UI file
        uic.loadUi('./views/qt_ux/rondes.ui', self)

    # Define widgets
        self.lbl_name_tournament_rondes = self.findChild(QLabel, "label_2")
        self.lbl_rondes = self.findChild(QPlainTextEdit, "plainTextEdit")

        self.btn_close = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_close.clicked.connect(self.btnClose)

        self.lbl_name_tournament_rondes.setText(infos_tournoi[0][0])

        for i in range(len(infos_tournoi[1])):
            if i % (infos_tournoi[0][4]*2) == 0:
                report_rondes_text = report_rondes_text + f"───────┤ Round {inc_01} ├───────\n"
                inc_01 += 1
            report_rondes_text = report_rondes_text + f"{infos_tournoi[1][i][1]} {infos_tournoi[1][i][0]} avec un score de {infos_tournoi[1][i][5]} \n"

        print("info tournoi : ", report_rondes_text)

        self.lbl_rondes.setPlainText(report_rondes_text)

    def btnClose(self):
        self.close()

class Matchs(QMainWindow):
    def __init__(self, value_a):
        super(Matchs, self).__init__()

    # Variables
        infos_tournoi = ReportModel().finishedTournamentNb(value_a+1)

        report_matchs_text = ""

        inc_01 = 1
        inc_02 = 0

    # Load the UI file
        uic.loadUi('./views/qt_ux/Matchs.ui', self)

    # Define widgets
        self.lbl_name_tournament_rondes = self.findChild(QLabel, "label_2")
        self.lbl_rondes = self.findChild(QPlainTextEdit, "plainTextEdit")

        self.btn_close = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_close.clicked.connect(self.btnClose)

        self.lbl_name_tournament_rondes.setText(infos_tournoi[0][0])

        for i in range(int(len(infos_tournoi[1])/2)):
            if i % (infos_tournoi[0][4]) == 0:
                report_matchs_text = report_matchs_text + f"───────┤ Round {inc_01} ├───────\n"
                inc_01 += 1
            report_matchs_text = report_matchs_text + f"{infos_tournoi[1][inc_02][1]} {infos_tournoi[1][inc_02][0]} VS {infos_tournoi[1][inc_02+1][1]} {infos_tournoi[1][inc_02+1][0]} \n"
            inc_02 += 2

        self.lbl_rondes.setPlainText(report_matchs_text)

    def btnClose(self):
        self.close()
