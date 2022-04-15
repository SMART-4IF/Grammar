import scriptsTraitement

class TestsTraductions:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesSucces = []
        self.messagesEchecs = []
        self.resultatsAttendus = [
            "Je sais.",                                         #testTrad1
            "Il est entendant.",                                #testTrad2
            "Récemment, il est parti.",                         #testTrad3
            "Je le connais.",                                   #testTrad4
            "Tu signes lentement.",                             #testTrad5
            "Je ne suis pas d’accord.",                         #testTrad6
            "Il ne fait rien.",                                 #testTrad7
            "Demain, j'irai.",                                  #testTrad8
            "Je l'appelle.",                                    #testTrad9
            "Hier, j'ai travaillé.",                            #testTrad10
            "Demain, je travaillerai.",                         #testTrad11
            "Il est son ami.",                                  #testTrad12
            "J'ai acheté une voiture.",                         #testTrad13
            "Hier, je suis allé au cinéma.",                    #testTrad14
            "Jeudi prochain, il partira en vacances.",          #testTrad15
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
        self.testTraduction8()
        self.testTraduction9()
        self.testTraduction10()
        self.testTraduction11()
        self.testTraduction12()
        self.testTraduction13()
        self.testTraduction14()
        self.testTraduction15()


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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

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
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction8(self):
        phrase = ["demain", "aller", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Demain aller moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 8 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1

    def testTraduction9(self):
        phrase = ["lui", "appeler", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui appeler moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 9 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction10(self):
        phrase = ["hier", "moi", "travailler", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Hier moi travailler moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 10 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction11(self):
        phrase = ["demain", "moi", "travailler", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Demain moi travailler moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 11 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction12(self):
        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Lui a-lui ami. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 12 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction13(self):
        phrase = ["moi", "voiture", "acheter", "fini"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Moi voiture acheter fini. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 13 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction14(self):
        phrase = ["hier", "cinéma", "aller", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Hier cinéma aller moi. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 14 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    def testTraduction15(self):
        phrase = ["jeudi", "prochain", "lui", "partir", "vacances"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.traduire(phrase)

        if str(structurePhrase) == self.resultatsAttendus[self.nbTests]:
            self.messagesSucces.append("Jeudi prochain lui partir vacances. = " + str(structurePhrase))
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test trad 15 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    # trace
    # print(structurePhrase.toStringDebug())
