
def unix_match(filename: str, pattern: str) -> bool:
    
    result = True
    #если длина паттера изначально больше длины имени, то можно ничего не искать больше
    if len(pattern) > len(filename):
        result = False
    #если нужно найти совпадение по одному любому символу:
    if '?' in pattern and '*' not in pattern:
        # но если ищем по 1 символу, то все остальные должны быть одинаковые
        # поэтому, если разные длины, то нет смысла искать 
        if len(filename) != len(pattern):
            result = False
        else:

            for i in range(0, len(filename)):
                # если не совпадают символы, то возвращаем false
                if filename[i] != pattern[i] and pattern[i] != '?':
                    result = False
    # если символы в названии паттерна не содержатся в названии файла,
    # не содержат знаков "поиска", то файл не найден по этому шаблону
    for char in pattern:
        if char != "*" and char != '?' and char not in filename:
            result = False
    # проверяем, совпадают ли расширения файла и паттерна
    # и не нужно ли нам любое расширение ("*")
    # также не должно быть поиска в расширении только по одному любому символу ("?")
    if '.' in filename:
        file_extension = filename.split(".")[1]
        # print(file_extension)
        if '.' in pattern:
            pattern_extension = pattern.split(".")[1]
            # print(pattern_extension)
            # если все(!) эти условия не выполняются, то файл тоже не может быть найден по паттерну
            if file_extension != pattern_extension and pattern_extension != '*' and '?' not in pattern_extension:
                result = False


    return result
print(unix_match("12apache1.log","*.*"))

#ВТОРОЙ ВАРИАНТ. ПРОХОДИТ ВСЕ ТЕСТЫ НА CHECKIO, НО НЕДОСТУПЕН ТАМ
# from fnmatch import fnmatch

from fnmatch import fnmatch
def unix_match(filename, pattern):
    f = fnmatch(filename, pattern)
    return f

# print(unix_match("12apache1.log","*.*"))


if __name__ == "__main__":
    print("Example:")
    print(unix_match("somefile.txt", "*"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("somefile.txt", "somefile.txt") == True
    assert unix_match("1name.txt", "[!abc]name.txt") == True
    assert unix_match("log1.txt", "log[!0].txt") == True
    assert unix_match("log1.txt", "log[1234567890].txt") == True
    assert unix_match("log1.txt", "log[!1].txt") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
