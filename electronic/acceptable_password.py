

def is_acceptable_password(psw: str):
    count = 0
    count_uniq = 0
    forbidden_word = ['password', 'PASSWORD']

    for w in forbidden_word:
        if w in psw:
            return False

    list_of_sym = []
    for i in range(0, len(psw)):
        list_of_sym.append(psw[i])
    set_res = set(list_of_sym)
    if len(set_res) >= 3:
        sym = True
    else:
        return False
       

    if sym:
        for d in psw:
                if d.isdigit():
                    count += 1
        if count >=1 and len(psw) > 6 and not psw.isdigit():
            return True
        elif len(psw)>9:
            return True
        else:
            return False
     

print(is_acceptable_password('aaaaaa1'))

# psw = 'fopff'
# sp = []
# for i in range(0, len(psw)):
#     sp.append(psw[i])
# set_res = set(sp)
# print(set_res)