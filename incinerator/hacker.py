

class HackerLanguage:
  def __init__(self) -> None:
    self.text = ""
    
  def write(self, text):
    self.text += text

  def delete(self, n):
    self.text = self.text[:-n]

  def send(self):
    message = ""
    special = "!?$%@:."
    for sym in self.text:
      if sym == " ":
        message += "1000000"
      elif sym.isdigit() or sym in special:
        message += sym
      else:
        message += bin((ord(sym)))[2:] # to ascii
    return message   


  def read(self, text):
    message = ""
    while text:
      if len(text) < 7:
        message += text
        text = "" # quit loop
      else:
         try:
          char_decimal = int(text[:7], 2)
          if char_decimal == 64:
            char_decimal = 32 # for space
          message += chr(char_decimal) #from ascii 
          text = text[7:]
         except:
          #  special = "!?$%@:."
          #  for sym in text:
          #    if sym in special

          message += text[0] # for digit and special
          text = text[1:]

    return message



# print('asdfgfkdifouy'[:7])
# print('asdfgfkdifouy'[8:])
#print(int("1101001",2))

#print(int("1110010",2)) #!!!!
#print(bin((ord("r")))[2:])

#print(chr(int("1100100",2))) #!!!! 

# print(chr(32))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()
    message = HackerLanguage()

    # print(message_1.send())
    # print(message_2.read("11001011101101110000111010011101100"))
    
    #test failed
    #print(message.read('1001001 1000000 1100001 1101101 1000000 1110100 1101001 1110010 1100101 1100100...'))

    print(message.read('1001001100000011000011101101100000011101001101001111001011001011100100...'))

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
