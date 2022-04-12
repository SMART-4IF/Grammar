# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json
from .. import dictionnaireUtilisable

class StructurePhrase:
    def __init__(self): 
        self.adverbe = ""
        self.sujet = ""
        self.verbe = ""
        self.complement = ""

    def __str__(self):
        return "adverbe : " + self.adverbe + " | sujet : " + self.sujet + " | verbe : " + self.verbe + " | complement : " + self.complement

structurePhrase = StructurePhrase()

# si le mot est dans la liste des verbes; c'est un verbe
def rechercheVerbe(phrase, data_dict_verbe) :
    for mot in phrase :
        if mot in data_dict_verbe:
            structurePhrase.verbe = mot

#si le mot est dans la liste des adverbes, c'est un adverbe
def rechercheAdverbe(phrase, data_dict_adverbe) :
    for mot in phrase :
        if mot in data_dict_adverbe:
            structurePhrase.adverbe = mot

# si le mot est dans la liste des pronoms, on le met en sujet
def rechercheSujet(phrase, pronomsLSF, pronomsFR) :
    for mot in phrase :
        if mot in pronomsLSF.personnels:
            #trouver le pronom correspondant
            structurePhrase.sujet = mot
            phrase.remove(mot)

def initStructurePhrase(phrase) :

    with open('../dictionnaireUtilisable/verbes.json') as json_data_verbe:
        data_dict_verbe = json.load(json_data_verbe)

    with open('../dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
        data_dict_adverbe = json.load(json_data_adverbe)

    pronomsLSF = dictionnaireUtilisable.autresMotsLSF.PronomsLSF()
    pronomsFR = dictionnaireUtilisable.autresMotsFrançais.PronomsFR()

    rechercheVerbe(phrase, data_dict_verbe)
    phrase.remove(structurePhrase.verbe)

    rechercheAdverbe(phrase, data_dict_adverbe)
    phrase.remove(structurePhrase.adverbe)

    rechercheSujet(phrase, pronomsLSF, pronomsFR)
    structurePhrase.complement = phrase[0] # complement (dernier terme restant)

    return(structurePhrase)

print(initStructurePhrase(["hier","cinéma","moi","aller"]))




