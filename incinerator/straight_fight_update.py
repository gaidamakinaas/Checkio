
class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
      
  @property
  def is_alive(self):
    if self.health > 0:
      return True
    else:
      return False

  def loss(self, attack):
    return attack

  def suffer(self, damage):
    self.health -= self.loss(damage)


  def heal(self, other):
    pass

  def hit(self, *enemy):
    enemy[0].suffer(self.attack)
    if isinstance(enemy[1], Healer):
      self.heal(self)


class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)


class Defender(Warrior):
  def __init__(self, health = 60, attack = 3):
    super().__init__(health, attack)
    self.defense = 2
    
  def loss(self, attack):
   # self.health -= max(0, damage - self.defense)
    return max(0, attack - self.defense)

class Vampire(Warrior):
  def __init__(self, health = 40, attack = 4):
      super().__init__(health, attack)
      self.vampirism = 50

  def hit(self, *enemy):
    super().hit(*enemy)
    self.health += enemy[0].loss(self.attack)*self.vampirism/100

class Lancer(Warrior):
  def __init__(self, health = 50, attack = 6):
      super().__init__(health, attack)

  def hit(self, *enemy):
    enemy[0].suffer(self.attack)
    if enemy[1]:
      enemy[1].suffer(self.attack*0.5)

class Healer(Warrior):
  def __init__(self, health = 60, attack = 0):
    super().__init__(health, attack)
    self.healing = 2

  def heal(self, mate):
    mate.health = min(mate.health + self.healing, type(mate)().health)
    

class Army():
  def __init__(self):
    self.units = [] 
    # self.number = 0

  def add_units(self, kind_of_unit, amount):
      for _ in range(amount):
        # i = kind_of_unit()
        self.units.append(kind_of_unit())
      
  @property
  def is_alive(self):
    return len(self.units) > 0

  @property
  def first_unit(self):
    return self.units[0]

  @property
  def delete_unit(self):
    self.units.pop(0)

  @property
  def next_unit(self):
    if len(self.units) > 1:
      return self.units[1]
    else:
      return None

  @property
  def alive_units(self):
    self.units = [u for u in self.units if u.is_alive]
    return self.units
    
  def __getitem__(self, index):
    return self.units[index]
     
class Battle():
  def fight(self, army_1, army_2):
    while army_1.is_alive and army_2.is_alive:
      if fight(army_1.first_unit, army_2.first_unit, army_1.next_unit, army_2.next_unit):
        army_2.delete_unit
      else:
        army_1.delete_unit
    return army_1.is_alive

  def straight_fight(self, army_1, army_2):
    while army_1.is_alive and army_2.is_alive:
      for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
        fight(unit_1, unit_2)
    return army_1.is_alive
       

def fight(unit_1, unit_2, unit_3 = None, unit_4 = None):
  while unit_1.is_alive and unit_2.is_alive:
    unit_1.hit(unit_2, unit_4)
    if unit_3 is not None:
      unit_3.heal(unit_1)
    if unit_2.is_alive:
      unit_2.hit(unit_1, unit_3)
    if unit_4 is not None:
      unit_4.heal(unit_2)
  return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
  chuck = Warrior()
  bruce = Warrior()
  carl = Knight()
  dave = Warrior()
  mark = Warrior()
  bob = Defender()
  mike = Knight()
  rog = Warrior()
  lancelot = Defender()
  eric = Vampire()
  adam = Vampire()
  richard = Defender()
  ogre = Warrior()
  freelancer = Lancer()
  vampire = Vampire()
  priest = Healer()

  assert fight(chuck, bruce) == True
  assert fight(dave, carl) == False
  assert chuck.is_alive == True
  assert bruce.is_alive == False
  assert carl.is_alive == True
  assert dave.is_alive == False
  assert fight(carl, mark) == False
  assert carl.is_alive == False
  assert fight(bob, mike) == False
  assert fight(lancelot, rog) == True
  assert fight(eric, richard) == False
  assert fight(ogre, adam) == True
  assert fight(freelancer, vampire) == True
  assert freelancer.is_alive == True
  assert freelancer.health == 14    
  priest.heal(freelancer)
  assert freelancer.health == 16

    #battle tests
  my_army = Army()
  my_army.add_units(Defender, 2)
  my_army.add_units(Healer, 1)
  my_army.add_units(Vampire, 2)
  my_army.add_units(Lancer, 2)
  my_army.add_units(Healer, 1)
  my_army.add_units(Warrior, 1)
    
  enemy_army = Army()
  enemy_army.add_units(Warrior, 2)
  enemy_army.add_units(Lancer, 4)
  enemy_army.add_units(Healer, 1)
  enemy_army.add_units(Defender, 2)
  enemy_army.add_units(Vampire, 3)
  enemy_army.add_units(Healer, 1)

  army_3 = Army()
  army_3.add_units(Warrior, 1)
  army_3.add_units(Lancer, 1)
  army_3.add_units(Healer, 1)
  army_3.add_units(Defender, 2)

  army_4 = Army()
  army_4.add_units(Vampire, 3)
  army_4.add_units(Warrior, 1)
  army_4.add_units(Healer, 1)
  army_4.add_units(Lancer, 2)

  army_5 = Army()
  army_5.add_units(Warrior, 10)

  army_6 = Army()
  army_6.add_units(Warrior, 6)
  army_6.add_units(Lancer, 5)
  army_1 = Army()
  army_2 = Army()
  army_1.add_units(Lancer, 7)
  army_1.add_units(Vampire, 3)
  army_1.add_units(Warrior, 4)
  army_1.add_units(Defender, 2)
  army_2.add_units(Warrior, 4)
  army_2.add_units(Defender, 4)
  army_2.add_units(Vampire, 6)
  army_2.add_units(Lancer, 4)

  battle = Battle()

  assert battle.fight(my_army, enemy_army) == False
  assert battle.fight(army_3, army_4) == True
  assert battle.straight_fight(army_5, army_6) == False
  # assert battle.straight_fight(army_1, army_2) == True
  print("Coding complete? Let's try tests!")