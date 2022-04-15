# hier cinéma aller moi 
# hier je suis allé au cinéma 
from contextlib import nullcontext
import json
import dictionnaireUtilisable
from verbecc import Conjugator

class StructurePhrase:

    def __init__(self, sujet = "", pronom_devant_verbe = "", verbe = "être", action = "", marqueurTemporel = "", adverbe = "", tempsConjug = "présent",
                 persConjug = 1, marqueurNegation1 = "", marqueurNegation2 = ""):
        self.sujet = sujet
        self.pronom_devant_verbe = pronom_devant_verbe
        self.verbe = verbe
        self.action = action
        self.marqueurTemporel = marqueurTemporel
        self.adverbe = adverbe
        self.tempsConjug = tempsConjug
        self.persConjug = persConjug
        self.marqueurNegation1 = marqueurNegation1
        self.marqueurNegation2 = marqueurNegation2

    def __str__(self):
        phrase = ""

        if self.marqueurTemporel != "": phrase += self.marqueurTemporel
        if self.marqueurTemporel != "" and self.sujet != "": phrase += ","

        if self.sujet != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.sujet

        if self.pronom_devant_verbe != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.pronom_devant_verbe

        if self.verbe != "":
            if len(phrase) > 1 and "'" not in self.sujet:
                phrase += " "
            phrase += self.verbe

        if self.action != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.action

        if self.adverbe != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.adverbe

        if phrase != "": phrase += "."

        return phrase.capitalize()

    def toStringDebug(self):
        return "marqueurTemporel : " + self.marqueurTemporel + " | sujet : " + self.sujet + " | verbe : " + self.verbe +\
               " | action : " + self.action + " | adverbe : " + self.adverbe + " | temps : " + self.tempsConjug + \
               " | pers conjug: " + str(self.persConjug)

    def __eq__(self, other):
        return self.sujet == other.sujet and self.pronom_devant_verbe == other.pronom_devant_verbe and self.verbe == other.verbe \
               and self.action == other.action and self.marqueurTemporel == other.marqueurTemporel and self.adverbe == other.adverbe and self.tempsConjug == other.tempsConjug and \
               self.persConjug == other.persConjug

    # execute l'ensemble du process de traduction
    def traduire(self, phraseInitiale):
        phraseInitiale = self.identifierVerbe(phraseInitiale)
        phraseInitiale = self.identifierMarqueurTemporel(phraseInitiale)
        phraseInitiale = self.identifierAdverbe(phraseInitiale)
        phraseInitiale = self.identifierSujet(phraseInitiale)
        phraseInitiale = self.identifierAction(phraseInitiale)
        self.identifierPersConjug()
        self.conjuguerVerbe()
        return self

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


    # identifie les marqueurs de negation
    def identifierMarqueursNegation(self, phrase):
        marqueursNegation = dictionnaireUtilisable.MarqueursNegation()

        for mot in phrase:
            if mot in marqueursNegation.simple:
                self.marqueurNegation1 = "ne"
                self.marqueurNegation2 = mot
                phrase.remove(mot)
            if mot in marqueursNegation.double:
                self.marqueurNegation1 = "ne"
                self.marqueurNegation2 = "pas"
                phrase.remove(mot)

    # Recherche action dans une sequence donnee de mots et init la val de self.action avec
    # phrase : liste de mots dans laquelle il faut trouver le action
    def identifierAction(self, phrase):
        if len(phrase) !=0 : 
            with open('dictionnaireUtilisable/noms.json') as json_data_noms:
                dictionnaireNoms = json.load(json_data_noms)
            pronomsLSF = dictionnaireUtilisable.PronomsLSF()  # ensemble des pronoms de LSF
            pronomsFR = dictionnaireUtilisable.PronomsFR()
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
                if phrase[0] in pronomsLSF.personnels:
                    index = 0
                    for pronom in pronomsLSF.personnels:
                        if pronom == phrase[0]:
                            self.pronom_devant_verbe = pronomsFR.pronoms_devant_verbe[index]
                        index+=1
                else : 
                    self.action = phrase[0]
                phrase.remove(phrase[0])

            return phrase

    # identifie la personne à laquelle il faut conjuguer le verbe
    def identifierPersConjug(self):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()
        pronomsFR = dictionnaireUtilisable.PronomsFR()
        index = 0
        for pronom in pronomsLSF.personnels:
            if pronom == self.sujet:
                self.sujet = pronomsFR.personnels[index]
                self.persConjug = index +1
            index+=1

    # conjugue le verbe selon le temps et la personne identifies
    def conjuguerVerbe(self):
        cg = Conjugator(lang='fr')
        conjugaisonsDuVerbe = cg.conjugate(self.verbe)
        verbeConjugue = conjugaisonsDuVerbe['moods']['indicatif'][self.tempsConjug][self.persConjug-1]

        # si pronom j', le split ne marche pas.
        if "'" in verbeConjugue:
            if self.sujet == "je":
                self.sujet = "j'"
            self.verbe = verbeConjugue[2:]
        else:
            verbeConjugue = verbeConjugue.split()
            verbeConjugue = verbeConjugue[1:]
            self.verbe = " ".join(verbeConjugue)


    # Recherche complement dans une sequence donnee de mots et init la val de self.complement avec
    # phrase : liste de mots dans laquelle il faut trouver le complement
    def identifierComplement(self, phrase):
        # pour l'instant, ce qu'il reste dans la liste de mots devient le complement
        if len(phrase) != 0:
            self.complement = phrase[0]
            phrase.remove(phrase[0])
            return phrase
