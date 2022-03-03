
class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.max_health = health
    self.attack = attack
    self.is_alive = True 
    self.defense = 0
    self.vampirism = 0
    self.heal_power = 0

  def heal(self, other):
    other.health = min(other.health + self.heal_power, type(other)().health)
  
  def equip_weapon(self, weapon):
    self.health = self.health + weapon.health
    self.max_health =  self.health + weapon.health
    if self.attack > 0:
      self.attack +=  weapon.attack
    if self.defense > 0:
      self.defense += weapon.defense
    if self.vampirism > 0:
      self.vampirism += weapon.vampirism
    if self.heal_power > 0:
      self.heal_power = self.heal_power + weapon.heal_power
    # if self.attack > 0:
    #   self.attack = max(0, self.attack + weapon.attack)
    # if self.defense > 0:
    #   self.defense = max(0, self.defense + weapon.defense)
    # if self.vampirism > 0:
    #   self.vampirism =  max(0, self.vampirism + weapon.vampirism)
    # if self.heal_power > 0:
    #   self.heal_power = self.heal_power + weapon.heal_power

    

class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)
    self.defense = 0
    self.is_alive = True 
    self.vampirism = 0
    self.heal_power = 0


class Defender(Warrior):
    def __init__(self, health = 60, attack = 3):
      super().__init__(health, attack)
      self.defense = 2
      self.is_alive = True 
      self.vampirism = 0
      self.heal_power = 0

class Vampire(Warrior):
  def __init__(self, health = 40, attack = 4):
      super().__init__(health, attack)
      self.defense = 0
      self.vampirism = 50
      self.is_alive = True
      self.heal_power = 0

class Lancer(Warrior):
  def __init__(self, health = 50, attack = 6):
      super().__init__(health, attack)
      self.defense = 0
      self.vampirism = 0
      self.is_alive = True
      self.heal_power = 0

class Healer(Warrior):
  def __init__(self, health = 60, attack = 0):
    super().__init__(health, attack)
    self.defense = 0
    self.vampirism = 0
    self.is_alive = True
    self.heal_power = 2

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

# for testing, not for game 
class Rookie(Warrior):
  def __init__(self, health=50, attack = 1):
    super().__init__(health, attack)
    self.defense = 0


class Army():
  def __init__(self):
    self.units = [] 
    # self.number = 0

  def add_units(self, kind_of_units, number):
    for i in range(number):
      i = kind_of_units()
      self.units.append(i)
    # return self.kind_of_unit

  # just for self-checking
  def get_units(self):
    for i in range(0, len(self.units)):
      print(self.units[i])

  # def length(self):
  #   return len(self.kind_of_unit)

  def __getitem__(self, item):
    return self.units[item]


     

class Battle():
  # def __init__(self, first_army, second_army):
  #     self.fisrt_army = first_army
  #     self.second_army = second_army
  
  def fight(self, first_army, second_army):
    # индексы, по которым будем проходиться в цикле (количество человек в обоих армиях)
    # num_unit1 = len(first_army.kind_of_unit) - 1
    # num_unit2 = len(second_army.kind_of_unit) -1 
    
    while len(first_army.units) > 0 and len(second_army.units):

      if fight(first_army.units[0], second_army.units[0],first_army.units,second_army.units):
        second_army.units.remove(second_army.units[0])
        #num_unit2 -= 1
        #print(f" number of unit 2 {num_unit2 }")
      else:
        first_army.units.remove(first_army.units[0])
       # num_unit1 -= 1
        #print(f" number of unit 1 {num_unit1}")
    return len(first_army.units) > 0 
  
  def straight_fight(self, first_army, second_army):
    while len(first_army.units) > 0 and len(second_army.units):
      for unit in zip(first_army.units, second_army.units):
        fight(unit[0], unit[1])
      first_army.units = [unit for unit in first_army.units if unit.is_alive]
      second_army.units = [unit for unit in second_army.units if unit.is_alive]
    return len(first_army.units) > 0 



def health_update(unit_1, unit_2, unit_next_army1 = None, unit_next_army2 = None):
  # урон от первого второму юниту
  
  loss = max(0, unit_1.attack - unit_2.defense)
 
   
  # if unit_1.attack > unit_2.defense:
  #   loss = unit_1.attack - unit_2.defense
  # else:
  #   loss = 0
  unit_2.health -=loss

  
  if isinstance(unit_1, Vampire):
    unit_1.health = min(unit_1.health + int(loss * unit_1.vampirism/100), unit_1.max_health)

  # если есть еще третий воин, он теряет здоровье от Lancer
  if isinstance(unit_1, Lancer) and unit_next_army2 is not None and len(unit_next_army2)>1:
    unit_next_army2[1].health -= 0.5 * loss

  # если есть лекарь (следующий за тем, кому наносят урон), он будет лечить впереди стоящего
  #  здесь сначала нужно проверить, есть ли вообще кто-то сзади второго юнита, иначе
  #  ошибка TypeError: 'NoneType' object is not subscriptable
 
  if unit_next_army1 is not None and len(unit_next_army1)>1 and isinstance(unit_next_army1[1], Healer):
    unit_next_army1[1].heal(unit_1)

  return unit_1.health, unit_2.health, unit_next_army1, unit_next_army2


# fight between two units
def fight(unit_1, unit_2, army_1 = None, army_2 = None):
    # пока здоровье первого больше 0, битва продолжается 
  while unit_1.health > 0 and unit_2.health > 0:
    unit_1.health, unit_2.health, army_1, army_2 = health_update(unit_1, unit_2, army_1, army_2)
   # print(f" 1 {unit_1.health, unit_2.health}")
    if unit_2.health <= 0:
      unit_2.is_alive = False
      
      break

    unit_2.health, unit_1.health, army_2, army_1 = health_update(unit_2, unit_1, army_2, army_1)
   # print(f"2 {unit_2.health, unit_1.health}")
    if unit_1.health <= 0:
      unit_1.is_alive = False
      
      break

  return unit_1.is_alive
  

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
  ogre = Warrior()
  lancelot = Knight()
  richard = Defender()
  eric = Vampire()
  freelancer = Lancer()
  priest = Healer()

  sword = Sword()
 # print(sword.attack)
  shield = Shield()
 # print(shield.health)
  axe = GreatAxe()
 # print(axe.health)
  katana = Katana()
 # print(katana.health)
  wand = MagicWand()
  #print(wand.health)
  super_weapon = Weapon(50, 10, 5, 150, 8)


  ogre.equip_weapon(sword)
  ogre.equip_weapon(shield)
  ogre.equip_weapon(super_weapon)
  lancelot.equip_weapon(super_weapon)
  richard.equip_weapon(shield)
  eric.equip_weapon(super_weapon)
  
  freelancer.equip_weapon(axe)
 # print(freelancer.health)
  freelancer.equip_weapon(katana)
  #print(freelancer.health)
  
  priest.equip_weapon(wand)
 # print(priest.heal_power)
  priest.equip_weapon(shield)
 # print(priest.attack)

  
  assert ogre.health == 125
  assert lancelot.attack == 17
  assert richard.defense == 4
  assert eric.vampirism == 200
  assert freelancer.health == 15
  
  assert priest.heal_power == 5

  assert fight(ogre, eric) == False
  assert fight(priest, richard) == False
  assert fight(lancelot, freelancer) == True

  my_army = Army()
  my_army.add_units(Knight, 1)
  my_army.add_units(Lancer, 1)

  enemy_army = Army()
  enemy_army.add_units(Vampire, 1)
  enemy_army.add_units(Healer, 1)

  my_army.units[0].equip_weapon(axe)
  my_army.units[1].equip_weapon(super_weapon)

  enemy_army.units[0].equip_weapon(katana)
  enemy_army.units[1].equip_weapon(wand)

  battle = Battle()

  assert battle.fight(my_army, enemy_army) == True

  weapon_1 = Katana()
  weapon_2 = Shield()
  my_army = Army()
  my_army.add_units(Vampire, 2)
  my_army.add_units(Rookie, 2)
  enemy_army = Army()
  enemy_army.add_units(Warrior, 1)
  enemy_army.add_units(Defender, 2)
  my_army.units[0].equip_weapon(weapon_1)
  my_army.units[1].equip_weapon(weapon_1)
  my_army.units[2].equip_weapon(weapon_2)
  enemy_army.units[0].equip_weapon(weapon_1)
  enemy_army.units[1].equip_weapon(weapon_2)
  enemy_army.units[2].equip_weapon(weapon_2)

  battle = Battle()
  assert battle.straight_fight(my_army, enemy_army) == True

  army_1 = Army()
  army_2 = Army()
  army_1.add_units(Defender, 5)
  army_1.add_units(Vampire, 6)
  army_1.add_units(Warrior, 7)
  army_2.add_units(Warrior, 6)
  army_2.add_units(Defender, 6)
  army_2.add_units(Vampire, 6)
  # battle = Battle()
  assert battle.fight(army_1, army_2) == False

  print("Coding complete? Let's try tests!")


# defense = 2
# weapon_defense = -3

# print(max(0, defense + weapon_defense))


