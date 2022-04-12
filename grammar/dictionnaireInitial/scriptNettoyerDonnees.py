# dictionnaire de base: https://github.com/hbenbel/French-Dictionary/tree/master/dictionary

import csv
import json

# extrait et sauvegarde les formes infinitives de la base de donnees des verbes
def nettoyerVerbes():

    # ouverture du csv
    with open('verb.csv') as csv_verbes:

       # initialisation des variables
        csv_reader = csv.reader(csv_verbes, delimiter=',')
        listeVerbes = []

        # parcourt tout le csv pour trouver les formes infinitives des verbes
        for row in csv_reader:
            if "'infinitive'" in row[2]:
                listeVerbes.append(row[1])

        # sauvegarde des resultats tries dans un json
        listeVerbes.sort()
        jsonString = json.dumps(listeVerbes)
        jsonFile = open("../dictionnaireUtilisable/verbes.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du resultat
        print(f' {len(listeVerbes)} verbes extraits.')


# extrait et sauvegarde les noms en supprimant ceux avec des espaces et les formes non nominales (feminin, pluriel)
def nettoyerNoms():

    # ouverture du csv
    with open('noun.csv') as csv_noms:

       # initialisation des variables
        csv_reader = csv.reader(csv_noms, delimiter=',')
        listeNoms = []
        listeNomsASupprimer = []

        for row in csv_reader:
            # recuperation de tous les noms qui ne possedent pas d'espaces, qui ne sont pas tagues et dont la taille est superieure a 1 caractere
            if " " not in row[1] and 'plural' not in row[2] and 'feminine' not in row[2] and len(row[1]) > 1:
                listeNoms.append(row[1])
            # recuperation de tous les noms tagues
            if " " not in row[1] and ('plural' in row[2] or 'feminine' in row[2]) and len(row[1]) > 1:
                listeNomsASupprimer.append(row[1])

        # soustraction des mots tagues au jeu de donnees a conserver pour garder que les formes sg, et masculin
        for nom in listeNomsASupprimer:
            if nom in listeNoms:
                listeNoms.remove(nom)

        # sauvegarde des resultats tries dans un json
        listeNoms.sort()
        jsonString = json.dumps(listeNoms)
        jsonFile = open("../dictionnaireUtilisable/noms.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du resultat
        print(f' {len(listeNoms)} noms extraits.')


# extrait et sauvegarde les adverbes
def nettoyerAdverbes():

    # ouverture du csv
    with open('adv.csv') as csv_adv:

       # initialisation des variables
        csv_reader = csv.reader(csv_adv, delimiter=',')
        listeAdv = []

        # parcourt tout le csv pour trouver les adverbes
        for row in csv_reader:
            if " " not in row[1]:
                listeAdv.append(row[1])

        # sauvegarde des resultats tries dans un json
        listeAdv.sort()
        jsonString = json.dumps(listeAdv)
        jsonFile = open("../dictionnaireUtilisable/adverbes.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du resultat
        print(f' {len(listeAdv)} adverbes extraits.')


# extrait et sauvegarde les adjectifs en supprimant ceux avec des espaces et les formes non nominales (feminin, pluriel)
def nettoyerAdjectifs():

    # ouverture du csv
    with open('adj.csv') as csv_adj:

       # initialisation des variables
        csv_reader = csv.reader(csv_adj, delimiter=',')
        listeAdj = []
        listeAdjASupprimer = []

        for row in csv_reader:
            # recuperation de tous les noms qui ne possedent pas d'espaces, qui ne sont pas tagues et dont la taille est superieure a 1 caractere
            if " " not in row[1] and 'plural' not in row[2] and 'feminine' not in row[2] and len(row[1]) > 1:
                listeAdj.append(row[1])
            # recuperation de tous les noms tagues
            if " " not in row[1] and ('plural' in row[2] or 'feminine' in row[2]) and len(row[1]) > 1:
                listeAdjASupprimer.append(row[1])

        # soustraction des mots tagues au jeu de donnees a conserver pour garder que les formes sg, et masculin
        for nom in listeAdjASupprimer:
            if nom in listeAdj:
                listeAdj.remove(nom)

        # sauvegarde des resultats tries dans un json
        listeAdj.sort()
        jsonString = json.dumps(listeAdj)
        jsonFile = open("../dictionnaireUtilisable/adjectifs.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du resultat
        print(f' {len(listeAdj)} adjectifs extraits.')

# lancement du nettoyage desire
nettoyerAdverbes()