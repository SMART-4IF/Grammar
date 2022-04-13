import scriptsTraitement

class TestsUnitaires:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesEchecs = []
        self.resultatsAttendus = [
            scriptsTraitement.StructurePhrase("", "", "aller", ""),                     #testVerbe1
            scriptsTraitement.StructurePhrase("", "", "être", ""),                      #testVerbe2
            scriptsTraitement.StructurePhrase("hier", "", "", ""),                      #testAdverbe1
            scriptsTraitement.StructurePhrase("", "moi", "", ""),                       #testSujet1
            scriptsTraitement.StructurePhrase("", "", "", "a-lui ami"),                 #testComplement1
            scriptsTraitement.StructurePhrase("hier", "moi", "aller", "cinéma"),        #testStructPhrase1
        ]

    def __str__(self):
        res = str(self.nbTestsReussis) + " / " + str(self.nbTests) + " tests passés avec succès. \n"
        if self.nbTests != self.nbTestsReussis:
            res += "-----------------------------------------------------------------------------\n"
            res += "|                           Description des echecs                          |\n"
            res += "-----------------------------------------------------------------------------\n"
            for message in self.messagesEchecs:
                res += "| " + message + "\n"
            res += "-----------------------------------------------------------------------------\n"
        return res

    def run(self):
        self.testVerbe1()
        self.testVerbe2()
        self.testAdverbe1()
        self.testSujet1()
        self.testComplement1()
        self.testStructPhrase1()


    # verifie que l'on est bien capable d'identifier le verbe de la phrase
    def testVerbe1(self):
        phrase = ["hier","cinéma","moi","aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierVerbe(phrase)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append("Test verbe 1 - Obtenu : '" + structurePhrase.verbe +"' | attendu : '" + self.resultatsAttendus[self.nbTests].verbe +"'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le verbe de la phrase
    def testVerbe2(self):
        phrase = ["lui", "son", "ami"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierVerbe(phrase)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test verbe 2 - Obtenu : '" + structurePhrase.verbe + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests].verbe + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier l'adverbe de la phrase
    def testAdverbe1(self):
        phrase = ["hier","cinéma","moi","aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierAdverbe(phrase)

        if structurePhrase.adverbe == self.resultatsAttendus[self.nbTests].adverbe :
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append("Test adverbe 1 - Obtenu : '" + structurePhrase.adverbe +"' | attendu : '" + self.resultatsAttendus[self.nbTests].adverbe +"'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le sujet de la phrase
    def testSujet1(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierSujet(phrase)

        if structurePhrase.sujet == self.resultatsAttendus[self.nbTests].sujet:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test sujet 1 - Obtenu : '" + structurePhrase.sujet + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].sujet + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le sujet de la phrase
    def testComplement1(self):
        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierComplement(phrase)

        if structurePhrase.complement == self.resultatsAttendus[self.nbTests].complement:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test complement 1 - Obtenu : '" + structurePhrase.complement + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].complement + "'")

        self.nbTests = self.nbTests + 1


    # verifie que tous les termes sont bien reconnus dans une phrase simple
    def testStructPhrase1(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierAdverbe(phrase)
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierComplement(phrase)

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 1 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1