def isometric_strings(x,y):
   # print()
  #  res = set(zip(x, y))
  #  print(res)
    #print()
  #  resu = set(x)
  #  print(resu)
    return len(set(zip(x, y))) == len(set(x))

print(isometric_strings("add", "egg"))
# суть метода в том, что множество не содержит повторяющихся элементов
# мы создаем новое множество из строки х, оставляя уникальные буквы
# сопоставляем две строки: zip() - делает кортеж из элементов
# set() - представляет кортеж в виде множества
# сравниваем длины получившихся уникальных элементов, то есть тех, которые мы можем сопоставить,
# и уже сопоставленных с помощью zip
