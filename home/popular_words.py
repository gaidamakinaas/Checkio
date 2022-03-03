from itertools import count

def popular_words(text: str, words: list) -> dict:
    # your code here
    dict = {}
    count = 0
    text = text.lower()
    new_text= text.split()
   
    for w in words:
        dict[w] = new_text.count(w)
    return dict

print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
