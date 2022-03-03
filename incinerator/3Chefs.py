# абстрактная фабрика
class AbstractCook():
    def __init__(self) -> None:
      self.food_amount = 0
      self.food_price = 0
      self.drink_amount = 0
      self.drink_price = 0
      self.cooked_food = ""
      self.cooked_drink = ""

    def add_food(self, food_amount, food_price):
      self.food_amount += food_amount
      self.food_price += food_amount * food_price


    def add_drink(self, drink_amount, drink_price):
      self.drink_amount += drink_amount
      self.drink_price += drink_amount * drink_price

    def total(self):
      return f"{self.cooked_food}: {self.food_price}, {self.cooked_drink}: {self.drink_price}, Total: {self.food_price + self.drink_price}"

# конкретная фабрика
class JapaneseCook(AbstractCook):
    def __init__(self) -> None:
        super().__init__()
        self.cooked_food = "Sushi"
        self.cooked_drink = "Tea"        

# конкретная фабрика
class RussianCook(AbstractCook):
    def __init__(self) -> None:
        super().__init__()
        self.cooked_food = "Dumplings"
        self.cooked_drink = "Compote"

# конкретная фабрика
class ItalianCook(AbstractCook):
    def __init__(self) -> None:
        super().__init__()
        self.cooked_food = "Pizza"
        self.cooked_drink = "Juice"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    # print(client_1.total())
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")