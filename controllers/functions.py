import os
import random
import numpy as np

# Function for simple directory creation
# path => relative path of the futur directory
def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

def ask_informations_tournament():
    name = input("Nom du tournois : ")
    place = input("Lieu du tounois : ")
    date = input("Date de début et de fin du tournois(jj/mm/aaaa-jj/mm/aaaa) : ")
    nb_round = input("Nombre de tours : ")
    rondes = input("Rondes : ")
    player = input("Nombre joueurs : ")
    time = input("Coups rapides, blitz ou bullet(1/2/3) : ")
    description = input("Description : ")

    return name,place,date,nb_round,rondes,player,time,description

def ask_informations_player():
    l_name = input("Entrez le nom de famille du joueur : ")
    f_name = input("Entrez le prénom du joueur : ")
    b_day = input("Entrez la date de naissance du joueur (jj/mm/aaaa): ")
    gender = input("Entrez le genre (H/F/N) : ")
    ranking = input("Entrez le classement du joueur : ")

    return l_name, f_name, b_day, gender, ranking

def pairing(nb_player):
    nb_list = []
    for i in range(nb_player):
        nb_list.append(i+1)
    random.shuffle(nb_list)

    return nb_list
    


