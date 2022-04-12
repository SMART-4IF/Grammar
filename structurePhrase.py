# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json
from dictionnaireUtilisable.autresMotsLSF import *
from dictionnaireUtilisable.autresMotsFrançais import *

with open('dictionnaireUtilisable/verbes.json') as json_data_verbe:
    data_dict_verbe = json.load(json_data_verbe)

with open('dictionnaireUtilisable/adverbes.json') as json_data_adverbe:
    data_dict_adverbe = json.load(json_data_adverbe)


phrase = ["hier","cinéma","moi","aller"]
phraseFinale = ["","","",""]

class structurePhrase:
    def __init__(self): 
        self.adverbe = ""
        self.sujet = ""
        self.verbe = ""
        self.complement = " "


# trouver verbe 
def rechercheVerbe(phrase) :
    for mot in phrase : 
        #si le mot est dans la liste de verbe, on l'ajoute dans la case corespondante 
        for i in range(len(data_dict_verbe)) : 
            if(mot == data_dict_verbe[i]):
                phraseFinale[2] = mot

rechercheVerbe(phrase)
print(phraseFinale[2])
phrase.remove(phraseFinale[2])

#trouver adverbe 
def rechercheAdverbe(phrase) :
    for mot in phrase : 
        #si le mot est dans la liste de verbe, on l'ajoute dans la case corespondante 
        for i in range(len(data_dict_adverbe)) : 
            if(mot == data_dict_adverbe[i]):
                phraseFinale[0] = mot
                


rechercheAdverbe(phrase)
print(phraseFinale[0])
phrase.remove(phraseFinale[0])


pronomsLSF = PronomsLSF()
pronomsFR = PronomsFR()
#print(pronomsLSF.personnels)
#print(pronomsFR.personnels)

mot_a_retirer = " "
#trouver le pronom
def recherchePronom(phrase) :
    for mot in phrase : 
        #si le mot est dans la liste de verbe, on l'ajoute dans la case corespondante 
        for i in range(len(pronomsLSF.personnels)) : 
            if(mot == pronomsLSF.personnels[i]):
                #trouver le pronom correspondant
                phraseFinale[1] = pronomsFR.personnels[i]
                phrase.remove(mot)

recherchePronom(phrase)
print(phraseFinale[1])

print(phrase)
phraseFinale[3]=phrase[0]

print(phraseFinale)









