
import json
import dictionnaireUtilisable

class Action:

    def __init__(self, texte, pronom_devant_verbe):
        self.texte = texte
        self.pronom_devant_verbe = pronom_devant_verbe

    def __eq__(self, other):
        return self.texte == other.texte and self.pronom_devant_verbe == other.pronom_devant_verbe


    # Recherche action dans une sequence donnee de mots et init la val de self.texte avec
    # phrase : liste de mots dans laquelle il faut trouver l'action
    def identifierAction(self, phrase):
        if len(phrase) !=0 :
            with open('dictionnaireUtilisable/noms.json') as json_data_noms:
                dictionnaireNoms = json.load(json_data_noms)
            pronomsLSF = dictionnaireUtilisable.PronomsLSF()  # ensemble des pronoms de LSF
            pronomsFR = dictionnaireUtilisable.PronomsFR()
            prepositionsFR = dictionnaireUtilisable.Prepositions()

            # si pronom possessif, mettre pornon + nom suivant dans le action
            testPossessif = False
            testPreposition = False
            listeMotsSupprimer = []

            for mot in phrase:

                # trouver une structure pronom possessif + nom
                for i in range(len(pronomsLSF.possessifs)):
                    if pronomsLSF.possessifs[i] == mot:
                        mot = pronomsFR.possessifsMasculin[i]
                        self.texte = mot
                        listeMotsSupprimer.append(mot)
                        testPossessif = True

                # trouver une structure du type preposition + nom
                for preposition in prepositionsFR.liste:

                    if preposition == mot:
                        self.texte = mot
                        listeMotsSupprimer.append(mot)
                        testPreposition = True

                #elif mot in prepositionsFR.liste:

                if testPossessif or testPreposition:

                    # si on trouve un nom propre
                    if mot[0].isupper():
                        self.texte += " " + mot
                        listeMotsSupprimer.append(mot)
                    else:
                        # si on trouve un nom commun
                        for element in dictionnaireNoms:
                            if mot == element[0] and mot not in listeMotsSupprimer:
                                self.texte += " "+mot
                                listeMotsSupprimer.append(mot)
                                break

            # on supprime les mots mis dans action
            for mot in listeMotsSupprimer:
                if mot in phrase:
                    phrase.remove(mot)

            if testPossessif is False and testPreposition is False:
                # pour l'instant, ce qu'il reste dans la liste de mots devient l'action
                if phrase[0] in pronomsLSF.personnels:
                    index = 0
                    for pronom in pronomsLSF.personnels:
                        if pronom == phrase[0]:
                            self.pronom_devant_verbe = pronomsFR.pronoms_devant_verbe[index]
                        index+=1
                else:
                    for mot in phrase:
                        if self.texte == "":
                            self.texte = mot
                        else:
                            self.texte += " "+mot

            return ""


    # choisir le determinent du complement
    # si le complement possede un nom commun, il faut placer un determinant adapte
    def choisirDeterminantAction(self, sujet, verbe):
        with open('dictionnaireUtilisable/noms.json') as json_data_noms:
            dictionnaireNoms = json.load(json_data_noms)
        pronomsFR = dictionnaireUtilisable.PronomsFR()
        quantificateurs = dictionnaireUtilisable.Pluriel().quantificateurs
        nombres = dictionnaireUtilisable.Pluriel().nombres
        voyelles = ["a", "e", "i", "o", "u", "y"]

        # test si mot dans quantificateur
        testQuantifacteur = False
        if self.texte != "":
            for mot in self.texte.split():
                if mot in quantificateurs or mot in nombres:
                    testQuantifacteur = True
                    break

        # si on est dans une phrase avec pronom personnel + etre ou phrase d'un seul mot ou phrase avec quantificateur: pas de determinant
        if (sujet.texte in pronomsFR.personnels and verbe.texte == "être") is False and (
                sujet.texte == "" and verbe == "") is False \
                and testQuantifacteur is False:

            for mot in self.texte.split():

                # s'il y a un pronom possessif, pas besoin de determinant
                if mot in pronomsFR.possessifsMasculin or mot in pronomsFR.possessifsFeminin or mot in pronomsFR.possessifsPluriel:
                    break

                for element in dictionnaireNoms:
                    if mot == element[0]:
                        if element[1] == "m" and verbe.texte == "aller" and element[0] in voyelles:
                            self.texte = "à l'" + self.texte
                        elif element[1] == "m" and verbe.texte == "aller" and element[0] not in voyelles:
                            self.texte = "au " + self.texte
                        elif element[1] == "f" and verbe.texte == "aller":
                            self.texte = "à la " + self.texte
                        elif element[1] == "f":
                            self.texte = "une " + self.texte
                        else:
                            self.texte = "un " + self.texte


    # accorder l'action en nombre
    def accorderAction(self):

        with open('dictionnaireUtilisable/noms.json') as json_data_noms:
            dictionnaireNoms = json.load(json_data_noms)
        pluriel = dictionnaireUtilisable.Pluriel()

        plurielNecessaire = False
        for mot in self.texte.split():
            # on accorder le nom suivant
            if mot in pluriel.quantificateurs or mot in pluriel.nombres:
                plurielNecessaire = True

            if plurielNecessaire:

                for element in dictionnaireNoms:
                    if element[0] == mot and mot not in pluriel.irreguliersPluriels:
                        self.texte = self.texte.replace(mot, mot + "s")
                    elif element[0] == mot and mot in pluriel.irreguliersPluriels:
                        self.texte = self.texte.replace(mot, mot + "x")