def is_ascending(items) -> bool:
    # your code here
    count = 0
    if items == [] or len(items) == 1:
        return True
    for i in range(0, len(items)-1):
        if items[i+1] > items[i]:
            res = True
        else:
            res = False
            break
    return res
       
print(is_ascending([4, 5, 6, 7, 3, 7, 9]))
