
def count_digits(text: str) -> int:
 
    count = 0
    string = "".join(text)
    for word in string:
        if word.isdigit():
            count += 1

    
    return count

