
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

class Warlord(Defender):
  def __init__(self, health = 100, attack = 4):
    super().__init__(health, attack)
    self.defense = 2


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.health = 50
      self.attack = 1



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
    flag = True
    for _ in range(amount):
        # i = kind_of_unit()
      if not isinstance(kind_of_unit(), Warlord) and flag or not isinstance(kind_of_unit(), Warlord) and not flag:
        self.units.append(kind_of_unit())
      elif isinstance(kind_of_unit(), Warlord) and flag:
        flag = False
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

  def clean_warlord(self):
    #unit = [type(x) for x in self.units]
    #count = 0
    unit = []
    # for x in self.units:
    [unit.append(x) for x in self.units if x not in unit]
    return unit
  
  def move_units(self):
    # self.clean_warlord()
    for x in self.units:

      if isinstance(x,Warlord):

        # self.units.sort(key=lambda unit: type(unit) != Lancer and type(unit)!= Healer and type(unit) != Warlord, reverse = True)
        # self.units.sort(key=lambda unit: type(unit) == Lancer, reverse=True)
        # self.units[1:] = sorted(self.units[1:], key=lambda unit: type(unit) == Healer, reverse=True)
        # self.units.sort(key=lambda unit: isinstance(unit, Warlord))
        self.units.sort(key=lambda unit: not isinstance(unit,Lancer) and not isinstance(unit,Healer) and not isinstance(unit,Warlord), reverse = True)
        self.units.sort(key=lambda unit: isinstance(unit,Lancer) , reverse=True)
        self.units[1:] = sorted(self.units[1:], key=lambda unit: isinstance(unit,Healer), reverse=True)
        self.units.sort(key=lambda unit: isinstance(unit, Warlord))
    

class Battle():
  def fight(self, army_1, army_2):
    # army_1.move_units()
    # army_2.move_units()
    while army_1.is_alive and army_2.is_alive:

      if fight(army_1.first_unit, army_2.first_unit, army_1.next_unit, army_2.next_unit):
        army_2.delete_unit
        army_2.move_units()
      else:
        army_1.delete_unit
        army_1.move_units()
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
    

  army_1 = Army()
  army_2 = Army()

  army_1.add_units(Warrior, 2)
  army_1.add_units(Lancer, 3)
  army_1.add_units(Defender, 1)
  army_1.add_units(Warlord, 1)

  army_2.add_units(Warlord, 5)
  army_2.add_units(Vampire, 1)
  army_2.add_units(Rookie, 1)
  army_2.add_units(Knight, 1)


  army_1.units[0].equip_weapon(Sword())
  army_2.units[0].equip_weapon(Shield())
  print(army_1.units[0].health)
  print(army_2.units[0].health)
  army_1.move_units()


  print(army_1.units[0])
  print(army_1.units[1])
  print(army_1.units[2])
  print(army_1.units[3])
  print(army_1.units[4])
  print(army_1.units[5])
  print(army_1.units[6])


  print()

  army_2.move_units()

  print(army_2.units[0])
  print(army_2.units[1])
  print(army_2.units[2])
  print(army_2.units[3])

  print(army_1.units[4].health)


  battle = Battle()
  assert battle.straight_fight(army_1, army_2) == False
  
  print("Coding complete? Let's try tests!")

# from itertools import count


# arm = Army()
# arm.add_units(Warlord,3)
# arm.add_units(Knight,1)
# arm.add_units(Healer,2)
#a = ["Warlord", "Warlord", "Healer", "Lancer", "Knight"]
# new = []
# count = 0
# for x in arm.units:
# print(arm.get_units())
#print(new)
  # if type(x) == Warlord:
  #   count+=1
  #   print(arm.units[type(x) == Warlord])
  # if count > 1:
  #   [new.append()]



# [new.append(x) for x in arm.add_units if arm not in new]
# print(new)

# b = ["Warlord", "Healer", "Lancer", "Knight"]
# c = ["Warlord", "Lancer",  "Healer", "Knight", "Healer",]
# d = ["Warlord", "Lancer",  "Healer", "Knight", "Healer",]
# # Ставим всех атакующих в начало
# a.sort(key=lambda i: i not in ["Lancer", "Warlord", "Healer"], reverse=True)
# # Ставим копейщиков в начало
# b.sort(key=lambda i: i == "Lancer", reverse=True)
# #c[1:].sort(c[1:], key=lambda i: i == "Healer", reverse=True)
# # Ставим лекарей вторыми и далее
# c[1:] = sorted(c[1:],key=lambda i: i == "Healer", reverse=True)
# # Ставим лордов в конец
# d.sort(key=lambda i: i == "Warlord")
# print(a)
# print(b)
# print(c)
# print(d)

# e = ["Warlord", "Lancer",  "Healer", "Knight", "Healer",]

# e.sort(key=lambda i: i not in ["Lancer", "Warlord", "Healer"], reverse=True)
# # Ставим копейщиков в начало
# e.sort(key=lambda i: i == "Lancer", reverse=True)
# #c[1:].sort(c[1:], key=lambda i: i == "Healer", reverse=True)
# # Ставим лекарей вторыми и далее
# e[1:] = sorted(e[1:],key=lambda i: i == "Healer", reverse=True)
# # Ставим лордов в конец
# e.sort(key=lambda i: i == "Warlord")
# print(e)