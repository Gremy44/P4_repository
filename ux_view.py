from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QRadioButton, QLineEdit, QSpinBox, QDateEdit, QListView
from PyQt6 import uic, QtWidgets
from xml.etree import ElementTree as et
import sys
from models.tournament_model_write import ModelRetrieveTournament


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

    def modifyXml(self):
        """
        Modifie les valeurs des fichiers xml pour les adapter dans l'interface
        """
        filename = "./views/qt_ux/players.ui"
        xmlTree = et.parse(filename)
        rootElement = xmlTree.getroot()
        #chemin dans le xml
        for element in rootElement.findall("widget/widget/layout/item/layout/item/widget/property"):
            #cherche le therme 'joueurs'
            if element.findtext('string') == 'Joueurs' :
                #Change the element
                element.find('string').text = "Joueuses"
        #Write the modified xml file.        
        xmlTree.write(filename,encoding='UTF-8',xml_declaration=True)
        
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
        print(self.send_add_player_infos())
        self.wplayer.show()
        self.close()

    def btnBack(self):
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

    def send_add_player_infos(self):
        """
        - Retourne les infos rentrées dans "ajouté joueur"
        - Format : tupple
        """
        self.gender = ""

        if self.rbtn_gender_h.isChecked() == True:
            self.gender = "Homme"
        elif self.rbtn_gender_f.isChecked() == True:
            self.gender = "Femme"
        else:
            self.gender = "Neutre"

        return(self.line_l_name.text(), 
               self.line_f_name.text(),
               self.date_bday.text(),
               self.gender,
               self.sb_rank.text()
               )

class PlayerList(QMainWindow):
    def __init__(self):
        super(PlayerList, self).__init__()

        self.myplayersobj = ModelRetrieveTournament()

        # Load the UI file
        uic.loadUi('./views/qt_ux/player_list.ui', self)

        # Define widgets
        self.btn_back = self.findChild(QPushButton, "back")
        self.list_db = self.findChild(QListView, "listplayers")

        # Connecting to actions
        self.btn_back.clicked.connect(self.btnBack)
        
        # List Widget
        #self.get_data()

    def get_data(self):
        model = self.myplayersobj.retrieve_all_player_from_db()
        for index in range(model.rowCount()):
            # item = model.data(index)
            item = model.data(index, 1, Qt.DisplayRole)
            print(item)
        
        

    def btnBack(self):
        self.wplayer = PlayersWindow()
        self.wplayer.show()
        self.close()

# initialize app
if __name__ == '__main__':
    app = QApplication(sys.argv)#instantiate

    main_window = MainWindow()

    sys.exit(app.exec())#execute

