class PronomsLSF:
  def __init__(self):
    self.personnels = ["moi", "toi", "lui", "nous", "vous", "eux"]
    self.possessifs = ["a-moi", "a-toi", "a-lui", "a-nous", "a-vous", "a-eux"]

class MarqueurTemporel:
  def __init__(self, mot, isIndispensable, tempsAssocie):
    self.mot = mot
    self.isIndispanesable = isIndispensable
    self.tempsAssocie = tempsAssocie

  def __str__(self):
    return self.marqueur + " (indispensable:" +str(self.isIndispanesable)+") : " + self.tempsAssocie

class MarqueursTemporels:
  def __init__(self):
    self.liste = [
      MarqueurTemporel("hier", True, "passé composé"),
      MarqueurTemporel("demain", True, "futur"),
      MarqueurTemporel("fini", False, "passé composé"),
      MarqueurTemporel("récemment", True, "passé composé")
    ]

  def __str__(self):
    res = "\n"
    for marqueur in self.liste:
      res += str(marqueur) + "\n"
    return res