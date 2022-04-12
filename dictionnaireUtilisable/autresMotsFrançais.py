class PronomsFR:
  def __init__(self):
    self.personnels = ["je", "tu", ["il", "elle"], "nous", "vous", ["ils", "elles"]]
    self.possessifsMasculin = ["mon", "ton", "son", "notre", "votre", "leur"]
    self.possessifsFeminin = ["ma", "ta", "sa", "notre", "votre", "leur"]
    self.possessifsPluriel = ["mes", "tes", "ses", "nos", "vos", "leurs"]

pronoms = PronomsFR()

print(pronoms.personnels)