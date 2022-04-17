from scriptsTraitement import StructurePhrase

# phrase sortie par l'IA de reconnaissance des signes
phraseInitiale = ["jeudi", "prochain", "lui", "aller", "camping"]
structurePhrase = structurePhrase = StructurePhrase()
structurePhrase = structurePhrase.traduire(phraseInitiale)

# debug
print("")
print(structurePhrase.toStringDebug())
print(structurePhrase)