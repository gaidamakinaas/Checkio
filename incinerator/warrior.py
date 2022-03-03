
class Warrior:
    def __init__(self, health = 50, attack=5):
        self.health = health
        self.attack = attack
       # self.__is_alive = True 

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    

        



class Knight(Warrior):
    def __init__(self, health=50, attack = 7):
        super().__init__(health, attack)

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

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    john = Warrior()
    # john.set_is_alive()
    john.health = 50
    print(john.is_alive)

    # assert fight(chuck, bruce) == True
    # assert fight(dave, carl) == False
    # assert chuck.is_alive == True
    # assert bruce.is_alive == False
    # assert carl.is_alive == True
    # assert dave.is_alive == False
    # assert fight(carl, mark) == False
    # assert carl.is_alive == False

    # print("Coding complete? Let's try tests!")
