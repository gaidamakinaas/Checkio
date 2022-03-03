def all_the_same(elements) -> bool:
# умножаем массив из первого элемента из исходного массива 
# на длину исходного массива. опять должен получиться исходный массив, если 
# все эл-ты одинаковые
    if not elements:
        return True
    return [elements[0]] * len(elements) == elements
