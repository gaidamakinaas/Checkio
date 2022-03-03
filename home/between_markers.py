def between_markers(text: str, begin: str, end: str) -> str:
    # БУДЕМ ИСКАТЬ, НАЧИНАЯ С ИНДЕКСА ПОСЛЕ МАРКЕРА
    begin_index = text.find(begin) + len(begin)
    # И ЗАКАНЧИВАЯ ИНДЕКСОМ ДО МАРКЕРА
    end_index = text.find(end)

    if begin not in text:
        begin_index = 0
    if end not in text:
        end_index = len(text)
    return text[begin_index:end_index]
