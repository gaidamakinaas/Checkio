import math
def split_list(items: list) -> list:
    # your code here
    first_ar = []
    sec_ar = []

    if len(items) % 2 != 0:
        middle = math.ceil((len(items)/2) - 1)
        
        for i in range(0, middle+1):
            first_ar.append(items[i])
            
        for j in range(middle+1, len(items)):
            sec_ar.append(items[j])

    elif len(items) % 2 == 0:
        middle = int((len(items)/2))
        for i in range(0, middle):
            first_ar.append(items[i])
        for j in range(middle, len(items)):
            sec_ar.append(items[j])

    return [first_ar, sec_ar]



print(split_list([]))