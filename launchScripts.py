import scriptsTraitement

# phrase sortie par l'IA de reconnaissance des signes
phraseInitiale = ["hier", "cinéma", "aller", "moi"]

# creation d'une phrase structuree
structurePhrase = scriptsTraitement.StructurePhrase()

# detection des elements structurels de la phrase (verbe, adverbe, nom, complement)
phraseInitiale = structurePhrase.identifierVerbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierMarqueurTemporel(phraseInitiale)
phraseInitiale = structurePhrase.identifierAdverbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierSujet(phraseInitiale)
phraseInitiale = structurePhrase.identifierAction(phraseInitiale)

# affichage du resultat
print(structurePhrase.toStringDebug())
print(structurePhrase)