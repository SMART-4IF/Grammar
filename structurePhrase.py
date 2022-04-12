# hier cinéma aller moi 
# hier je suis allé au cinéma 
import json

with open('dictionnaireUtilisable/verbes.json') as json_data:
    data_dict = json.load(json_data)
    #print(data_dict)

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
        print(len(data_dict))
        for i in range(len(data_dict)) : 
            print(i)
            if(mot == data_dict[i]):
                phraseFinale[2] = mot

print(phraseFinale[2])





