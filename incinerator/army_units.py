# абстрактная фабрика
class Army:
    def __init__(self) -> None:
      # названия для юнитов у каждой армии свои
        self.occupation = ""
        self.name = ""
        self.place = ""

    def train_swordsman(self, name):
        pass

    def train_lancer(self, name):
        pass

    def train_archer(self, name):
        pass


    # def train_swordsman (self, name):
    #   #self.swordsman_units = []
    #   new_swordsman = Swordsman(name)
    #   #self.swordsman_units.append(new_swordsman)
    #   return new_swordsman

    # def train_lancer(self, name):
    #   #self.lancer_units = []
    #   new_lancer = Lancer(name)
    #   #self.lancer_units.append(new_lancer)

    # def train_archer(self, name):
    #  # self.archer_units = []
    #   new_archer = Archer(name)
    #   #self.archer_units.append(new_archer)
    #   return new_archer 

# абстрактный продукт
class Soldier:
    def __init__(self, occupation, place, name):
        self.occupation = occupation
        self.name = name
        self.place = place

    def introduce(self):
        pass

# конкретный продукт
class Swordsman(Soldier):
    # def __init__(self, name) -> None:
    #   self.name = name


    def introduce(self):
        return f'{self.occupation} {self.name}, {self.place} swordsman'


# конкретный продукт
class Lancer(Soldier):
    # def __init__(self, name) -> None:
    #   self.name = name


    def introduce(self):
        return f'{self.occupation} {self.name}, {self.place} lancer'


# конкретный продукт
class Archer(Soldier):
    # def __init__(self, name) -> None:
    #   self.name = name


    def introduce(self):
        return f'{self.occupation} {self.name}, {self.place} archer'

# конкретная фабрика
class AsianArmy(Army):
    def __init__(self) -> None:
        super().__init__()

        # self.swordsman = "Knight"
        # self.lancer = "Raubritter"
        # self.archer = "Ranger"

        # self.units = {'swordsman' : "Samurai", 'lancer': "Ronin", 'archer': "Shinobi"}
        # self.place = 'asian'

        self.place = 'Asian'

    def train_swordsman(self, name):
        return Swordsman('Samurai', self.place , name)

    def train_lancer(self, name):
        return Lancer('Ronin', self.place , name)

    def train_archer(self, name):
        return Archer('Shinobi', self.place , name)



# конкретная фабрика
class EuropeanArmy(Army):
    def __init__(self) -> None:
        super().__init__()
        # self.swordsman = "Samurai"
        # self.lancer = "Ronin"
        # self.archer = "Shinobi"
        self.place  = 'European'
        
        # self.units = {'swordsman' :"Knight", 'lancer': "Raubritter", 'archer': "Ranger"}
        

    def train_swordsman(self, name):
        return Swordsman('Knight', self.place , name)

    def train_lancer(self, name):
        return Lancer('Raubritter', self.place , name)

    def train_archer(self, name):
        return Archer('Ranger', self.place , name)



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
