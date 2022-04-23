# hier cinéma aller moi 
# hier je suis allé au cinéma 
from contextlib import nullcontext
import json
import dictionnaireUtilisable
from verbecc import Conjugator

class StructurePhrase:

    def __init__(self, sujet = "", pronom_devant_verbe = "", verbe = "", action = "", marqueurTemporel = "", adverbe = "", tempsConjug = "présent",
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

        if self.marqueurNegation1 != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.marqueurNegation1

        if self.pronom_devant_verbe != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.pronom_devant_verbe

        if self.verbe != "":
            if len(phrase) > 1 and "'" != phrase [-1]:
                phrase += " "
            phrase += self.verbe

        if self.marqueurNegation2 != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.marqueurNegation2

        if self.action != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.action

        if self.adverbe != "":
            if len(phrase) > 1:
                phrase += " "
            phrase += self.adverbe

        # choix de la ponctuation adaptee
        phrase += self.determinerPonctuation(phrase)

        # on retire les - des mots composes
        phrase = self.nettoyerTirets(phrase)

        return phrase.capitalize()

    def toStringDebug(self):
        return "marqueurTemporel : " + self.marqueurTemporel + " | sujet : " + self.sujet + \
               " | marqueur neg 1 : " + self.marqueurNegation1 + " | pronom devant verbe : " + self.pronom_devant_verbe + \
               " | verbe : " + self.verbe + " | marqueur neg 2 : " + self.marqueurNegation2 + \
               " | action : " + self.action + " | adverbe : " + self.adverbe + " | temps : " + self.tempsConjug + \
               " | pers conjug: " + str(self.persConjug)

    def __eq__(self, other):
        return self.marqueurTemporel == other.marqueurTemporel and self.sujet == other.sujet and \
               self.marqueurNegation1 == other.marqueurNegation1 and self.pronom_devant_verbe == other.pronom_devant_verbe and \
               self.verbe == other.verbe and self.marqueurNegation2 == other.marqueurNegation2 \
               and self.action == other.action and self.adverbe == other.adverbe and self.tempsConjug == other.tempsConjug and \
               self.persConjug == other.persConjug

    # execute l'ensemble du process de traduction
    def traduire(self, phraseInitiale):

        phraseInitiale = self.identifierVerbe(phraseInitiale)
        phraseInitiale = self.identifierSujet(phraseInitiale)
        self.identifierMotsParDefaut()
        phraseInitiale = self.identifierMarqueursNegation(phraseInitiale)
        phraseInitiale = self.identifierMarqueurTemporel(phraseInitiale)
        phraseInitiale = self.identifierAdverbe(phraseInitiale)
        phraseInitiale = self.identifierAction(phraseInitiale)
        self.identifierPersConjug()
        self.choisirDeterminantAction()
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
    # IMPORATNT ! Doit etre appele après identifierMarqueurTemporel
    # phrase : liste de mots dans laquelle il faut trouver l'adverbe
    def identifierAdverbe(self, phrase):
        # ouverture du dictionnaire des adverbes francais
        with open('dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
            dictionnaireAdverbes = json.load(json_data_adverbe)
        marqueursTemporelsLSF = dictionnaireUtilisable.MarqueursTemporels()

        # si mot est dans dictionnaire des adverbes : c'est un adverbes
        testMarqueurTemporel = False
        for mot in phrase:
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

        marqueurTrouve = False
        motPrecedent = ""
        for mot in phrase:
            # si mot est dans dictionnaire des marqueurs temporels simbles : c'est un marqueur temporel
            for marqueur in marqueursTemporelsLSF.marqueursSimples:
                if mot == marqueur.mot:
                    self.tempsConjug = marqueur.tempsAssocie
                    if marqueur.isIndispanesable:
                        self.marqueurTemporel = mot
                    phrase.remove(mot)
                    marqueurTrouve = True
                    break

            if marqueurTrouve:
                break

            # si mot precedent + mot est dans dictionnaire des marqueurs temporels doubles : c'est un marqueur temporel
            for marqueur in marqueursTemporelsLSF.marqueursDoubles:
                if motPrecedent != "" and (motPrecedent + " " + mot) == marqueur.mot:
                    self.tempsConjug = marqueur.tempsAssocie
                    self.marqueurTemporel = motPrecedent + " " + mot
                    phrase.remove(motPrecedent)
                    phrase.remove(mot)
                    marqueurTrouve = True
                    break

            if marqueurTrouve:
                break

            motPrecedent = mot

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

        if len(tmp)==2:
            if(tmp[0]==tmp[1]): 
                self.sujet = tmp[0]
                phrase.remove(tmp[0])
                phrase.remove(tmp[1])
            else:
                self.sujet = tmp[1]
                self.complement = tmp[0]
        elif len(tmp)==1:
            self.sujet = tmp[0]
            phrase.remove(tmp[0])

        return phrase


    # identifie les marqueurs de negation
    def identifierMarqueursNegation(self, phrase):
        marqueursNegation = dictionnaireUtilisable.MarqueursNegation()

        if self.verbe != "":
            for mot in phrase:
                if mot in marqueursNegation.simple:
                    self.marqueurNegation1 = "ne"
                    self.marqueurNegation2 = mot
                    phrase.remove(mot)
                if mot in marqueursNegation.double:
                    self.marqueurNegation1 = "ne"
                    self.marqueurNegation2 = "pas"
                    phrase.remove(mot)

        return phrase


    # Recherche action dans une sequence donnee de mots et init la val de self.action avec
    # phrase : liste de mots dans laquelle il faut trouver l'action
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
                    index = 0
                    #a-lui devient son !!! toujours au masculin
                    for pronom in pronomsLSF.possessifs:
                        if pronom == mot:
                            mot = pronomsFR.possessifsMasculin[index]
                        index+=1
                    self.action = mot
                    listeMotsSupprimer.append(mot)
                    testPossessif = True
                elif testPossessif:
                    for element in dictionnaireNoms:
                        if mot == element[0]:
                            self.action += " "+mot
                            listeMotsSupprimer.append(mot)
                            break

            for mot in listeMotsSupprimer:
                if mot in phrase:
                    phrase.remove(mot)

            if testPossessif == False:
                # pour l'instant, ce qu'il reste dans la liste de mots devient l'action
                if phrase[0] in pronomsLSF.personnels:
                    #test verbe pour savoir si commence par une voyelle 
                    voyelle = ["a","e","i","o","u"]
                    verbe_voyelle = False
                    if self.verbe[0] in voyelle : 
                        verbe_voyelle = True
                    index = 0
                    for pronom in pronomsLSF.personnels:
                        if pronom == phrase[0]:
                            if verbe_voyelle == False :
                                self.pronom_devant_verbe = pronomsFR.pronoms_devant_verbe[index]
                            else : 
                                self.pronom_devant_verbe = pronomsFR.pronoms_devant_verbe_voyelle[index]
                        index+=1
                else:
                    for mot in phrase:
                        if self.action == "":
                            self.action = mot
                        else:
                            self.action += " "+mot

            return ""

    # identifie les mots par defauts (les mots non dit mais deduits automatiquement)
    # cette methode est a appeler quand on a determine toute la strcuture de la phrase
    def identifierMotsParDefaut(self):
        # si pas de sujet mais verbe: sujet par defaut est "je"
        if self.sujet == "" and self.verbe != "":
            self.sujet = "je"

        # si pas de verbe mais sujet, verbe par defaut est "être"
        if self.verbe == "" and self.sujet != "":
            self.verbe = "être"

    # identifie la personne a laquelle il faut conjuguer le verbe
    def identifierPersConjug(self):
        pronomsLSF = dictionnaireUtilisable.PronomsLSF()
        pronomsFR = dictionnaireUtilisable.PronomsFR()
        index = 0
        for pronom in pronomsLSF.personnels:
            if pronom == self.sujet:
                self.sujet = pronomsFR.personnels[index]
                self.persConjug = index +1
            index+=1


    # choisir le determinent du complement
    # si le complement possede un nom commun, il faut placer un determinant adapte
    def choisirDeterminantAction(self):
        with open('dictionnaireUtilisable/noms.json') as json_data_noms:
            dictionnaireNoms = json.load(json_data_noms)
        pronomsFR = dictionnaireUtilisable.PronomsFR()
        voyelles = ["a", "e", "i", "o", "u"]

        # si on est dans une phrase avec pronom personnel + etre ou phrase d'un seul mot: pas de determinant
        if (self.sujet in pronomsFR.personnels and self.verbe == "être") is False and (self.sujet == "" and self.verbe == "") is False:

            for mot in self.action.split():

                # s'il y a un pronom possessif, pas besoin de determinant
                if mot in pronomsFR.possessifsMasculin or mot in pronomsFR.possessifsFeminin or mot in pronomsFR.possessifsPluriel:
                    break

                for element in dictionnaireNoms:
                    if mot == element[0]:
                        if element[1] == "m" and self.verbe == "aller" and element[0] in voyelles:
                            self.action = "à l'"+self.action
                        elif element[1] == "m" and self.verbe == "aller" and element[0] not in voyelles:
                            self.action = "au "+self.action
                        elif element[1] == "f" and self.verbe == "aller" and element[0] in voyelles:
                            self.action = "à l'"+self.action
                        elif element[1] == "f" and self.verbe == "aller" and element[0] not in voyelles:
                            self.action = "à la "+self.action
                        elif element[1] == "f":
                            self.action = "une " + self.action
                        else:
                            self.action = "un " + self.action


    # conjugue le verbe selon le temps et la personne identifies
    def conjuguerVerbe(self):
        if self.verbe != "":
            cg = Conjugator(lang='fr')
            conjugaisonsDuVerbe = cg.conjugate(self.verbe)
            verbeConjugue = conjugaisonsDuVerbe['moods']['indicatif'][self.tempsConjug][self.persConjug - 1]

            # si pronom j', le split ne marche pas.
            if "'" in verbeConjugue:
                if self.pronom_devant_verbe == "":
                    if self.sujet == "je":
                        self.sujet = "j'"
                self.verbe = verbeConjugue[2:]
            else:
                verbeConjugue = verbeConjugue.split()
                verbeConjugue = verbeConjugue[1:]
                self.verbe = " ".join(verbeConjugue)


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
            isMotFrançais = False
            if '-' in mot:
                for element in dictionnaireNoms:
                    if element[0] == mot:
                        isMotFrançais = True
                        break

                if isMotFrançais is False:
                    mot = mot.replace("-", " ")

            if phraseNettoyee == "":
                phraseNettoyee = mot
            else:
                phraseNettoyee += " "+mot

        return phraseNettoyee