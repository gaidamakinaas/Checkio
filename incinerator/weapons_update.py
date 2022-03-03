class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
    self.max_health = health
      
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

  def equip_weapon(self, weapon):
    self.max_health += weapon.health
    self.health = max(0, self.max_health)
    
    if self.attack > 0:
      self.attack = max(0, self.attack+ weapon.attack)
  

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

  def equip_weapon(self, weapon):
    super().equip_weapon(weapon)
    self.defense = max(0, self.defense+weapon.defense)


class Vampire(Warrior):
  def __init__(self, health = 40, attack = 4):
      super().__init__(health, attack)
      self.vampirism = 50

  def hit(self, *enemy):
    super().hit(*enemy)
    self.health += enemy[0].loss(self.attack)*self.vampirism/100

  def equip_weapon(self, weapon):
    super().equip_weapon(weapon)
    self.vampirism = max(0, self.vampirism+weapon.vampirism)

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
    self.heal_power = 2

  def heal(self, mate):
    mate.health = min(mate.health + self.heal_power, type(mate)().health)
  
  def equip_weapon(self, weapon):
    super().equip_weapon(weapon)
    self.heal_power  = max(0, self.heal_power+weapon.heal_power)


class Weapon():
  def __init__(self, health = 0, attack = 0, defense = 0, vampirism = 0, heal_power = 0):
    self.health = health
    self.attack = attack
    self.defense = defense
    self.vampirism = vampirism
    self.heal_power = heal_power

class Sword(Weapon):
  def __init__(self):
    super().__init__(health = 5, attack = 2)

class Shield(Weapon):
  def __init__(self):
    super().__init__(health = 20, attack = -1, defense =2)

class GreatAxe(Weapon):
  def __init__(self):
    super().__init__(health = -15, attack = 5, defense = -2, vampirism = 10)

class Katana(Weapon):
  def __init__(self):
    super().__init__(health = -20, attack = 6, defense = -5, vampirism = 50) 

class MagicWand(Weapon):
  def __init__(self):
    super().__init__(health = 30, attack = 3, heal_power=3) 
    

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
