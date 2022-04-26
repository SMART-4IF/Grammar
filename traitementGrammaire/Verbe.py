
import json
from verbecc import Conjugator

class Verbe:

    def __init__(self, texte):
        self.texte = texte

    def __eq__(self, other):
        return self.texte == other.texte

    # Recherche verbe dans une sequence donnee de mots et init la val de self.texte avec
    # phrase : la phrase dans laquelle il faut trouver le verbe
    def identifierVerbe(self, phrase):
        # ouverture du dictionnaire des verbes francais
        with open('dictionnaireUtilisable/verbes.json') as json_data_verbe:
            dictionnaireVerbes = json.load(json_data_verbe)
        # si mot est dans dictionnaire des verbes : c'est un verbe
        for mot in phrase:
            if mot in dictionnaireVerbes:
                self.texte = mot
                phrase.remove(mot)
                break
        return phrase

    # conjugue le verbe selon le temps et la personne identifies
    def conjuguerVerbe(self, tempsConjug, sujet, pronom_devant_verbe):
        if self.texte != "":
            cg = Conjugator(lang='fr')
            conjugaisonsDuVerbe = cg.conjugate(self.texte)
            verbeConjugue = conjugaisonsDuVerbe['moods']['indicatif'][tempsConjug][sujet.persConjug - 1]

            # si pronom j', le split ne marche pas.
            if "'" in verbeConjugue:
                if pronom_devant_verbe == "":
                    if sujet.texte == "je":
                        sujet.texte = "j'"
                self.texte = verbeConjugue[2:]
            else:
                verbeConjugue = verbeConjugue.split()
                verbeConjugue = verbeConjugue[1:]
                self.texte = " ".join(verbeConjugue)