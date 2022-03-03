def checkio(array: list) -> int:
    sum = 0
    if array == []:
        return 0
    else:
        for i in range(0, len(array)):
            if i % 2 == 0:
                sum += array[i]

        sum = sum * array[-1]

    return sum

print(checkio([0, 1, 2, 3, 4, 5]))