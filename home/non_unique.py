def checkio(data):
    new_list = []
    for item in data:
        if data.count(item) > 1:
            new_list.append(item)
    return new_list

print(checkio([1, 2, 3, 4, 5]))