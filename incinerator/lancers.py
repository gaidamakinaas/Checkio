
class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
    self.is_alive = True 
    self.defense = 0
    self.vampirisim = 0


class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)
    self.defense = 0
    self.is_alive = True 
    self.vampirisim = 0


class Defender(Warrior):
    def __init__(self, health = 60, attack = 3):
      super().__init__(health, attack)
      self.defense = 2
      self.is_alive = True 
      self.vampirisim = 0

class Vampire(Warrior):
  def __init__(self, health = 40, attack = 4):
      super().__init__(health, attack)
      self.defense = 0
      self.vampirisim = 50
      self.is_alive = True 

class Lancer(Warrior):
  def __init__(self, health = 50, attack = 6):
      super().__init__(health, attack)
      self.defense = 0
      self.vampirisim = 0
      self.is_alive = True



  
# for testing, not for game 
class Rookie(Warrior):
  def __init__(self, health=50, attack = 1):
    super().__init__(health, attack)
    self.defense = 0


class Army():
  def __init__(self):
    self.kind_of_unit = [] 
    # self.number = 0

  def add_units(self, kind_of_units, number):
    for i in range(number):
      i = kind_of_units()
      self.kind_of_unit.append(i)
    # return self.kind_of_unit

  # just for self-checking
  def get_units(self):
    for i in range(0, len(self.kind_of_unit)):
      print(self.kind_of_unit[i])

  # def length(self):
  #   return len(self.kind_of_unit)

  def __getitem__(self, item):
    return self.kind_of_unit[item]
     

class Battle():
  # def __init__(self, first_army, second_army):
  #     self.fisrt_army = first_army
  #     self.second_army = second_army
  
  def fight(self, first_army, second_army):
    # индексы, по которым будем проходиться в цикле (количество человек в обоих армиях)
    num_unit1 = len(first_army.kind_of_unit) - 1
    num_unit2 = len(second_army.kind_of_unit) -1 
    while num_unit1 >= 0 and num_unit2 >= 0:
      if fight(first_army.kind_of_unit[num_unit1], second_army.kind_of_unit[num_unit2]) == True:
        second_army.kind_of_unit.remove(second_army.kind_of_unit[num_unit2])
        num_unit2 -= 1
      else:
        first_army.kind_of_unit.remove(first_army.kind_of_unit[num_unit1])
        num_unit1 -= 1
    return len(first_army.kind_of_unit) > 0  

  

def health_update(unit_1, unit_2, unit_next_army = None):
  # урон от первого второму юниту
  if unit_1.attack > unit_2.defense:
    loss = unit_1.attack - unit_2.defense
  else:
    loss = 0
  unit_2.health -=loss

  # урон от второго юнита первому
  if isinstance(unit_1, Vampire):
    unit_1.health += loss * unit_1.vampirisim/100
  # если есть еще третий воин, он теряет здоровье от Lancer
  if isinstance(unit_1, Lancer) and unit_next_army is not None and len(unit_next_army)>1:
    unit_next_army[1].health -= 0.5*loss

  return unit_1.health, unit_2.health, unit_next_army


# fight between two units
def fight(unit_1, unit_2, army_1 = None, army_2 = None):
    # пока здоровье первого больше 0, битва продолжается 
  while unit_1.health > 0 and unit_2.health > 0:
    unit_1.health, unit_2.health, army_2 = health_update(unit_1, unit_2, army_2)
    #print(f" 1 {unit_1.health, unit_2.health}")
    if unit_2.health <= 0:
      unit_2.is_alive = False
      
      break
    # unit_1.health = health_update(unit_1, unit_2)
    unit_2.health, unit_1.health, army_1 = health_update(unit_2, unit_1, army_1)
   # print(f"2 {unit_2.health, unit_1.health}")
    if unit_1.health <= 0:
      unit_1.is_alive = False
      
      break

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

    # #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")