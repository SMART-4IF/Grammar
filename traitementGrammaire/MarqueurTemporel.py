
import dictionnaireUtilisable

class MarqueurTemporel:

    def __init__(self, texte, tempsConjug):
        self.texte = texte
        self.tempsConjug = tempsConjug

    def __eq__(self, other):
        return self.texte == other.texte and self.tempsConjug == other.tempsConjug

    # Recherche marqueur temporel dans une sequence donnee de mots et init la val de self.texte avec
    # Si marqueur trouve, determine le temps de la phrase
    # phrase : liste de mots dans laquelle il faut trouver le marqueur temporel
    def identifierMarqueurTemporel(self, phrase):
        # recuperation de la liste des marqueurs temporels de la LSF
        marqueursTemporelsLSF = dictionnaireUtilisable.MarqueursTemporels()

        marqueurTrouve = False
        motPrecedent = ""
        for mot in phrase:
            # si mot est dans dictionnaire des marqueurs temporels simbles : c'est un marqueur temporel
            for marqueur in marqueursTemporelsLSF.marqueursSimples:
                if mot == marqueur.mot:
                    self.tempsConjug = marqueur.tempsAssocie
                    if marqueur.isIndispanesable:
                        self.texte = mot
                    phrase.remove(mot)
                    marqueurTrouve = True
                    break

            if marqueurTrouve:
                break

            # si mot precedent + mot est dans dictionnaire des marqueurs temporels doubles : c'est un marqueur temporel
            for marqueur in marqueursTemporelsLSF.marqueursDoubles:
                if motPrecedent != "" and (motPrecedent + " " + mot) == marqueur.mot:
                    self.tempsConjug = marqueur.tempsAssocie
                    self.texte = motPrecedent + " " + mot
                    phrase.remove(motPrecedent)
                    phrase.remove(mot)
                    marqueurTrouve = True
                    break

            if marqueurTrouve:
                break

            motPrecedent = mot

        return phrase