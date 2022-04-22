class PronomsLSF:
  def __init__(self):
    self.personnels = ["moi", "toi", "lui", "nous", "vous", "eux"]
    self.possessifs = ["a-moi", "a-toi", "a-lui", "a-nous", "a-vous", "a-eux"]

class Ponctuations:
  def __init__(self):
    self.interrogatifs = ["quoi", "et-moi", "et-toi", "et-lui", "et-nous", "et-vous", "et-eux"]

class MarqueursNegation:
  def __init__(self):
    self.simple = ["rien", "plus"]      # nécessite seulement un "ne" devant le verbe
    self.double = ["non"]               # nécessite ne devant le verbe et pas après et est supprimé

class MarqueurTemporel:
  def __init__(self, mot, tempsAssocie, isIndispensable = True):
    self.mot = mot
    self.isIndispanesable = isIndispensable
    self.tempsAssocie = tempsAssocie

  def __str__(self):
    return self.marqueur + " (indispensable:" +str(self.isIndispanesable)+") : " + self.tempsAssocie

class MarqueursTemporels:
  def __init__(self):
    self.marqueursSimples = [
      MarqueurTemporel("hier", "passé-composé"),
      MarqueurTemporel("demain", "futur-simple"),
      MarqueurTemporel("fini", "passé-composé", False),
      MarqueurTemporel("récemment", "passé-composé")
    ]

    self.marqueursDoubles = [
      MarqueurTemporel("lundi prochain", "futur-simple"),
      MarqueurTemporel("mardi prochain", "futur-simple"),
      MarqueurTemporel("mercredi prochain", "futur-simple"),
      MarqueurTemporel("jeudi prochain", "futur-simple"),
      MarqueurTemporel("vendredi prochain", "futur-simple"),
      MarqueurTemporel("samedi prochain", "futur-simple"),
      MarqueurTemporel("dimanche prochain", "futur-simple"),
      MarqueurTemporel("lundi dernier", "passé-composé"),
      MarqueurTemporel("mardi dernier", "passé-composé"),
      MarqueurTemporel("mercredi dernier", "passé-composé"),
      MarqueurTemporel("jeudi dernier", "passé-composé"),
      MarqueurTemporel("vendredi dernier", "passé-composé"),
      MarqueurTemporel("samedi dernier", "passé-composé"),
      MarqueurTemporel("dimanche dernier", "passé-composé"),
    ]

  def __str__(self):
    res = "\n"
    for marqueur in self.liste:
      res += str(marqueur) + "\n"
    return res