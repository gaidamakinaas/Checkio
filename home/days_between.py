import datetime

def days_diff(a, b):

    year_a = int(a[0])
    mounth_a = int(a[1])
    day_a = int(a[2])

    year_b = int(b[0])
    mounth_b = int(b[1])
    day_b = int(b[2])

    diff = abs((datetime.date(year_b, mounth_b, day_b) - datetime.date(year_a, mounth_a, day_a)).days)
    return diff

print(days_diff((2014, 1, 1), (2014, 8, 27)))