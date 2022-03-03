# ITERATOR

class Iterator():
    """
    Абстрактный итератор
    """

   # _error = None   # класс ошибки, которая прокидывается в случае выхода за границы коллекции

    def __init__(self, collection):
        """
        Constructor.

        :param collection: коллекция, по которой производится проход итератором
        :param cursor: изначальное положение курсора в коллекции (ключ)
        """
        self._collection = collection
       # self._cursor = cursor

   # @abstractmethod
    def first_channel(self):
        """
        Переключается на первый канал из списка. 
        """
        pass

   # @abstractmethod
    def last_channel(self):
        """
        переключается на последний канал из списка. 
        """
        pass

   # @abstractmethod
    def next_channel(self):
        """
        переключается на канал номер N. 
        Обратите внимание, что нумерация каналов начинается с 1, а не с 0. 
        """
        pass

    def turn_channel(self, n):
        """
        переключается на следующий канал. Если текущий канал - последний, 
        то эта команда переключает на первый канал. 
        """
        pass

    def previous_channel(self):
        """
       переключается на предыдущий канал.
       Если текущий канал - первый, то эта команда переключает 
       на последний канал. 
        """
        pass

    def current_channell(self):
        """
        возвращает название текущего канала. 
        """
        pass

    def is_exist(self,  n):
        """
        принимает 1 аргумент - число N или строку 'name' и 
        возвращает "Yes", если канал с номером N или названием 
        'name' существует в списке и "No" в ином случае. 
        """
        pass

class VoiceCommand(Iterator):
    """
    Итератор, проходящий по обычному списку
    """
    def __init__(self, channels: list):
      self._channels = channels
      self.cursor = 0

    def first_channel(self):
      return self._channels[self.cursor]

    def last_channel(self):
      self.cursor = -1
      return self._channels[self.cursor]

    def turn_channel(self, n):
        self.cursor = n-1
        return self._channels[self.cursor]
    
    def next_channel(self):
      if self.cursor == len(self._channels)-1:
        self.cursor = 0
      else:
        self.cursor += 1
      return self._channels[self.cursor]

    def previous_channel(self):
      self.cursor -= 1
      return self._channels[self.cursor]
    
    def current_channel(self):
      
      return self._channels[self.cursor]        
    
    def is_exist(self,  n):
      #ПО НОМЕРАМ 
      if type(n) == int:
        if n in range(0, len(self._channels)-1):
          return "Yes"
        else:
          res =  "No"
      else:
        for i in self._channels:
          if i == n:
            return "Yes"
          else:
            res = "No"
      return res
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    # assert controller.first_channel() == "BBC"
    # assert controller.last_channel() == "TV1000"
    # assert controller.turn_channel(1) == "BBC"
    # assert controller.next_channel() == "Discovery"
    # assert controller.previous_channel() == "BBC"
    # assert controller.current_channel() == "BBC"
    # assert controller.is_exist(4) == "No"
    # assert controller.is_exist("TV1000") == "Yes"
    CHANNELS = ['Nickelodeon', 'BBC', 'Discovery', 'TV1000']
    controller = VoiceCommand(CHANNELS)
    assert controller.turn_channel(3)
    assert controller.next_channel()
    assert controller.is_exist('BBC') == "Yes"
    print("Coding complete? Let's try tests!")