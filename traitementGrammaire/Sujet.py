
import dictionnaireUtilisable

class Sujet:

    def __init__(self, texte, persConjug):
        self.texte = texte                      # texte du sujet
        self.persConjug = persConjug            # le sujet determine la personne à laquelle on conjugue le verbe

    def __eq__(self, other):
        return self.texte == other.texte and self.persConjug == other.persConjug


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

        if len(tmp)==2:
            if(tmp[0]==tmp[1]): 
                self.texte = tmp[0]
                phrase.remove(tmp[0])
                phrase.remove(tmp[1])
            else:
                self.texte = tmp[1]
                self.complement = tmp[0]
        elif len(tmp)==1:
            self.texte = tmp[0]
            phrase.remove(tmp[0])

        return phrase


    # identifie la personne a laquelle il faut conjuguer le verbe
    def identifierPersConjug(self):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()
        pronomsFR = dictionnaireUtilisable.PronomsFR()
        index = 0
        for pronom in pronomsLSF.personnels:
            if pronom == self.texte:
                self.texte = pronomsFR.personnels[index]
                self.persConjug = index +1
            index+=1