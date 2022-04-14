# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json
import dictionnaireUtilisable

class StructurePhrase:

    def __init__(self, sujet = "", verbe = "être", action = "", marqueurTemporel = "", adverbe = "", tempsConjug = "présent", persConjug = ""):
        self.sujet = sujet
        self.verbe = verbe
        self.action = action
        self.marqueurTemporel = marqueurTemporel
        self.adverbe = adverbe
        self.tempsConjug = tempsConjug
        self.persConjug = persConjug

    def __str__(self):
        phrase = ""

        if self.marqueurTemporel != "": phrase += self.marqueurTemporel
        if self.marqueurTemporel != "" and self.sujet != "": phrase += ", "

        if self.sujet != "": phrase += self.sujet
        if self.sujet != "" and self.verbe != "": phrase += " "

        if self.verbe != "": phrase += self.verbe
        if self.verbe != "" and self.action != "": phrase += " "

        if self.action != "": phrase += self.action
        if self.action != "" and self.adverbe != "": phrase += " "

        if self.adverbe != "": phrase += self.adverbe
        if phrase != "": phrase += "."

        return phrase.capitalize()

    def toStringDebug(self):
        return "marqueurTemporel : " + self.marqueurTemporel + " | sujet : " + self.sujet + " | verbe : " + self.verbe +\
               " | action : " + self.action + " | adverbe : " + self.adverbe + " | temps : " + self.tempsConjug

    def __eq__(self, other):
        return self.marqueurTemporel == other.marqueurTemporel and self.sujet == other.sujet and self.verbe == other.verbe \
               and self.action == other.action and self.adverbe == other.adverbe and self.tempsConjug == other.tempsConjug

    # Recherche verbe dans une sequence donnee de mots et init la val de self.verbe avec
    # phrase : la phrase dans laquelle il faut trouver le verbe
    def identifierVerbe(self, phrase):
        # ouverture du dictionnaire des verbes francais
        with open('dictionnaireUtilisable/verbes.json') as json_data_verbe:
            dictionnaireVerbes = json.load(json_data_verbe)
        # si mot est dans dictionnaire des verbes : c'est un verbe
        for mot in phrase:
            if mot in dictionnaireVerbes:
                self.verbe = mot
                phrase.remove(mot)
                break
        return phrase

    # Recherche adverbe dans une sequence donnee de mots et init la val de self.adverbe avec
    # phrase : liste de mots dans laquelle il faut trouver l'adverbe
    def identifierAdverbe(self, phrase):
        # ouverture du dictionnaire des adverbes francais
        with open('dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
            dictionnaireAdverbes = json.load(json_data_adverbe)
        marqueursTemporelsLSF = dictionnaireUtilisable.MarqueursTemporels()

        # si mot est dans dictionnaire des adverbes : c'est un adverbes
        testMarqueurTemporel = False
        for mot in phrase:
            for marqueur in marqueursTemporelsLSF.liste:
                if mot == marqueur.mot:
                    testMarqueurTemporel = True
                    break

            if testMarqueurTemporel is False and mot in dictionnaireAdverbes:
                self.adverbe = mot
                phrase.remove(mot)
                break

        return phrase

    # Recherche marqueur temporel dans une sequence donnee de mots et init la val de self.marqueurTemporel avec
    # Si marqueur trouve, determine le temps de la phrase
    # phrase : liste de mots dans laquelle il faut trouver le marqueur temporel
    def identifierMarqueurTemporel(self, phrase):
        # recuperation de la liste des marqueurs temporels de la LSF
        marqueursTemporelsLSF = dictionnaireUtilisable.MarqueursTemporels()
        # si mot est dans dictionnaire des adverbes : c'est un adverbes
        for mot in phrase:
            for marqueur in marqueursTemporelsLSF.liste:
                if mot == marqueur.mot:
                    self.tempsConjug = marqueur.tempsAssocie
                    if marqueur.isIndispanesable:
                        self.marqueurTemporel = mot
                    phrase.remove(mot)
                    break
        return phrase

    # Recherche sujet dans une sequence donnee de mots et init la val de self.sujet avec
    # phrase : liste de mots dans laquelle il faut trouver le sujet
    def identifierSujet(self, phrase):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()    # ensemble des pronoms de LSF
        # s'il y a un pronom dans la phrase, il devient le sujet
        i = 0
        tmp = []
        for mot in phrase:
            if mot in pronomsLSF.personnels:
                # trouver le pronom correspondant
                tmp.append(mot)
                i += 1
                #self.sujet = mot
                #phrase.remove(mot)
        if(len(tmp)==2):
            if(tmp[0]==tmp[1]): 
                self.sujet = tmp[0]
                phrase.remove(tmp[0])
                phrase.remove(tmp[1])
            else:
                self.sujet = tmp[1]
                self.complement = tmp[0]
        else:
            self.sujet = tmp[0]
            phrase.remove(tmp[0])

        return phrase

    # Recherche action dans une sequence donnee de mots et init la val de self.action avec
    # phrase : liste de mots dans laquelle il faut trouver le action
    def identifierAction(self, phrase):
        if len(phrase) !=0 : 
            with open('dictionnaireUtilisable/noms.json') as json_data_noms:
                dictionnaireNoms = json.load(json_data_noms)
            pronomsLSF = dictionnaireUtilisable.PronomsLSF()  # ensemble des pronoms de LSF
            # si pronom possessif, mettre pornon + nom suivant dans le action
            testPossessif = False
            listeMotsSupprimer = []

            for mot in phrase:
                if mot in pronomsLSF.possessifs:
                    # trouver le pronom correspondant
                    self.action = mot
                    listeMotsSupprimer.append(mot)
                    testPossessif = True
                elif testPossessif is True and mot in dictionnaireNoms:
                    self.action += " "+mot
                    listeMotsSupprimer.append(mot)
                    break

            for mot in listeMotsSupprimer:
                if mot in phrase:
                    phrase.remove(mot)

            if testPossessif == False:
                # pour l'instant, ce qu'il reste dans la liste de mots devient le action
                self.action = phrase[0]
                phrase.remove(phrase[0])

            return phrase

    # identifie la personne à laquelle il faut conjuguer le verbe
    def identifierPersConjug(self):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()
        pronomsFR = dictionnaireUtilisable.PronomsFR
        if self.sujet in pronomsLSF.personnels:
            self.sujet = self.sujet
        return "ok"