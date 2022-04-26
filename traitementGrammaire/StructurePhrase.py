
import json
from . import Sujet
from . import Verbe
from . import Adverbe
from . import MarqueurTemporel
from . import MarqueursNegation
from . import Action
import dictionnaireUtilisable

class StructurePhrase:

    def __init__(self, sujet = "", pronom_devant_verbe = "", verbe = "", action = "", marqueurTemporel = "", adverbe = "", persConj = 1, tempsConjug = "présent", marqueurNegation1 = "", marqueurNegation2 = ""):
        self.sujet = Sujet.Sujet(sujet, persConj)
        self.verbe = Verbe.Verbe(verbe)
        self.action = Action.Action(action, pronom_devant_verbe)
        self.marqueurTemporel = MarqueurTemporel.MarqueurTemporel(marqueurTemporel, tempsConjug)
        self.adverbe = Adverbe.Adverbe(adverbe)
        self.marqueursNegation = MarqueursNegation.MarqueursNegation(marqueurNegation1, marqueurNegation2)


    def __str__(self):

        phraseSplitee = []

        if self.marqueurTemporel.texte != "":
            phraseSplitee.append(self.marqueurTemporel.texte+',')

        if self.sujet.texte != "":
            for mot in self.sujet.texte.split():
                phraseSplitee.append(mot)

        if self.marqueursNegation.marqueur1 != "":
            phraseSplitee.append(self.marqueursNegation.marqueur1)

        if self.action.pronom_devant_verbe != "":
            phraseSplitee.append(self.action.pronom_devant_verbe)

        if self.verbe.texte != "":
            for mot in self.verbe.texte.split():
                phraseSplitee.append(mot)

        if self.marqueursNegation.marqueur2 != "":
            phraseSplitee.append(self.marqueursNegation.marqueur2)

        if self.action.texte != "":
            for mot in self.action.texte.split():
                phraseSplitee.append(mot)

        if self.adverbe.texte != "":
            phraseSplitee.append(self.adverbe.texte)

        # ajout des elisions
        phrase = self.ajoutAppostrophes(phraseSplitee)

        # choix de la ponctuation adaptee
        phrase += self.determinerPonctuation(phrase)

        # on retire les - des mots composes
        phrase = self.nettoyerTirets(phrase)

        return phrase[0].upper() + phrase[1:]

    # permet d'afficher le detail de toutes les infos
    def toStringDebug(self):
        return "marqueurTemporel : " + self.marqueurTemporel.texte + " | sujet : " + self.sujet.texte + \
               " | marqueur neg 1 : " + self.marqueursNegation.marqueur1 + " | pronom devant verbe : " + self.action.pronom_devant_verbe + \
               " | verbe : " + self.verbe.texte + " | marqueur neg 2 : " + self.marqueursNegation.marqueur2 + \
               " | action : " + self.action.texte + " | adverbe : " + self.adverbe.texte + " | temps : " + self.marqueurTemporel.tempsConjug + \
               " | pers conjug: " + str(self.sujet.persConjug)

    def __eq__(self, other):
        return self.marqueurTemporel == other.marqueurTemporel and self.sujet == other.sujet and \
               self.marqueursNegation == other.marqueursNegation and \
               self.verbe == other.verbe and self.action == other.action and self.adverbe == other.adverbe

    # execute l'ensemble du process de traduction
    def traduire(self, phraseInitiale):

        longueurPhrase = len(phraseInitiale)

        if(longueurPhrase > 1):
            phraseInitiale = self.verbe.identifierVerbe(phraseInitiale)
            phraseInitiale = self.sujet.identifierSujet(phraseInitiale)
            phraseInitiale = self.marqueursNegation.identifierMarqueursNegation(phraseInitiale)
            phraseInitiale = self.marqueurTemporel.identifierMarqueurTemporel(phraseInitiale)
            phraseInitiale = self.adverbe.identifierAdverbe(phraseInitiale)

        phraseInitiale = self.action.identifierAction(phraseInitiale)

        if (longueurPhrase > 1):
            self.identifierMotsParDefaut()
            self.sujet.identifierPersConjug()
            self.action.choisirDeterminantAction(self.sujet, self.verbe)
            self.action.accorderAction()
            self.verbe.conjuguerVerbe(self.marqueurTemporel.tempsConjug, self.sujet, self.action.pronom_devant_verbe)
        return self


    # identifie les mots par defauts (les mots non dit mais deduits automatiquement)
    # cette methode est a appeler quand on a determine toute la strcuture de la phrase
    def identifierMotsParDefaut(self):
        # si pas de sujet mais verbe: sujet par defaut est "je"
        if self.sujet.texte == "" and self.verbe.texte != "":
            self.sujet.texte = "je"

        # si pas de verbe mais sujet, verbe par defaut est "être"
        if self.verbe.texte == "" and self.sujet.texte != "":
            self.verbe.texte = "être"

        # si ni verbe ni sujet mais il y a une action: verbe être et sujet ce
        if self.verbe.texte == "" and self.sujet.texte == "" and (self.action.texte != "" or self.adverbe.texte != ""):
            self.sujet.texte = "ce"
            self.verbe.texte = "être"
            self.sujet.persConjug = 3



    # determiner si certains mots doivent subir une élision
    def ajoutAppostrophes(self, phraseSplitee):
        elision = dictionnaireUtilisable.Elision()
        voyelles = ["a", "e", "i", "o", "u", "y"]
        voyellesSonS = ["a", "e", "i"]

        if len(phraseSplitee) > 1:
            for i in range(len(phraseSplitee)-1):
                if phraseSplitee[i] in elision.listeElisionsVoyelles and phraseSplitee[i+1][0] in voyelles:
                    phraseSplitee[i] = phraseSplitee[i][:-1]+"'"
                elif phraseSplitee[i] in elision.listeElisionSonS and phraseSplitee[i+1][0] in voyellesSonS:
                    phraseSplitee[i] = phraseSplitee[i][:-1]+"'"

        # reconstitution de la phrase
        phraseTraitee = "";
        for mot in phraseSplitee:
            if phraseTraitee != "" and phraseTraitee[-1] != "'":
                phraseTraitee += " "
            phraseTraitee += mot

        return phraseTraitee


    # determine la ponctuation da la phrase en fonction de certains indicateurs
    def determinerPonctuation(self, phrase):
        motsPonctuations = dictionnaireUtilisable.Ponctuations()
        ponctuation = ".";
        for mot in phrase.split():
            if mot in motsPonctuations.interrogatifs:
                ponctuation = "?"
                break

        return  ponctuation


    # retire les tirets des mots composés de la lsf, mais pas des mots avec des tirets de la langue française
    def nettoyerTirets(self, phrase):

        with open('dictionnaireUtilisable/noms.json') as json_data_noms:
            dictionnaireNoms = json.load(json_data_noms)
        phraseNettoyee = ""

        for mot in phrase.split():
            isMotFrancais = False
            if '-' in mot:
                for element in dictionnaireNoms:
                    if element[0] == mot:
                        isMotFrancais = True
                        break

                if isMotFrancais is False:
                    mot = mot.replace("-", " ")

            if phraseNettoyee == "":
                phraseNettoyee = mot
            else:
                phraseNettoyee += " "+mot

        return phraseNettoyee