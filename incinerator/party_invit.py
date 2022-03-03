# OBSERVER
# абстрактный наблюдатель

class Observer():


  def show_invites(self):
      pass

class Friend(Observer):
    
    def __init__(self, name) :
      self.name = name
      self.invites = []
      self.party = []
     

    def update(self, party, message: str):
      self.invites.append(message)
      self.party.append(party)

    def show_invite(self):
      if self.invites != []:
        for (x, y) in zip(self.party,self.invites):
          inv = f"{self.party[-1]}: {self.invites[-1]}"
      else:
        inv = "No party..."
      return inv

    def __repr__(self) -> str:
      return self.name
      

# абстрактный наблюдаемый, то есть издатель
class Observable():
  def __init__(self):
    self.friends = []     # инициализация списка наблюдателей
  
  def add_friend(self, name: Friend):
      self.friends.append(name)
    
  def del_friend(self, name: Friend):
      self.friends.remove(name)

  def notify_friends(self, party_name, message: str):
      for friend in self.friends:
        friend.update(party_name, message)




class Party(Observable):
  def __init__(self, party_name):
      super().__init__()
      self.party_name = party_name

  
  def send_invites(self, invite: str):
    self.notify_friends(self.party_name, invite)
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)


    print(john.show_invite())
    print(lucy.show_invite())
    print(nick.show_invite())
    print(chuck.show_invite())




    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")



