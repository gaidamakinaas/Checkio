
class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
    self.is_alive = True 


  def suffer(self, damage):
    self.health -= damage


class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)



class Defender(Warrior):
    def __init__(self, health = 60, attack = 3):
      super().__init__(health, attack)
      self.defense = 2
    
    def suffer(self, damage):
      self.health -= max(0, damage - self.defense)


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

    # пока есть, кому воевать
    while num_unit1  >= 0 and num_unit2 >= 0:
      # пока есть здоровье у дуэлянтов, первый наносит урон второму
      while first_army.kind_of_unit[num_unit1].health > 0 and second_army.kind_of_unit[num_unit2].health > 0:
        second_army.kind_of_unit[num_unit2].health = health_update(second_army.kind_of_unit[num_unit2], first_army.kind_of_unit[num_unit1])
        if second_army.kind_of_unit[num_unit2].health > 0:
          first_army.kind_of_unit[num_unit1].health = health_update(first_army.kind_of_unit[num_unit1],second_army.kind_of_unit[num_unit2])
      #   if  isinstance(second_army.kind_of_unit[num_unit2], Defender):
      #    # count +=1
      #     second_army.kind_of_unit[num_unit2].health -= (first_army.kind_of_unit[num_unit1].attack - second_army.kind_of_unit[num_unit2].defense)
      #    # print(f" Здоровье 2 защитника {second_army.kind_of_unit[num_unit2].health}")
       
      #   else:
      #     second_army.kind_of_unit[num_unit2].health -= first_army.kind_of_unit[num_unit1].attack
      #     #print(f" Здоровье 2 незащитника {second_army.kind_of_unit[num_unit2].health}")
      # # если второй жив, он наносит урон первому
      #   if second_army.kind_of_unit[num_unit2].health > 0:
      #     if isinstance(first_army.kind_of_unit[num_unit1], Defender):
          
      #       first_army.kind_of_unit[num_unit1].health -= (second_army.kind_of_unit[num_unit2].attack - first_army.kind_of_unit[num_unit1].defense)
      #       #print(f" Здоровье 1 защитника {first_army.kind_of_unit[num_unit1].health}")

      #     else:
      #       first_army.kind_of_unit[num_unit1].health -= second_army.kind_of_unit[num_unit2].attack
      #       #print(f" Здоровье 1 незащитника {first_army.kind_of_unit[num_unit2].health}")

      # когда кто-то умер, он соответственно своей армии убирается из списка воинов
      if first_army.kind_of_unit[num_unit1].health > 0:
        second_army.kind_of_unit.pop()
        num_unit2 -= 1

      else:
        first_army.kind_of_unit.pop()
        num_unit1 -= 1
     # вернет True, если в первой армии остались живые
    return len(first_army.kind_of_unit) > 0 

# def health_update(unit_1, unit_2):
  # if unit_2.attack > unit_1.defense:
  #   loss = unit_2.attack - unit_1.defense
  # else:
  #   loss = 0
  # unit_1.health -= loss
  # return unit_1.health


# fight between two units
def fight(unit_1, unit_2):
    # пока здоровье первого больше 0, битва продолжается 
  while unit_1.health > 0 and unit_2.health > 0:
    # unit_2.health = health_update(unit_2, unit_1)
    unit_2.suffer(unit_1.attack)
    unit_1.hit(unit_2)
    # unit_1.health = health_update(unit_1, unit_2)
    unit_1.suffer(unit_2.attack)
    # print(f" Здоровье 2 {unit_2.health}")
    # print(f" Здоровье 1 {unit_1.health}")

    # if isinstance(unit_2, Defender) and unit_2.defense < unit_1.attack:
    #   unit_2.health -= (unit_1.attack - unit_2.defense)
    #  # print(f" Здоровье 2 защитника {unit_2.health}")
    # elif isinstance(unit_2, Defender) and unit_2.defense > unit_1.attack:
    #   unit_2.health -= 0
    # else:
    #   unit_2.health -= unit_1.attack
    #  # print(f" Здоровье 2 незащитника {unit_2.health}")

    # if isinstance(unit_1, Defender) and unit_1.defense < unit_2.attack:
    #   unit_1.health -= (unit_2.attack - unit_1.defense)
    # #  print(f" Здоровье 1 защитника {unit_1.health}")
    # elif isinstance(unit_1, Defender) and unit_1.defense > unit_2.attack:
    #   unit_1.health -= 0
    # else:
    #   unit_1.health -= unit_2.attack 
    # #  print(f" Здоровье 1 незащитника {unit_2.health}")

  if unit_2.health > unit_1.health:
    unit_1.is_alive = False
    return False
  else:
    unit_2.is_alive = False
    return True


# my_army = Army()
# my_army.add_units(Warrior, 3)
# enemy = Army()
# enemy.add_units(Defender, 2)
# print(my_army.kind_of_unit[1].attack)
# print(enemy.kind_of_unit[1].attack)





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
    john = Rookie()

    # print(fight(lancelot, john))
    # print(lancelot.health)


    # print(isinstance(bob, Defender))
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    #print(fight(bob, mike))
    assert fight(bob, mike) == False
   # print(fight(lancelot, rog))
    assert fight(lancelot, rog) == True


    # #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
