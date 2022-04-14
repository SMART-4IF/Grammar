import tests

print("\nLancement des tests unitaires: ")
testsUnitaires = tests.TestsUnitaires()
testsUnitaires.run()
print(testsUnitaires)

print("Lancement des tests de traduction: ")
testsTraductions = tests.TestsTraductions()
testsTraductions.run()
print(testsTraductions)

