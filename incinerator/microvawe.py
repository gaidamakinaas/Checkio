# Bridge pattern
class MicrovaweBase:
  def __init__(self):
    self._seconds = 0

  def set_time(self, time):
    self._seconds = int(time[0:2])*60 + int(time[3:5])
  
  def add_time(self, amount):
    sec = self._seconds
    if amount[-1] == "s":
      sec += int(amount[0:-1])
    else:
      sec += int(amount[0:-1])*60
    self._seconds = sec if sec < 90*60 else 90*60
    return self._seconds

  def del_time(self, amount):
    sec = self._seconds
    if amount[-1] == "s":
      sec -= int(amount[0:-1])
    else:
      sec -= int(amount[0:-1])*60
    self._seconds = sec if sec > 0 else 0
    return self._seconds
  

  def show_time(self):
    min, sec = divmod(self._seconds, 60)
    # print(self._seconds)
    # print(min, sec)
    return '{:02d}:{:02d}'.format(min, sec)

class Microwave1(MicrovaweBase):
  def show_time(self):
      return '_' + super().show_time()[1:]

class Microwave2(MicrovaweBase):
  def show_time(self):
      return super().show_time()[:-1] + '_'

class Microwave3(MicrovaweBase):
  pass

class RemoteControl:
  def __init__(self, microwave: MicrovaweBase):
    self.microwave = microwave

  def set_time(self, time):
    return self.microwave.set_time(time)
  
  def add_time(self, amount):
    return self.microwave.add_time(amount)

  def del_time(self, amount):
    return self.microwave.del_time(amount)
 
  def show_time(self):
    return self.microwave.show_time()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")
    
    remote_control_3 = RemoteControl(microwave_3)  
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")
    
    # print(remote_control_1.show_time())
    # print(remote_control_2.show_time())
    # print(remote_control_3.show_time())
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")