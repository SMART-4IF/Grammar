
import streamApp.Grammar.dictionnaireUtilisable as dictionnaireUtilisable

class MarqueursNegation:

    def __init__(self, marqueur1, marqueur2):
        self.marqueur1 = marqueur1
        self.marqueur2 = marqueur2

    def __eq__(self, other):
        return self.marqueur1 == other.marqueur1 and self.marqueur2 == other.marqueur2

    # identifie les marqueurs de negation
    def identifierMarqueursNegation(self, phrase):

        listeMarqueursNegation = dictionnaireUtilisable.MarqueursNegation()

        for mot in phrase:

            if mot in listeMarqueursNegation.simple:
                self.marqueur2 = mot
                phrase.remove(mot)
            if mot in listeMarqueursNegation.double:
                self.marqueur2 = "pas"
                phrase.remove(mot)

        if self.marqueur2 != "":
            self.marqueur1 = "ne"

        return phrase