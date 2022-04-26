import traitementGrammaire

StructurePhrase = traitementGrammaire.StructurePhrase
Sujet = traitementGrammaire.Sujet
Adverbe = traitementGrammaire.Adverbe

class TestsUnitaires:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesEchecs = []
        self.resultatsAttendus = [
            StructurePhrase("", "", "aller"),                                                                  #testVerbe1
            StructurePhrase("", "", ""),                                                                       #testVerbe2
            StructurePhrase("", "", "", "", "", "lentement"),                                                  #testAdverbe1
            StructurePhrase("moi", ""),                                                                      #testSujet1
            StructurePhrase("moi", ""),                                                                      #testSujet2
            StructurePhrase("", "", "", "son ami"),                                                            #testAction1
            StructurePhrase("", "", "", "avec Bob"),                                                           #testAction1
            StructurePhrase("", "", "", "", "récemment", "", 1, "passé-composé"),                                 #testTemps1
            StructurePhrase("", "", "", "", "", "", 1, "passé-composé"),                                          #testTemps2
            StructurePhrase("", "", "", "", "jeudi dernier", "", 1, "passé-composé"),                             #testTemps3
            StructurePhrase("moi", "", "aller", "cinéma", "hier", "", 1, "passé-composé"),   #testStructPhrase1
            StructurePhrase("lui", "", "être", "son ami"),                            #testStructPhrase2
            StructurePhrase("moi", "le", "connaitre", ""),                           #testStructPhrase3
            StructurePhrase("lui", "", "partir", "", "récemment", "", 1, "passé-composé"),   #testStructPhrase4
            StructurePhrase("", "", "", "", "", "", 3),                          #testIdentificationPersConj1
            StructurePhrase("", "", "vais"),                                          #testConj1
            StructurePhrase("", "", "suis allé"),                                     #testConj2
            StructurePhrase("", "", "", "", "", "", 1, "", "ne", "rien"),            #testNegation1
            StructurePhrase("", "", "", "", "", "", 1, "", "ne", "pas"),             #testNegation2
            StructurePhrase("", "te"),                                                #testPronomDevantVerbe
            StructurePhrase("", "", "", "une voiture"),                               #testChoixDeterminant1
            StructurePhrase("", "", "", "au cinéma"),                                 #testChoixDeterminant2
            StructurePhrase("", "", "", "son ami"),                                   #testChoixDeterminant3
            StructurePhrase("", "", "", "entendant"),                                 #testChoixDeterminant4
            StructurePhrase("", "", "", "sept voitures"),                             #testAccordAction1
            StructurePhrase("", "", "", "plusieurs hiboux"),                          #testAccordAction2
            StructurePhrase("je", "", "", ""),                                        #testMotsParDefaut1
            StructurePhrase("", "", "être", ""),                                      #testMotsParDefaut2
            "?",                                                                                        #testChoixPonctuation1
            ".",                                                                                        #testChoixPonctuation2
            "ça va",                                                                                    #testNettoyageTirets1
            "arc-en-ciel",                                                                              #testNettoyageTirets2
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
        self.testAction2()
        self.testTemps1()
        self.testTemps2()
        self.testTemps3()
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
        self.testChoixDeterminant1()
        self.testChoixDeterminant2()
        self.testChoixDeterminant3()
        self.testChoixDeterminant4()
        self.testAccordAction1()
        self.testAccordAction2()
        self.testMotsParDefauts1()
        self.testMotsParDefauts2()
        self.testChoixPonctuation1()
        self.testChoixPonctuation2()
        self.testNettoyageTirets1()
        self.testNettoyageTirets2()


    # verifie que l'on est bien capable d'identifier le verbe de la phrase
    def testVerbe1(self):

        phrase = ["hier","cinéma","moi","aller"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append("Test verbe 1 - Obtenu : '" + structurePhrase.verbe.texte +"' | attendu : '" + self.resultatsAttendus[self.nbTests].verbe.texte +"'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le fait qu'il n'y a pas de verbe
    def testVerbe2(self):

        phrase = ["lui", "son", "ami"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test verbe 2 - Obtenu : '" + structurePhrase.verbe.texte + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests].verbe.texte + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier l'adverbe de la phrase
    def testAdverbe1(self):

        phrase = ["toi", "signer", "lentement"]
        structurePhrase = StructurePhrase()
        structurePhrase.adverbe.identifierAdverbe(phrase)

        if structurePhrase.adverbe == self.resultatsAttendus[self.nbTests].adverbe :
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append("Test adverbe 1 - Obtenu : '" + str(structurePhrase.adverbe.texte) +"' | attendu : '" + str(self.resultatsAttendus[self.nbTests].adverbe.texte) +"'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le sujet de la phrase
    def testSujet1(self):

        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = StructurePhrase()
        structurePhrase.sujet.identifierSujet(phrase)

        if structurePhrase.sujet == self.resultatsAttendus[self.nbTests].sujet:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test sujet 1 - Obtenu : '" + structurePhrase.sujet.texte + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].sujet.texte + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le sujet de la phrase quand deux pronoms
    def testSujet2(self):

        phrase = ["lui", "connaitre", "moi"]
        structurePhrase = StructurePhrase()
        structurePhrase.sujet.identifierSujet(phrase)

        if structurePhrase.sujet == self.resultatsAttendus[self.nbTests].sujet:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test sujet 2 - Obtenu : '" + structurePhrase.sujet.texte + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].sujet.texte + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier le complément de la phrase
    def testAction1(self):

        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = StructurePhrase()
        structurePhrase.identifierAction(phrase)

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test action 1 - Obtenu : '" + structurePhrase.action + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].action + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on est bien capable d'identifier la preposition de la phrase
    def testAction2(self):

        phrase = ["avec", "Bob", "travailler"]
        structurePhrase = StructurePhrase()
        structurePhrase.identifierAction(phrase)

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test action 2 - Obtenu : '" + structurePhrase.action + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].action + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on identifie bien le marqueur temporel et le temps de cette phrase (et on laisse le marqueur car indispensable)
    def testTemps1(self):

        phrase = ["lui", "partir", "récemment", "lui"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)

        if structurePhrase.marqueurTemporel == self.resultatsAttendus[self.nbTests].marqueurTemporel:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test temps 1 - Obtenu : '" + structurePhrase.marqueurTemporel.texte + " "
                + structurePhrase.marqueurTemporel.tempsConjug + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].marqueurTemporel.texte + " "
                + self.resultatsAttendus[self.nbTests].marqueurTemporel.tempsConjug + "'")

        self.nbTests = self.nbTests + 1  # verifie que l'on identifie bien le temps de cette phrase (et on laisse le marqueur car indispensable)


    # verifie que l'on identifie bien le temps de cette phrase (et on retire le marqueur car dispensable)
    def testTemps2(self):

        phrase = ["moi", "voiture", "acheter", "fini"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)

        if structurePhrase.marqueurTemporel == self.resultatsAttendus[self.nbTests].marqueurTemporel:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test temps 2 - Obtenu : '" + structurePhrase.marqueurTemporel.texte + " "
                + structurePhrase.marqueurTemporel.tempsConjug + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].marqueurTemporel.texte + " "
                + self.resultatsAttendus[self.nbTests].marqueurTemporel.tempsConjug + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on identifie bien le temps de cette phrase (marqueur temporel double)
    def testTemps3(self):

        phrase = ["moi", "voiture", "acheter", "jeudi", "dernier"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)

        if structurePhrase.marqueurTemporel == self.resultatsAttendus[self.nbTests].marqueurTemporel:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test temps 3 - Obtenu : '" + structurePhrase.marqueurTemporel.texte + " "
                + structurePhrase.marqueurTemporel.tempsConjug + "' | attendu : '" + self.resultatsAttendus[
                    self.nbTests].marqueurTemporel.texte + " "
                + self.resultatsAttendus[self.nbTests].marqueurTemporel.tempsConjug + "'")

        self.nbTests = self.nbTests + 1


    # verifie que tous les termes et le temps sont bien reconnus dans une phrase simple
    def testStructPhrase1(self):
        phrase = ["hier", "cinéma", "moi", "aller"]
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.adverbe.identifierAdverbe(phrase)
        phrase = structurePhrase.sujet.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)
        structurePhrase.identifierMotsParDefaut()

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
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.adverbe.identifierAdverbe(phrase)
        phrase = structurePhrase.sujet.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)
        structurePhrase.identifierMotsParDefaut()

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
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.adverbe.identifierAdverbe(phrase)
        phrase = structurePhrase.sujet.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)
        structurePhrase.identifierMotsParDefaut()

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
        structurePhrase = StructurePhrase()
        phrase = structurePhrase.verbe.identifierVerbe(phrase)
        phrase = structurePhrase.marqueurTemporel.identifierMarqueurTemporel(phrase)
        phrase = structurePhrase.adverbe.identifierAdverbe(phrase)
        phrase = structurePhrase.sujet.identifierSujet(phrase)
        phrase = structurePhrase.identifierAction(phrase)
        structurePhrase.identifierMotsParDefaut()

        if structurePhrase == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test struct phrase 4 - Obtenu : '" + str(structurePhrase) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests]) + "'")

        self.nbTests = self.nbTests + 1


    # verifie que l'on identifie lq premiere personne pour la conj
    def testIdentificationPersConj1(self):

        structurePhrase = StructurePhrase("lui", "", "aller", "cinéma")
        structurePhrase.sujet.identifierPersConjug()

        if structurePhrase.sujet.persConjug == self.resultatsAttendus[self.nbTests].sujet.persConjug:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test identif pers conj 1 - Obtenu : '" + str(structurePhrase.sujet.persConjug) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].sujet.persConjug) + "'")

        self.nbTests = self.nbTests + 1


    # verifie si l'on est capable de conjuguer verbe au present 1p sg
    def testConj1(self):

        structurePhrase = StructurePhrase("je", "", "aller", "cinéma")
        structurePhrase.verbe.conjuguerVerbe(structurePhrase.marqueurTemporel.tempsConjug, structurePhrase.sujet, structurePhrase.pronom_devant_verbe)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test conj 1 - Obtenu : '" + structurePhrase.verbe.texte + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests].verbe.texte + "'")

        self.nbTests = self.nbTests + 1


    # verifie si l'on est capable de conjuguer verbe au passé composé 1p sg
    def testConj2(self):

        structurePhrase = StructurePhrase("je", "", "aller", "cinéma", "hier", "", 1, "passé-composé")
        structurePhrase.verbe.conjuguerVerbe(structurePhrase.marqueurTemporel.tempsConjug, structurePhrase.sujet, structurePhrase.pronom_devant_verbe)

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test conj 2 - Obtenu : '" + structurePhrase.verbe.texte + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests].verbe.texte + "'")

        self.nbTests = self.nbTests + 1


    # test si la negation est bien identifiee (negation avec seulement ne devant verbe)
    def testNegation1(self):

        phrase = ["rien"]
        structurePhrase = StructurePhrase("il", "", "faire")
        structurePhrase.marqueursNegation.identifierMarqueursNegation(phrase)

        if structurePhrase.marqueursNegation == self.resultatsAttendus[self.nbTests].marqueursNegation:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test negation 1 - Obtenu : '" + structurePhrase.marqueursNegation.marqueur1 + " " + structurePhrase.marqueursNegation.marqueur2
                + "' | attendu : '" + self.resultatsAttendus[self.nbTests].marqueursNegation.marqueur1 + " "
                + self.resultatsAttendus[self.nbTests].marqueursNegation.marqueur2 + "'")

        self.nbTests = self.nbTests + 1


    # test si la negation est bien identifiee (ne + pas)
    def testNegation2(self):

        phrase = ["non"]
        structurePhrase = StructurePhrase("je", "", "être", "d'accord")
        structurePhrase.marqueursNegation.identifierMarqueursNegation(phrase)

        if structurePhrase.marqueursNegation == self.resultatsAttendus[self.nbTests].marqueursNegation:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test negation 2 - Obtenu : '" + structurePhrase.marqueursNegation.marqueur1 + " " + structurePhrase.marqueursNegation.marqueur2
                + "' | attendu : '" + self.resultatsAttendus[self.nbTests].marqueursNegation.marqueur1 + " "
                + self.resultatsAttendus[self.nbTests].marqueursNegation.marqueur2 + "'")

        self.nbTests = self.nbTests + 1


    def testPronomDevantVerbe(self):

        phrase = ["toi"]
        structurePhrase = StructurePhrase("je", "", "appeller")
        phrase = structurePhrase.identifierAction(phrase)

        if structurePhrase.pronom_devant_verbe == self.resultatsAttendus[self.nbTests].pronom_devant_verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test pronom devant verbe - Obtenu : '" + str(structurePhrase.pronom_devant_verbe) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].pronom_devant_verbe) + "'")

        self.nbTests = self.nbTests + 1


    # test choix determinant simple (mettre une dvant voiture)
    def testChoixDeterminant1(self):

        structurePhrase = StructurePhrase("j'", "", "acheter", "voiture")
        structurePhrase.choisirDeterminantAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix determinant 1 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1


    # test choix determinant "à un = au"
    def testChoixDeterminant2(self):

        structurePhrase = StructurePhrase("je", "", "aller", "cinéma", "hier")
        structurePhrase.choisirDeterminantAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix determinant 2 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1

    # test choix determinant: si pronom possessif  pas de determinant a ajouter
    def testChoixDeterminant3(self):

        structurePhrase = StructurePhrase("il", "", "être", "son ami")
        structurePhrase.choisirDeterminantAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix determinant 3 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1


    # test choix determinant si "il est entendant" (pas d'ajout de determinant meme si entendant peut etre un nom)
    def testChoixDeterminant4(self):

        structurePhrase = StructurePhrase("il", "", "être", "entendant")
        structurePhrase.choisirDeterminantAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix determinant 4 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1


    # test si on est capable d'accorder l'action en nombre (identifier nombre + mettre s)
    def testAccordAction1(self):

        structurePhrase = StructurePhrase("", "", "", "sept voiture")
        structurePhrase.accorderAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test accord action 1 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1


    # test si on est capable d'accorder l'action en nombre (identifier quantificateur + mettre x)
    def testAccordAction2(self):

        structurePhrase = StructurePhrase("", "", "", "plusieurs hibou")
        structurePhrase.accorderAction()

        if structurePhrase.action == self.resultatsAttendus[self.nbTests].action:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test accord action 2 - Obtenu : '" + str(structurePhrase.action) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].action) + "'")

        self.nbTests = self.nbTests + 1


    # test si pas de sujet mais présence d'un verbe, sujet = "je"
    def testMotsParDefauts1(self):

        structurePhrase = StructurePhrase("", "", "travailler", "avec Bob")
        structurePhrase.identifierMotsParDefaut()

        if structurePhrase.sujet == self.resultatsAttendus[self.nbTests].sujet:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix mot defaut 1 - Obtenu : '" + str(structurePhrase.sujet) + "' | attendu : '" +
                str(self.resultatsAttendus[self.nbTests].sujet) + "'")

        self.nbTests = self.nbTests + 1


    # test si pas de verbe mais présence d'un sujet, verbe = "être"
    def testMotsParDefauts2(self):

        structurePhrase = StructurePhrase("il", "", "", "son ami")
        structurePhrase.identifierMotsParDefaut()

        if structurePhrase.verbe == self.resultatsAttendus[self.nbTests].verbe:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix mot defaut 2 - Obtenu : '" + structurePhrase.verbe.texte + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests].verbe.texte + "'")

        self.nbTests = self.nbTests + 1


    # test si reconnait mot interrogatif, on met ? en ponctuation
    def testChoixPonctuation1(self):

        phrase = ["faire", "quoi", "vous"]
        structurePhrase = StructurePhrase()
        ponctuation = structurePhrase.determinerPonctuation(" ".join(phrase))

        if ponctuation == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix ponctuation 1 - Obtenu : '" + ponctuation + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1


    # test si pas de mot necessitant une ponctuation particulière, on met un "."
    def testChoixPonctuation2(self):

        phrase = ["lui", "a-lui", "ami"]
        structurePhrase = StructurePhrase()
        ponctuation = structurePhrase.determinerPonctuation(" ".join(phrase))

        if ponctuation == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test choix ponctuation 2 - Obtenu : '" + ponctuation + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1

    # test nettoyage tirets: la phrase comporte un mot composé de la lsf qui n'a pas de tiret en francais.
    # Il faut le retirer.
    def testNettoyageTirets1(self):

        phrase = "ça-va"
        structurePhrase = StructurePhrase()
        phraseTraduite = structurePhrase.nettoyerTirets(phrase)

        if phraseTraduite == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test nettoyage tirets 1 - Obtenu : '" + phraseTraduite + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1

    # test nettoyage tirets: la phrase comporte un mot qui a des tirets en français
    def testNettoyageTirets2(self):

        phrase = "arc-en-ciel"
        structurePhrase = StructurePhrase()
        phraseTraduite = structurePhrase.nettoyerTirets(phrase)

        if phraseTraduite == self.resultatsAttendus[self.nbTests]:
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append(
                "Test nettoyage tirets 2 - Obtenu : '" + phraseTraduite + "' | attendu : '" +
                self.resultatsAttendus[self.nbTests] + "'")

        self.nbTests = self.nbTests + 1

    # trace
    # print(structurePhrase.toStringDebug())
    # print(self.resultatsAttendus[self.nbTests].toStringDebug())