class players():
    def __init__(self, l_name, f_name, b_day, gender, ranking):
        self.l_name = l_name
        self.f_name = f_name
        self.b_day = b_day
        self.gender = gender
        self.ranking = ranking

        l_name = input("Entrez le nom de famille du joueur : ")
        f_name = input("Entrez le prénom du joueur : ")
        b_day = input("Entrez la date de naissance du joueur : ")
        gender = input("Entrez le genre (H/F/N) : ")
        ranking = input("Entrez le classement du joueur : ")