def sum_numbers(text: str) -> int:
    # your code here
    sum = 0
    string = text.split(sep=" ")
    for word in string:
        if word.isdigit():
            sum += int(word)

    return sum

print(sum_numbers('5 plus 6 is'))