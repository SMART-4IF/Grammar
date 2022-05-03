from traitementGrammaire import StructurePhrase
import time

# phrase sortie par l'IA de reconnaissance des signes
startTime = time.time()
phraseInitiale = ["lui", "manger", "lentement","lui"]
structurePhrase = StructurePhrase()
structurePhrase = structurePhrase.traduire(phraseInitiale)
print("temps: "+str(time.time() - startTime))

# debug
print("")
print(structurePhrase.toStringDebug())
print(structurePhrase)