from os import sep


def backward_string_by_word(text: str) -> str:
    # # your code here
    # string = text.split(' ')

    # for word in string:
    #     reversed_word = joinword[::-1]
    # rev_str = ' '.join(new)
    #     rev = word[::-1]
    #     rever = ''.join(rev)

    return ' '.join(word[::-1] for word in text.split(' '))
   

print(backward_string_by_word('hello  world'))