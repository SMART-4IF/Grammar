import scriptsTraitement

class TestsUnitaires:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesEchecs = []
        self.resultatsAttendus = [
            scriptsTraitement.StructurePhrase("", "", "aller"),                                         #testVerbe1
            scriptsTraitement.StructurePhrase("", "", "être"),                                          #testVerbe2
            scriptsTraitement.StructurePhrase("", "", "", "", "", "lentement"),                         #testAdverbe1
            scriptsTraitement.StructurePhrase("moi", ""),                                               #testSujet1
            scriptsTraitement.StructurePhrase("moi", ""),                                               #testSujet2
            scriptsTraitement.StructurePhrase("", "",  "", "son ami"),                                 #testAction1
            scriptsTraitement.StructurePhrase("", "", "", "", "récemment", "", "passé-composé"),        # testTemps1
            scriptsTraitement.StructurePhrase("", "",  "", "", "", "", "passé-composé"),             # testTemps2
            scriptsTraitement.StructurePhrase("moi","",  "aller", "cinéma", "hier", "", "passé-composé"),   #testStructPhrase1
            scriptsTraitement.StructurePhrase("lui","",  "être", "son ami"),                          #testStructPhrase2
            scriptsTraitement.StructurePhrase("moi", "le",  "connaitre", ""),                           #testStructPhrase3
            scriptsTraitement.StructurePhrase("lui","",  "partir", "", "récemment", "", "passé-composé"),   #testStructPhrase4
            scriptsTraitement.StructurePhrase("", "",  "", "", "", "", "", 1),                          #testIdentificationPersConj1
            scriptsTraitement.StructurePhrase("", "", "vais"),                                          #testConj1
            scriptsTraitement.StructurePhrase("", "", "suis allé"),                                     #testConj2
            scriptsTraitement.StructurePhrase("", "",  "", "", "", "", "", 1, "ne", "rien"),            #testNegation1
            scriptsTraitement.StructurePhrase("", "",  "", "", "", "", "", 1, "ne", "pas"),             #testNegation2
            scriptsTraitement.StructurePhrase("", "t'", "appelle"),                                     #testPronomDevantVerbe
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
        self.testSujet2()
        self.testAction1()
        self.testTemps1()
        self.testTemps2()
        self.testStructPhrase1()
        self.testStructPhrase2()
        self.testStructPhrase3()
        self.testStructPhrase4()
        self.testIdentificationPersConj1()
        self.testConj1()
        self.testConj2()
        self.testNegation1()
        self.testNegation2()
        self.testPronomDevantVerbe()


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
        phrase = ["toi", "signer", "lentement"]
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

    # verifie que l'on est bien capable d'identifier le sujet de la phrase quand deux pronoms
    def testSujet2(self):
        phrase = ["lui", "connaitre", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierSujet(phrase)

        if structurePhrase.sujet == self.resultatsAttendus[self.nbTests].sujet:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test sujet 2 - Obtenu : '" + structurePhrase.sujet + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].sujet + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le complément de la phrase
    def testAction1(self):
        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierAction(phrase)

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test action 1 - Obtenu : '" + structurePhrase.action + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].action + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on identifie bien le marqueur temporel et le temps de cette phrase (et on laisse le marqueur car indispensable)
    def testTemps1(self):
        phrase = ["lui", "partir", "récemment", "lui"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)

        if structurePhrase.marqueurTemporel == self.resultatsAttendus[self.nbTests].marqueurTemporel \
                and structurePhrase.tempsConjug == self.resultatsAttendus[self.nbTests].tempsConjug:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test temps 1 - Obtenu : '" + structurePhrase.marqueurTemporel + " "
                + structurePhrase.tempsConjug + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].marqueurTemporel + " "
                + self.resultatsAttendus[self.nbTests].tempsConjug + "'")

        self.nbTests = self.nbTests + 1  # verifie que l'on identifie bien le temps de cette phrase (et on laisse le marqueur car indispensable)


    # verifie que l'on identifie bien le temps de cette phrase (et on retire le marqueur car dispensable)
    def testTemps2(self):
        phrase = ["moi", "voiture", "acheter", "fini"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)

        if structurePhrase.marqueurTemporel == self.resultatsAttendus[self.nbTests].marqueurTemporel \
                and structurePhrase.tempsConjug == self.resultatsAttendus[self.nbTests].tempsConjug:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test temps 2 - Obtenu : '" + structurePhrase.marqueurTemporel + " "
                + structurePhrase.tempsConjug + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].marqueurTemporel + " "
                + self.resultatsAttendus[self.nbTests].tempsConjug + "'")

        self.nbTests = self.nbTests + 1


    # verifie que tous les termes et le temps sont bien reconnus dans une phrase simple
    def testStructPhrase1(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.identifierAdverbe(phrase)
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 1 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    # verifie que tous les termes et le temps sont bien reconnus dans une phrase simple avec action
    # compose d'un possessif et d'un nom
    def testStructPhrase2(self):
        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.identifierAdverbe(phrase)
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 2 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    # verifie que tous les termes sont bien reconnus dans une phrase simple avec action
    # compose d'un possessif et d'un nom
    def testStructPhrase3(self):
        phrase = ["lui", "connaitre", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.identifierAdverbe(phrase)
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 3 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on supprime les double pronom
    def testStructPhrase4(self):
        phrase = ["lui", "partir", "récemment","lui"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.identifierAdverbe(phrase)
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 4 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1

    # verifie que l'on identifie lq premiere personne pour la conj
    def testIdentificationPersConj1(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierSujet(phrase)
        structurePhrase.identifierPersConjug()

        if structurePhrase.persConjug == self.resultatsAttendus[self.nbTests].persConjug:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test identif pers conj 1 - Obtenu : '" + str(structurePhrase.persConjug) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].persConjug) + "'")

        self.nbTests = self.nbTests + 1

    # verifie si l'on est capable de conjuguer verbe au present 1p sg
    def testConj1(self):
        phrase = ["cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        structurePhrase.identifierPersConjug()
        structurePhrase.conjuguerVerbe()

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test conj 1 - Obtenu : '" + str(structurePhrase.verbe) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].verbe) + "'")

        self.nbTests = self.nbTests + 1

    # verifie si l'on est capable de conjuguer verbe au passé composé 1p sg
    def testConj2(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierMarqueurTemporel(phrase)
        structurePhrase.identifierPersConjug()
        structurePhrase.conjuguerVerbe()

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test conj 2 - Obtenu : '" + str(structurePhrase.verbe) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].verbe) + "'")

        self.nbTests = self.nbTests + 1


    # test si la negation est bien identifiee (negation avec seulement ne devant verbe)
    def testNegation1(self):
        phrase = ["lui", "faire", "rien"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierMarqueursNegation(phrase)

        if structurePhrase.marqueurNegation1 == self.resultatsAttendus[self.nbTests].marqueurNegation1 and \
                structurePhrase.marqueurNegation2 == self.resultatsAttendus[self.nbTests].marqueurNegation2:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test negation 1 - Obtenu : '" + structurePhrase.marqueurNegation1 + " " + structurePhrase.marqueurNegation2
                + "' | attendu : '" + self.resultatsAttendus[self.nbTests].marqueurNegation1 + " "
                + self.resultatsAttendus[self.nbTests].marqueurNegation2 + "'")

        self.nbTests = self.nbTests + 1


    # test si la negation est bien identifiee (ne + pas)
    def testNegation2(self):
        phrase = ["moi", "d’accord", "non"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        structurePhrase.identifierMarqueursNegation(phrase)

        if structurePhrase.marqueurNegation1 == self.resultatsAttendus[self.nbTests].marqueurNegation1 and \
                structurePhrase.marqueurNegation2 == self.resultatsAttendus[self.nbTests].marqueurNegation2:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test negation 2 - Obtenu : '" + structurePhrase.marqueurNegation1 + " " + structurePhrase.marqueurNegation2
                + "' | attendu : '" + self.resultatsAttendus[self.nbTests].marqueurNegation1 + " "
                + self.resultatsAttendus[self.nbTests].marqueurNegation2 + "'")

        self.nbTests = self.nbTests + 1


    def testPronomDevantVerbe(self):
        phrase = ["toi", "appeler", "moi"]
        structurePhrase = scriptsTraitement.StructurePhrase()
        phrase = structurePhrase.identifierSujet(phrase)
        phrase = structurePhrase.identifierVerbe(phrase)
        phrase = structurePhrase.identifierAction(phrase)
        structurePhrase.identifierPersConjug()
        structurePhrase.conjuguerVerbe()

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test pronom devant verbe - Obtenu : '" + str(structurePhrase.verbe) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].verbe) + "'")

        self.nbTests = self.nbTests + 1


    # trace
    # print(structurePhrase.toStringDebug())
    # print(self.resultatsAttendus[self.nbTests].toStringDebug())