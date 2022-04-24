class PronomsFR:
  def __init__(self):
    self.personnels = ["je", "tu", "il", "nous", "vous", "ils"]
    self.possessifsMasculin = ["mon", "ton", "son", "notre", "votre", "leur"]
    self.possessifsFeminin = ["ma", "ta", "sa", "notre", "votre", "leur"]
    self.possessifsPluriel = ["mes", "tes", "ses", "nos", "vos", "leurs"]
    self.pronoms_devant_verbe = ["me", "te", "le","nous", "vous","les" ]
    self.pronoms_devant_verbe_voyelle = ["m'", "t'", "l'","nous", "vous","les" ]

class Prepositions:
  def __init__(self):
    self.liste = ["avec", "pour", "sur", "dans"]


class Pluriel:
  def __init__(self):
    self.nombres = ["deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
    self.quantificateurs = ["plusieurs"]
    self.irreguliersPluriels = ["hibou", "caillou", "chou", "bijou", "genou", "joujou", "pou"]

class Elision:
  def __init__(self):
    self.listeElisionsVoyelles = ["ne", "je", "le", "la", "me", "te"]
    self.listeElisionSonS = ["ce"]
