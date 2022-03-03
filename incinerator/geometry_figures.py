
from abc import ABC, abstractmethod

# base stragedy interface 
class BaseFigure(ABC):

    @abstractmethod
    def perimeter(self, param):
        pass

    @abstractmethod
    def area(self, param):
        pass

    @abstractmethod
    def volume(self, param):
        pass

# analog Context class
class Parameters:
  
    def __init__(self, parameter) -> None:
        self.parameter = parameter


    def choose_figure(self, strategy: BaseFigure) -> None:
      self.strategy = strategy
     # return self.strategy

    def perimeter(self):
      return self.strategy.perimeter(self.parameter)


    def area(self):
      return self.strategy.area(self.parameter)


    def volume(self):
      return self.strategy.volume(self.parameter)
      

    def __repr__(self) -> str:
      return self.__class__.__name__


pi = 3.1415926

class Circle:

    def perimeter(self, param):
      return round(2*pi*param, 2)
    
    def area(self, param):
      return round(pi*param**2, 2)

    def volume(self, param):
      return 0


class Triangle:

    def perimeter(self, param):
      return param*3
    
    def area(self, param):
      return round((3**(0.5)*param**2)/4, 2)

    def volume(self, param):
      return 0

class Square:

    def perimeter(self, param):
      return param*4
    
    def area(self, param):
      return param**2

    def volume(self, param):
      return 0

class Pentagon:

  def perimeter(self, param):
    return param*5
    
  def area(self, param):
    return round(((25 + 10 * 5**(0.5))**(0.5))/4 * param**2, 2)

  def volume(self, param):
    return 0

class Hexagon:

  def perimeter(self, param):
    return param*6
    
  def area(self, param):
    return round((3*3**(0.5) * param**2)/2, 2)

  def volume(self, param):
    return 0

class Cube:

  def perimeter(self, param):
    return param*12
    
  def area(self, param):
    return 6*param**2

  def volume(self, param):
    return param**3


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)
    
    figure.choose_figure(Circle())
   # print(figure.choose_figure(Circle()))
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")


