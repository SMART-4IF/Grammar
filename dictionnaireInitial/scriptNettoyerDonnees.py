# dictionnaire de base: https://github.com/hbenbel/French-Dictionary/tree/master/dictionary

import csv
import json

# extrait et sauvegarde les formes infinitives de la base de données des verbes
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

        # sauvegarde des résultats triés dans un json
        listeVerbes.sort()
        jsonString = json.dumps(listeVerbes)
        jsonFile = open("../dictionnaireUtilisable/verbes.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        # affichage du résultat
        print(f' {len(listeVerbes)} verbes extraits.')

# lancement du nettoyage désiré
nettoyerVerbes()