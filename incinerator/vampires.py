
class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
    self.is_alive = True 
    self.defense = 0
    self.vampirisim = 0

  def suffer(self, damage):
    self.health -= damage

  def hit(self, enemy):
    enemy.suffer(self.attack)


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

  def hit(self, enemy):
    super().hit(enemy)
    self.health += self.vampirism/100

  

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

    # # пока есть, кому воевать
    # while num_unit1  >= 0 and num_unit2 >= 0:
    #   # пока есть здоровье у дуэлянтов, первый наносит урон второму
    #   while first_army.kind_of_unit[num_unit1].health > 0 and second_army.kind_of_unit[num_unit2].health > 0:
    #     second_army.kind_of_unit[num_unit2].health = health_update(second_army.kind_of_unit[num_unit2], first_army.kind_of_unit[num_unit1])
    #     if second_army.kind_of_unit[num_unit2].health > 0:
    #       first_army.kind_of_unit[num_unit1].health = health_update(first_army.kind_of_unit[num_unit1],second_army.kind_of_unit[num_unit2])
    #   # когда кто-то умер, он соответственно своей армии убирается из списка воинов
    #   if first_army.kind_of_unit[num_unit1].health > 0:
    #     second_army.kind_of_unit.pop()
    #     num_unit2 -= 1

    #   else:
    #     first_army.kind_of_unit.pop()
    #     num_unit1 -= 1
    #  # вернет True, если в первой армии остались живые
    # return len(first_army.kind_of_unit) > 0 

def health_update(unit_1, unit_2):
  if unit_1.attack > unit_2.defense:
    loss = unit_1.attack - unit_2.defense
  else:
    loss = 0
  unit_2.health -= loss
  unit_1.health += loss * unit_1.vampirisim/100
  return unit_1.health, unit_2.health

# fight between two units
def fight(unit_1, unit_2):
    # пока здоровье первого больше 0, битва продолжается 
  while unit_1.health > 0 and unit_2.health > 0:
    unit_1.health, unit_2.health = health_update(unit_1, unit_2)
    #print(f" 1 {unit_1.health, unit_2.health}")
    if unit_2.health <= 0:
      unit_2.is_alive = False
      
      break
    # unit_1.health = health_update(unit_1, unit_2)
    unit_2.health, unit_1.health = health_update(unit_2, unit_1)
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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")