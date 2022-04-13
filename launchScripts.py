import scriptsTraitement

# phrase sortie par l'IA de reconnaissance des signes
phraseInitiale = ["lui", "partir", "récemment", "lui"]

# création d'une phrase structuree
structurePhrase = scriptsTraitement.StructurePhrase()

# detection des elements structurels de la phrase (verbe, adverbe, nom, complement)
phraseInitiale = structurePhrase.identifierVerbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierAdverbe(phraseInitiale)
phraseInitiale = structurePhrase.identifierSujet(phraseInitiale)
phraseInitiale = structurePhrase.identifierComplement(phraseInitiale)

# affichage du résultat
print(structurePhrase.toStringDebug())
print(structurePhrase)