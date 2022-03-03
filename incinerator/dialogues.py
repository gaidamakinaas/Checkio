# from __future__ import annotations
# from abc import ABC

VOWELS = "aeiou"


class Chat:
  def __init__(self) -> None:
    self.human_name = None
    self.robot_adress = None
    self.history_chat = []
    self.history_message = []
    # self.history_human = []
    # self.history_robot = []
  
  def connect_human(self, human_name) -> None:
    self.human_name = human_name
    self.human_name.chat = self

  def connect_robot(self, robot_adress) -> None:
    self.robot_adress = robot_adress
    self.robot_adress.chat = self

  def show_human_dialogue(self):
    return '\n'.join(sender1.name + ' said: ' + mes for (sender1, mes) in zip(self.history_chat, self.history_message))
    
   # human_dialogue = f"{self.human_name} said: " + "".join(self.history_human) + "\n" + f"{self.robot_adress} said: " + "".join(self.history_robot)
    #return human_dialogue
  

  def show_robot_dialogue(self):
    def encode(mes):
      robot_mes = ""
      for sym in mes:
        robot_mes += "0" if sym in VOWELS else "1"
       # print(robot_mes)
      return robot_mes
    #print(encode(self.history_human))
    robot_dialogue = '\n'.join(sender1.name + ' said: ' + encode(mes) for (sender1, mes) in zip(self.history_chat, self.history_message))
    return robot_dialogue
    

  def notify(self, sender, message):
    self.history_chat.append(sender)
    self.history_message.append(message)

    #self.history_human.append(message)

  # def notify_robot(self, message):
  #   self.history_robot.append(message)



class BaseComponent():
  """
  Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
  посредника внутри объектов компонентов.
  """

  def __init__(self, name) -> None:
    self._chat = None
    self.name = name

  @property
  def chat(self) -> Chat:
    return self._chat

  @chat.setter
  def chat(self, chat: Chat) -> None:
    self._chat = chat


class Human(BaseComponent):
  # def __init__(self, human_name) -> None:
  #   self.name = human_name

  
  def send(self, message):
    self.chat.notify(self, message)

  # def __repr__(self) -> str:
  #   return self.name


class Robot(BaseComponent):
  # def __init__(self, robot_name) -> None:
  #   self.name = robot_name
  def send(self, message):
    self.chat.notify(self, message)
  
  # def __repr__(self) -> str:
  #   return self.name



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

  chat = Chat()
  karl = Human("Karl")
  bot = Robot("R2D2")
  chat.connect_human(karl)
  chat.connect_robot(bot)
  karl.send("Hi! What's new?")
  bot.send("Hello, human. Could we speak later about it?")

  print(chat.show_human_dialogue())
  print(chat.show_robot_dialogue())

  assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
  assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

  print("Coding complete? Let's try tests!")


karl = Human("Karl")

chat = Chat()

bot = Robot("R2D2")

chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
#print(karl.send("Hi! What's new?"))
#print(bot.send("Hello, human. Could we speak later about it?"))
# print(chat.connect_human(karl))

# print(chat.show_human_dialogue())
# print(chat.show_robot_dialogue())

# VOWELS = "aeiou"

# def encode(mes):
#   robot_mes = ""
 
#   for i in mes:
#         # if i in VOWELS:
#         #   robot_mes += "0"
#         # else:
#         #   robot_mes += "1"
#         #   print(robot_mes)
#     robot_mes += "0" if i in VOWELS else "1"
#   #print(robot_mes)
#   return robot_mes

# print(encode(["Hello, human. Could we speak later about it?"]))