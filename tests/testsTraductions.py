import scriptsTraitement

class TestsTraductions:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesSucces = []
        self.messagesEchecs = []
        self.resultatsAttendus = [
            "Je sais.",                             #testTrad1
            "Il est entendant.",                    #testTrad2
            "Récemment, il est parti.",             #testTrad3
            "Je le connais.",                       #testTrad4
            "Tu signes lentement.",                 #testTrad5
            "Je ne suis pas d’accord.",             #testTrad6
            "Il ne fait rien.",                     #testTrad7
            #"J’irai demain.",                       #testTrad8
        ]

    def __str__(self):
        res = ""
        if self.nbTestsReussis > 0:
            res += "-----------------------------------------------------------------------------\n"
            res += "|                                "+str(self.nbTestsReussis) + " / " +\
                   str(self.nbTests)+" succes                              |\n"
            res += "-----------------------------------------------------------------------------\n"
            for message in self.messagesSucces:
                res += "| " + message + "\n"
            res += "-----------------------------------------------------------------------------\n\n"


        if self.nbTests != self.nbTestsReussis:
            res += "-----------------------------------------------------------------------------\n"
            res += "|                                Echecs                                     |\n"
            res += "-----------------------------------------------------------------------------\n"
            for message in self.messagesEchecs:
                res += "| " + message + "\n"
            res += "-----------------------------------------------------------------------------\n"

        return res

    def run(self):
        self.testTraduction1()
        self.testTraduction2()
        self.testTraduction3()
        self.testTraduction4()
        self.testTraduction5()
        self.testTraduction6()
        self.testTraduction7()
        # self.testTraduction8()


    def testTraduction1(self):
        phrase = ["moi", "savoir", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Moi savoir moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 1 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction2(self):
        phrase = ["lui", "entendant", "lui"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui entendant lui. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 2 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction3(self):
        phrase = ["lui", "partir", "récemment", "lui"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui partir récemment lui. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 3 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction4(self):
        phrase = ["lui", "connaitre", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui connaitre moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 4 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction5(self):
        phrase = ["toi", "signer", "lentement"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Toi signer lentement. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 5 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction6(self):
        phrase = ["moi", "d’accord", "non"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Moi d’accord non. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 6 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction7(self):
        phrase = ["lui", "faire", "rien"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui faire rien. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 7 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    # trace
    # print(structurePhrase.toStringDebug())
    # print(self.resultatsAttendus[self.nbTests].toStringDebug())