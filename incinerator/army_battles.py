class Warrior:
  def __init__(self, health = 50, attack=5):
    self.health = health
    self.attack = attack
    self.is_alive = True 

class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)



class Army():
  def __init__(self):
    self.kind_of_unit = [] 
    # self.number = 0

  def add_units(self, kind_of_unit, amount):
      for _ in range(amount):
        # i = kind_of_unit()
        self.kind_of_unit.append(kind_of_unit())
    # for n in range(number):  
    #   if kind_of_unit == "Warrior":
    #     n = Warrior()
    #     self.kind_of_unit.append(n)
    #   else:
    #     n = Knight()
    #     self.kind_of_unit.append(n)


  # just for self-checking
  # def get_units(self):
  #   for i in range(0, len(self.kind_of_unit)):
  #     print(self.kind_of_unit[i])

  # def length(self):
  #   return len(self.kind_of_unit)

  def __getitem__(self, index):
    return self.kind_of_unit[index]
     


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
        second_army.kind_of_unit[num_unit2].health -= first_army.kind_of_unit[num_unit1].attack
      # если второй жив, он наносит урон первому
        if second_army.kind_of_unit[num_unit2].health > 0:
          first_army.kind_of_unit[num_unit1].health -= second_army.kind_of_unit[num_unit2].attack
      # когда кто-то умер, он соответственно своей армии убирается из списка воинов
      if first_army.kind_of_unit[num_unit1].health > 0:
        second_army.kind_of_unit.pop()
        num_unit2 -= 1

      else:
        first_army.kind_of_unit.pop()
        num_unit1 -= 1
     # вернет True, если в первой армии остались живые
    return len(first_army.kind_of_unit) > 0 

    

# fight between two units
def fight(unit_1, unit_2):
    # пока здоровье первого больше 0, битва продолжается 
  while unit_1.health > 0:
    unit_2.health -= unit_1.attack
    unit_1.health -= unit_2.attack
  if unit_2.health > unit_1.health:
    unit_1.is_alive = False
    return False
  else:
    unit_2.is_alive = False
    return True


# my_army = Army()
# my_army.add_units("Knight", 5)
# my_army.get_units()
# print(my_army.kind_of_unit[2].health)
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    # assert fight(chuck, bruce) == True
    # assert fight(dave, carl) == False
    # assert chuck.is_alive == True
    # assert bruce.is_alive == False
    # assert carl.is_alive == True
    # assert dave.is_alive == False
    # assert fight(carl, mark) == False
    # assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()
    print(battle.fight(army_3, army_4))
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")