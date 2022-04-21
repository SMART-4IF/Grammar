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

        # dans les données, il y a des mots qui ne sont pas des verbes. Il faut les identifier et les retirer
        listeFauxVerbes = ["hier"]
        for nom in listeFauxVerbes:
            if nom in listeVerbes:
                listeVerbes.remove(nom)

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
        listeNomsOfficielle = []

        for row in csv_reader:
            # recuperation de tous les noms qui ne possedent pas d'espaces, qui ne sont pas tagues et dont la taille est superieure a 1 caractere
            if " " not in row[1] and len(row[1]) > 1:
                attribut = "m"
                if row[1][0].isupper():
                    attribut = "np"
                elif "plural" in row[2] or row[1].endswith('s') or row[1].endswith('x'):
                    attribut = "pl"
                elif "feminine" in row[2] or row[1].endswith('tion') or row[1].endswith('ance') or row[1].endswith('ade')\
                        or row[1].endswith('ence') or row[1].endswith('esse') or row[1].endswith('ette')\
                        or row[1].endswith('euse') or row[1].endswith('té') or row[1].endswith('ude')\
                        or row[1].endswith('ée') or row[1].endswith('ie') or row[1].endswith('ine')\
                        or row[1].endswith('sion') or row[1].endswith('ure') or row[1].endswith('ance')\
                        or row[1].endswith('ite'):
                    attribut = "f"

                nom = [row[1], attribut]

                if nom not in listeNoms:
                    listeNoms.append(nom)

        for element in listeNoms:
            if element[1] != "pl" and element[1] != "np":
                listeNomsOfficielle.append(element)

        # sauvegarde des resultats tries dans un json
        listeNomsOfficielle.sort()
        jsonString = json.dumps(listeNomsOfficielle)
        jsonFile = open("../dictionnaireUtilisable/noms.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du resultat
        print(f' {len(listeNomsOfficielle)} noms extraits.')


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
nettoyerNoms()