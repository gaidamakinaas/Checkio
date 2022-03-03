import copy

# создатель
# class Text:
#     def __init__(self):
#       self.text = ''
#       self.font_name = ''

#     def write(self, text):
#       if self.font_name != "":
#         self.text = self.text[0:len(self.font_name)+2] + text
#       else:
#         self.text += text

#     def set_font(self, font_name):
#       self.font_name = font_name
#       if (self.font_name != ''):
#         self.font_name = '[' + self.font_name + ']'
#       else:
#         self.font_name = ''
#       return self.font_name

#     def show(self):
#       return '{}{}{}'.format(self.font_name, self.text, self.font_name)

#     def restore(self, text):
#       self.text = text
#       #self.font_name = text.font_name

class Text:
    def __init__(self):
        self.text = ''
        self.font = ''

    def set_font(self, font):
        self.font = font

    def write(self, text):
        self.text += text

    def restore(self, text):
        self.text = text.text
        self.font = text.font

    def show(self):
        if (self.font != ''):
            font = '[' + self.font + ']'
        else:
            font = ''
        return '{}{}{}'.format(font, self.text, font)

class Memento():
    """
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """
        
    def save_text(self, text) -> str:
        pass

    def get_version(self, version) -> str:
        pass


class SavedText(Memento):
    def __init__(self):
        self.texts = {}
        self.last_version = 0

    def save_text(self, text):
        self.texts[self.last_version] = copy.copy(text)
        self.last_version += 1

    def get_version(self, version):
        return self.texts[version]


# class SavedText(Memento):

#   def __init__(self) -> None:
#     self.texts = []

#   def save_text(self, text):
#     self.texts.append(text.text)
#     #print(self.text)

#   def get_version(self, version) -> str:
#     return self.texts[version]

#   def __repr__(self) -> str:
#     return self.texts


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    print(f" first write: {text.text}")
    saver.save_text(text)

    text.set_font("Arial")

    saver.save_text(text)

   # print(saver.text)

    text.write("there was nothing.")

    print(f"second{text.show()}")
    print()
    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    print(f"resore {text.show()}")
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")

# import copy 
 
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] 
# list2 = copy.copy(list1) 
 
# list1.append([13, 14,15]) 
 
# print("Old list:", list1) 
# print("New list:", list2) 
