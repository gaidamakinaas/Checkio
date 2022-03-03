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


  def suffer(self, damage):
    self.health -= damage

  def hit(self, enemy):
    enemy.suffer(self.attack)


class Knight(Warrior):
  def __init__(self, health=50, attack = 7):
    super().__init__(health, attack)


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
    return len(self.units) != 0

  @property
  def get_unit(self):
    return self.units[0]

  @property
  def delete_unit(self):
    self.units.pop(0)
    
  def __getitem__(self, index):
    return self.units[index]
     
class Battle():
  def fight(self, army_1, army_2):
    while army_1.is_alive and army_2.is_alive:
      if fight(army_1.get_unit, army_2.get_unit):
        army_2.delete_unit
      else:
        army_1.delete_unit
    return army_1.is_alive
       

def fight(unit_1, unit_2):
  while unit_1.is_alive and unit_2.is_alive:
    unit_1.hit(unit_2)    
    if unit_2.is_alive:
      unit_2.hit(unit_1)
  return unit_1.is_alive


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

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
