# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json
import dictionnaireUtilisable

class StructurePhrase:

    def __init__(self):
        self.adverbe = ""
        self.sujet = ""
        self.verbe = ""
        self.complement = ""

    def __str__(self):
        return "adverbe : " + self.adverbe + " | sujet : " + self.sujet + " | verbe : " + self.verbe + " | complement : " + self.complement

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
        # si mot est dans dictionnaire des adverbes : c'est un adverbes
        for mot in phrase:
            if mot in dictionnaireAdverbes:
                self.adverbe = mot
                phrase.remove(mot)
                break
        return phrase

    # Recherche sujet dans une sequence donnee de mots et init la val de self.sujet avec
    # phrase : liste de mots dans laquelle il faut trouver le sujet
    def identifierSujet(self, phrase):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()    # ensemble des pronoms de LSF
        # s'il y a un pronom dans la phrase, il devient le sujet
        for mot in phrase:
            if mot in pronomsLSF.personnels:
                # trouver le pronom correspondant
                self.sujet = mot
                phrase.remove(mot)
                break
        return phrase

    # Recherche complement dans une sequence donnee de mots et init la val de self.complement avec
    # phrase : liste de mots dans laquelle il faut trouver le complement
    def identifierComplement(self, phrase):
        # pour l'instant, ce qu'il reste dans la liste de mots devient le complement
        self.complement = phrase[0]
        phrase.remove(phrase[0])
        return phrase