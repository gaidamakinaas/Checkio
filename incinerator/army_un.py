class Army:
    def __init__(self) -> None:
      # названия для юнитов у каждой армии свои
      # self.swordsman = ""
      # self.lancer = ""
      # self.archer = ""
      self.units = {}
      self.place = ""

    def train_swordsman (self, name):
     # self.swordsman_units = []
      new_swordsman = Swordsman(name)
     # self.swordsman_units.append(new_swordsman)
      return new_swordsman

    def train_lancer(self, name):
     # self.lancer_units = []
      new_lancer = Lancer(name)
     # self.lancer_units.append(new_lancer)
      return new_lancer

    def train_archer(self, name):
      #self.archer_units = []
      new_archer = Archer(name)
     # self.archer_units.append(new_archer)
      return new_archer 

class Soldier:
  def __init__(self, name) -> None:
      self.name = name
     # self.army = army

def  introduce(self):
      return f"{self.army.units[self.category]} {self.name}"

class Swordsman(Soldier):
    def __init__(self) -> None:
      super().__init__()
     # self.category = 'swordsman'


class Lancer:
    def __init__(self, name) -> None:
      self.name = name
      self.category = 'lancer'

class Archer:
    def __init__(self, name) -> None:
      self.name = name
      self.category = 'archer'

class AsianArmy(Army):
    def __init__(self) -> None:
        super().__init__()
        self.place ='asian'
        self.units = {'swordsman' :"Knight", 'lancer': "Raubritter", 'archer': "Ranger"}
        # self.swordsman = "Knight"
        # self.lancer = "Raubritter"
        # self.archer = "Ranger"
       

class EuropeanArmy(Army):
    def __init__(self) -> None:
        super().__init__()
        self.place = 'european'
        self.units = {'swordsman' : "Samurai", 'lancer': "Ronin", 'archer': "Shinobi"}
        # self.swordsman = "Samurai"
        # self.lancer = "Ronin"
        # self.archer = "Shinobi"


my_army = EuropeanArmy()

soldier_1 = my_army.train_swordsman("Jaks")

print(soldier_1.introduce())