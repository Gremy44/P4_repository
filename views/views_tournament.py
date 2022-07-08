from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QRadioButton, QLineEdit, QSpinBox, QDateEdit, QListView, QTextEdit, QLabel, QTableWidget, QTabWidget, QWidget, QVBoxLayout
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import QSize, Qt
from xml.etree import ElementTree as et
from models.tournament_model_write import AddPlayerModel, ModelRetrieveTournament, ModelWriteTournament
import sys

# --------------
# ----- CL -----
# --------------

class AddPlayerViews:
    def __init__(self, l_name = "", f_name = "", b_day = "", gender = "", rank = 0.0):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.rank = rank
        self.score = 0.0

    def ask_player_infos(self):
        self.l_name = input("Entrez nom : ")
        self.f_name = input("Entrez prénom : ")
        self.b_day = input("Date d'anniversaire : ")
        self.gender = input("Genre : ")
        self.rank = input("Rang : ")
        return self.l_name, self.f_name, self.b_day, self.gender, self.rank, self.score

class ViewsTournament:
    def __init__(self):
        self.complete_result = []
        self.id_round_views = ModelRetrieveTournament().id_round

    def ask_tounament_infos(self):
        self.t_name    = input("Entrez nom : ")
        self.t_place   = input("Entrez lieu : ")
        self.t_date    = input("Entrez date : ")
        self.t_round   = 4
        self.t_rondes  = input("Entrez instances rondes : ")
        self.t_players = [3042972155808, 2520259116960, 2835596394400, 2498757410720,
                          2123311234976, 1988607754144, 1384106246048, 2187293245344]
        self.t_time    = input("Bullet/Blitz/coup rapide : ")
        self.t_desc    = input("Entrez description : ")

        return self.t_name, self.t_place, self.t_date, self.t_round, self.t_rondes, self.t_players, self.t_time, self.t_desc

    def views_round_input(self, sorted_paires, ronde):
        '''
        - input pour les resulats de chaque round
        '''
        print("round : ", ronde)
        for i in range(len(sorted_paires)):
            print("Ronde", ronde,":",
                  sorted_paires[i][0]['Nom'],
                  sorted_paires[i][0]['Prenom'], "contre",
                  sorted_paires[i][1]['Nom'],
                  sorted_paires[i][1]['Prenom'])
            score_p1 = input(f"Score joueur {sorted_paires[i][0]['Nom']} {sorted_paires[i][0]['Prenom']}: ")
            score_p2 = input(f"Score joueur {sorted_paires[i][1]['Nom']} {sorted_paires[i][1]['Prenom']}: ")
            sorted_paires[i][0]['Score'] = sorted_paires[i][0]['Score'] + float(score_p1)
            sorted_paires[i][1]['Score'] = sorted_paires[i][1]['Score'] + float(score_p2)

        return sorted_paires 

    def results(self):
        tournoi = ModelRetrieveTournament().retrieve_tournament()
        inc_score = 1
        print("--- Tournoi terminé ---")
        print("Informations sur le tournoi :")
        print()
        print("Résultats du tournois :")
        score_final = ModelRetrieveTournament().sorted_players()
        for i in score_final : 
            print(f"{inc_score} -  {i['Nom']} {i['Prenom']} au rang {i['Rang']} avec un score de {i['Score']}")
            inc_score += 1
        tournoi = ModelRetrieveTournament().retrieve_tournament()

# --------------
# ----- UX -----
# --------------

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

        #Show the app
        self.show()

    def btnPlayers(self):
        self.wplayers = PlayersWindow()
        self.wplayers.show()
        self.close()

    def btnTournaments(self):
        self.wplayers = Tournament()
        self.wplayers.show()
        self.close()

    def btnQuit(self):
        self.close()
        
    @staticmethod
    def goGui():
        app = QApplication(sys.argv)#instantiate

        main_window = MainWindow()

        sys.exit(app.exec())#execute

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
        self.aplayer = AddPlayers()
        self.aplayer.show()
        self.close()

    def btnSeePlayers(self):
        self.mw = PlayerList()
        self.mw.show()
        self.close()

    def btnBack(self):
        self.mw = MainWindow()
        self.mw.show()
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
        self.wplayer = PlayersWindow()
        self.send_add_player_infos()
        self.wplayer.show()
        self.close()

    def btnBack(self):
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

    def send_add_player_infos(self):
        """
        Ajoute un joueur dans la DB depuis la GUI
        """

        if self.rbtn_gender_h.isChecked() == True:
            self.gender = "H"
        elif self.rbtn_gender_f.isChecked() == True:
            self.gender = "F"
        else:
            self.gender = "N"

        AddPlayerModel().player_db_reg(
            self.line_l_name.text(), 
            self.line_f_name.text(),
            self.date_bday.text(),
            self.gender,
            self.sb_rank.text()
            )

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
        players = ModelRetrieveTournament().retrieve_all_player_from_db() 
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
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

class Tournament(QMainWindow):
    def __init__(self):
        super(Tournament,self).__init__()

        # Load the UI file
        uic.loadUi('./views/qt_ux/tournament.ui', self)

        # Define widgets
        self.btn_new_tournament = self.findChild(QPushButton, "new_tournament")
        self.btn_resume_tournament = self.findChild(QPushButton, "resume_tournament")
        self.btn_back = self.findChild(QPushButton, "back")

        # Connecting to actions
        self.btn_new_tournament.clicked.connect(self.btnNewT)
        self.btn_resume_tournament.clicked.connect(self.btnResumeT)
        self.btn_back.clicked.connect(self.btnBack)

    def btnNewT(self):
        self.wplayer = NewTournament()
        self.wplayer.show()
        self.close()

    def btnResumeT(self):
        pass

    def btnBack(self):
        self.wplayer = MainWindow()
        self.wplayer.show()
        self.close()

class NewTournament(QMainWindow):
    def __init__(self):
        super(NewTournament,self).__init__()

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

        # Connecting to actions
        self.btn_players.clicked.connect(self.btnSelPlayers)
        self.btn_validation.clicked.connect(self.btnValidation)
        self.btn_back.clicked.connect(self.btnBack)

    def btnSelPlayers(self):
        self.lplayer = PlayerListSel()
        self.lplayer.show()

    def btnValidation(self):
        id_players = self.player_to_db(self.lplayer.my_players)

        if self.rbtn_blitz.isChecked() == True:
            self.time = "Blitz"
        elif self.rbtn_bullet.isChecked() == True:
            self.time = "Bullet"
        else:
            self.time = "Coup rapide"

        tournoi_infos = ModelWriteTournament(self.line_t_name.text(),
                                      self.line_t_place.text(),
                                      self.date_t_begin.text(),
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
        self.wplayer = Tournament()
        self.wplayer.show()
        self.close()

   
    def player_to_db(self, players_lst_from_gui:dict):
        """
        Retourne les 'id_player' des joueurs selectionnés
        """
        id_player = []
    
        all_players = ModelRetrieveTournament().retrieve_all_player_from_db()

        for i,n in zip(players_lst_from_gui.items(), all_players):
            if i[1] == True:
                id_player.append(n['id_player'])

        return id_player
        

        

class PlayerListSel(QMainWindow):
    def __init__(self):
        super(PlayerListSel, self).__init__()

        #variables
        self.players = ModelRetrieveTournament().retrieve_all_player_from_db()

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

        #sel_table = QTableWidget()
        self.list_db.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected, deselected):
        a = None
        b = None
        self.element_true = 0        

        for ix in selected.indexes():
            a = ix.row()

        for ix in deselected.indexes():
            b = ix.row()

        #print(a, b)

        self.my_players[a]=True
        self.my_players[b]=False

        del self.my_players[None]#supprime la dernière clé qui est un none

        # retourn le nb d'éléments selectionnés
        for i in self.my_players:
            if self.my_players[i] is True:
                self.element_true +=1

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
        super(Begin,self).__init__()

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

    
class Round(QMainWindow):
    def __init__(self):
        super(Round,self).__init__()

        # Variables
        self.rondes = ModelRetrieveTournament().retrieve_tournament()[2]["Rondes"]

        # Load the UI file
        uic.loadUi('./views/qt_ux/round.ui', self)

        # Define widgets
        self.tab_match = self.findChild(QWidget, "tab_7")
        self.tab_match_i = self.findChild(QTabWidget, "tabWidget")
        self.lbl_player_1 = self.findChild(QLabel, "label_3")
        self.lbl_player_2 = self.findChild(QLabel, "label_4")
        self.s_p_1 = self.findChild(QSpinBox, "doubleSpinBox")
        self.s_p_2 = self.findChild(QSpinBox, "doubleSpinBox_2")
        self.btn_validate_round = self.findChild(QPushButton, "pushButton")

        # Connecting to actions
        self.btn_validate_round.clicked.connect(self.btnValidateRound)

        for i in range(self.rondes-1):
            print(i)
            self.tab_match_i.addTab(QWidget(), f"Match {i+2}")

    def btnValidateRound(self):
        pass

class QWRound(QMainWindow):
    def __init__(self):
        super(QWRound,self).__init__()

    # Load the UI file
        uic.loadUi('./views/qt_ux/mw_qw_round.ui', self)

    # Define widgets
        self.lbl_player_1 = self.findChild(QLabel, "label_3")
        self.lbl_player_2 = self.findChild(QLabel, "label_4")
        self.s_p_1 = self.findChild(QSpinBox, "doubleSpinBox_3")
        self.s_p_2 = self.findChild(QSpinBox, "doubleSpinBox_4")
        self.btn_validate_round = self.findChild(QPushButton, "pushButton")

    # Connecting to actions
        self.btn_validate_round.clicked.connect(self.btnValidateRound)


class QWRoundEmpty(QMainWindow):
    def __init__(self):
        super(QWRoundEmpty,self).__init__()

    # Variables
        self.rondes = ModelRetrieveTournament().retrieve_tournament()[2]["Rondes"]

    # Load the UI file
        uic.loadUi('./views/qt_ux/round_empty.ui', self)

    # Define Widgets
        self.tab_match = self.findChild(QTabWidget, "tabWidget")

        for i in range(self.rondes):
                print(i)
                self.tab_match.addTab(QWRound(), f"Match {i+1}")
                QWRound().lbl_player_1.setText(f"{self.element_true} éléments sélectionnés sur 8")