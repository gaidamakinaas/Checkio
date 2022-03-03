import re
def first_word(text: str) -> str:

    first = re.findall(r"[\w']+", text)[0]
    return first


print(first_word("... and so on ...")) 
