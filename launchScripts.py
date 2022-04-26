from traitementGrammaire import StructurePhrase

# phrase sortie par l'IA de reconnaissance des signes
phraseInitiale = ["lui", "partir", "lentement","lui"]
structurePhrase = structurePhrase = StructurePhrase()
structurePhrase = structurePhrase.traduire(phraseInitiale)

# debug
print("")
print(structurePhrase.toStringDebug())
print(structurePhrase)