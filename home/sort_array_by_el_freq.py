def frequency_sort(items):
    # your code here
    #items.count в данном случае возращает количество элементов в порядке убывания
    #сортировка ведется сначала по количеству вхождений, затем по индексам, если количество одинаково
    #items.index вернет положение элемента 
    s = sorted(items, key=lambda i: (-items.count(i), items.index(i)))
    return s
print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))