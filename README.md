# OC projet P4 - Chess Swiss Tournament
___
## Table des matières
1. Introduction
2. Lancer le programme
3. Fonctionnement
    - Interface console ou graphique
    - Partie 'Joueur'
    - Partie 'Tournois'
4. Rapport **Flake8**
    - Rapport existant
    - Générer un nouveau rapport

___
### 1. Introduction
Cette application est développée dans le cadre de la formation OpenClassrooms 'Développeur d'application python
Vous trouverez dans le repository, l'application ainsi que les fichiers supplémentaires pour tester et faire fonctionner facilement celle-ci.
Dans le répertoire '*chess data base*' sont stockés des fiches de joueur ainsi que des exemples de matchs déjà disputé pour tester plus vite les fonctionnalités de matchmaking et de génération de rapports des matchs disputés sans avoir à tout recréer au préalable.
Le dossier '*flake-report*' contient le rapport flake8 sur l'application
### 2. Utiliser l'application
- Cloner le git
- Créer votre environnement virtuel
- Installer les librairies grâce au fichier 'requirements.txt'
- Lancer l'application
### 3. Fonctionnement
#### - Interface console ou graphique
Au lancement de l'application, vous avez le choix d'utiliser l'interface console ou une interface graphique pour naviguer dans celle-ci. Les deux interfaces proposent les mêmes fonctionnalités et la même structure.
#### - Partie 'Joueur'
Dans la partie '**Joueur**' vous aurez le choix de :
- Créer un nouveau joueur que vous pourrez utiliser dans les prochains tournois
- Consulter la liste des joueurs déjà présents dans la base de données
- Modifier le rang du joueur souhaité
#### - Partie 'Tournois'
Dans la partie '**Tournois**' vous aurez le choix de :
- Commencer un nouveau tournoi
- Reprendre un tournoi en cour qui aurait été interrompu
- Consulter les rapports des tournois passé
### 4. Rapport Flake8
Le rapport *Flake8* se situe dans le répertoire '*flake-report*' situé à la racine de l'application.
Pour le consulter il vous faudra cliquer sur le fichier index.html présent dans le répertoire.
Pour générer votre propre rapport flake8, vous pouvez entrer la ligne suivante dans la console:
`flake8 --format=html --htmldir=flake-report`
