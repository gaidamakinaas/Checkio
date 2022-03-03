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

def fight(unit_1, unit_2):
  while unit_1.is_alive and unit_2.is_alive:
    unit_1.hit(unit_2)    
    if unit_2.is_alive:
      unit_2.hit(unit_1)
  return unit_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
