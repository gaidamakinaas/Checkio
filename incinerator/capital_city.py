# # SINGLTON example

# class Singleton:
#   __instance = None

#   def __new__(cls, *args, **kwargs):
#     if cls.__instance is None:
#       cls.__instance = super().__new__(cls)
#     else:
#       print("Instance already created:", cls.getInstance())

#     return cls.__instance

#   def __repr__(self) -> str:
#       return self.__class__.__name__

#   @classmethod
#   def getInstance(cls):
#     if not cls.__instance:
#       cls.__instance = Singleton()
#     return cls.__instance


class Capital:
  __instance = None
  first_init = True
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    #   print("Obj created")
    # else:
    #   print("Instance already created:", cls.__instance)
    return cls.__instance

  def __init__(self, city_name):
    if self.first_init:
      self.city_name = city_name
      self.first_init = False

  def __repr__(self) -> str:
    return self.__class__.__name__

  def name(self):
    return self.city_name


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    # print(ukraine_capital_1.name())
    ukraine_capital_2 = Capital("London")
    # print(ukraine_capital_2.name())
    ukraine_capital_3 = Capital("Marocco")
    
    # print(ukraine_capital_3.name())
    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
    







# class Singleton:
#     __instance = None
#     def __init__(self):
#         if not Singleton.__instance:
#             print(" __init__ method called..")
#         else:
#             print("Instance already created:", self.getInstance())

#     @classmethod
#     def getInstance(cls):
#         if not cls.__instance:
#             cls.__instance = Singleton()
#         return cls.__instance

# s = Singleton() ## class initialized, but object not created
# print("Object created", s) # Object gets created here
# s1 = Singleton() ## instance already created

# print(s is s1)

