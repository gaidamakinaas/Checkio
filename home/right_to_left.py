def left_join(phrases: tuple) -> str:
    string = ",".join(phrases)
    rep = string.replace("right", "left")

    return rep

print(left_join(("enough", "jokes")))