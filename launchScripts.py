from traitementGrammaire import StructurePhrase

# phrase sortie par l'IA de reconnaissance des signes
phraseInitiale = ["bonbon", "lui", "vouloir"]
structurePhrase = structurePhrase = StructurePhrase()
structurePhrase = structurePhrase.traduire(phraseInitiale)

# debug
print("")
print(structurePhrase.toStringDebug())
print(structurePhrase)