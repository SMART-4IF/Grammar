# import unittest
class TestsUnitaires:

    def __init__(self):
        self.nbTests = 0
        self.nbTestsReussis = 0
        self.messagesEchecs = []

    def __str__(self):
        res = str(self.nbTestsReussis) + " / " + str(self.nbTests) + " tests passés avec succès. \n"
        res += "-----------------------------------------------------------------------------\n"
        res += "|                           Description des echecs                          |\n"
        res += "-----------------------------------------------------------------------------\n"
        for message in self.messagesEchecs:
            res += "| " + message + "\n"
        res += "-----------------------------------------------------------------------------\n"
        return res

    def test1(self):
        self.nbTests = self.nbTests + 1
        var1 = 3
        var2 = 2
        if var1 == var2 :
            self.nbTestsReussis = self.nbTestsReussis + 1
        else:
            self.messagesEchecs.append("Tests 1: " + str(var1) +" différent de " + str(var2))