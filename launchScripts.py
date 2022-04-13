import scriptsTraitement

# phrase sortie par l'IA de reconnaissance des signes
<<<<<<< HEAD
phraseInitiale = ["hier", "cinéma", "aller", "moi"]
=======
phraseInitiale = ["lui", "partir", "récemment", "lui"]
>>>>>>> 24958a82364d13e687aef0870de5d14d51600f26

# création d'une phrase structuree
structurePhrase = scriptsTraitement.StructurePhrase()

# detection des elements structurels de la phrase (verbe, adverbe, nom, complement)
phraseInitiale = structurePhrase.identifierVerbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierAdverbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierSujet(phraseInitiale)
phraseInitiale = structurePhrase.identifierComplement(phraseInitiale)
structurePhrase.identifierTempsConjug()

# affichage du résultat
print(structurePhrase.toStringDebug())
print(structurePhrase)