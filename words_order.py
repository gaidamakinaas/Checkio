
def words_order(text, words):
    text_split = text.split() # разделяем строку на слова
    ind = -1 # индекс, с которого начнем считать
     # для каждого слова в списке слов будет использована 
    # ф. index(), поэтому оборачиваем программу в блок try-except
    for word in words:
        if words.count(word) > 1:
            return False
        try:
           ind = text_split.index(word, ind + 1)
           
        except ValueError:
            return False
    return True

print(words_order("hi world world im here",["world","world"]))