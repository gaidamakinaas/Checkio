def checkio(words: str) -> bool:
    count = 0
    result = False
    string = words.split(sep=" ")
    for word in string:
        if word.isdigit():
            count = 0
        else:
            count += 1
            if count >= 3:
                result = True
                break
    return result
# def checkio(words: str) -> bool:
#     count = 0
#     res = True
#     for i in words.split():
#         print(i)
#         if i.isalpha():
#             count +=1
#             print(count)
#         else:
#             count = 0
#     if count <3:
#         res = False
#     return res


print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))