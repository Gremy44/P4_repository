from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QRadioButton, QLineEdit, QSpinBox, QDateEdit
from PyQt6 import uic
import sys

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
        pass

    def btnQuit(self):
        self.close()

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
        self.wplayer.show()
        self.close()

    def btnBack(self):
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

class PlayerList(QMainWindow):
    def __init__(self):
        super(PlayerList, self).__init__()

        # Load the UI file
        uic.loadUi('./views/qt_ux/player_list.ui', self)

        # Define widgets
        self.btn_back = self.findChild(QPushButton, "back")

        # Connecting to actions
        self.btn_back.clicked.connect(self.btnBack)

    def btnBack(self):
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

# initialize app
if __name__ == '__main__':
    app = QApplication(sys.argv)#instantiate

    main_window = MainWindow()

    sys.exit(app.exec())#execute

