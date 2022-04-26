
import json
import dictionnaireUtilisable

class Adverbe:

    def __init__(self, texte):
        self.texte = texte

    def __eq__(self, other):
        return self.texte == other.texte

    # Recherche adverbe dans une sequence donnee de mots et init la val de self.texte avec
    # IMPORATNT ! Doit etre appele après identifierMarqueurTemporel     TODO
    # phrase : liste de mots dans laquelle il faut trouver l'adverbe
    def identifierAdverbe(self, phrase):
        # ouverture du dictionnaire des adverbes francais
        with open('dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
            dictionnaireAdverbes = json.load(json_data_adverbe)
        prepositionsFR = dictionnaireUtilisable.Prepositions()

        # si mot est dans dictionnaire des adverbes : c'est un adverbes
        for mot in phrase:
            if mot in dictionnaireAdverbes and mot not in prepositionsFR.liste:
                self.texte = mot
                phrase.remove(mot)
                break

        return phrase