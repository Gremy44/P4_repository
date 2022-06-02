def ask_informations_tournois():
    name = input("Nom du tournois : ")
    place = input("Lieu du tounois : ")
    date = input("Date de début et de fin du tournois(jj/mm/aaaa-jj/mm/aaaa) : ")
    nb_round = input("Nombre de tours : ")
    rondes = input("Rondes : ")
    player = input("Nombre joueurs : ")
    time = input("Coups rapides, blitz ou bullet(1/2/3) : ")
    description = input("Description : ")

    return name,place,date,nb_round,rondes,player,time,description
