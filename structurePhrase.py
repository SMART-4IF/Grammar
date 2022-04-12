# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json
from dictionnaireUtilisable.autresMotsLSF import *
from dictionnaireUtilisable.autresMotsFrançais import *

class structurePhrase:
    def __init__(self): 
        self.adverbe = ""
        self.sujet = ""
        self.verbe = ""
        self.complement = ""

phraseFinale = ["","","",""]

# si le mot est dans la liste des verbes; c'est un verbe
def rechercheVerbe(phrase, data_dict_verbe) :
    for mot in phrase :
        if mot in data_dict_verbe:
            phraseFinale[2] = mot

#si le mot est dans la liste des adverbes, c'est un adverbe
def rechercheAdverbe(phrase, data_dict_adverbe) :
    for mot in phrase :
        if mot in data_dict_adverbe:
            phraseFinale[0] = mot

# si le mot est dans la liste des pronoms, on le met en sujet
def rechercheSujet(phrase, pronomsLSF, pronomsFR) :
    for mot in phrase :
        if mot in pronomsLSF.personnels:
            #trouver le pronom correspondant
            phraseFinale[1] = mot
            phrase.remove(mot)

def initStructurePhrase(phrase) :

    with open('dictionnaireUtilisable/verbes.json') as json_data_verbe:
        data_dict_verbe = json.load(json_data_verbe)

    with open('dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
        data_dict_adverbe = json.load(json_data_adverbe)

    pronomsLSF = PronomsLSF()
    pronomsFR = PronomsFR()

    rechercheVerbe(phrase, data_dict_verbe)
    phrase.remove(phraseFinale[2])

    rechercheAdverbe(phrase, data_dict_adverbe)
    phrase.remove(phraseFinale[0])

    rechercheSujet(phrase, pronomsLSF, pronomsFR)
    phraseFinale[3]=phrase[0] # complement (dernier terme restant)

    return(phraseFinale)

print(initStructurePhrase(["hier","cinéma","moi","aller"]))




