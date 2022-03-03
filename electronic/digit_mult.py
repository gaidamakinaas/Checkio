def checkio(number: int) -> int:
    num = str(number)
    mult = 1
    for digit in num:
        if digit != '0':
            mult = mult * int(digit)

    return mult

    