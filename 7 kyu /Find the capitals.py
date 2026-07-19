def capitals(word):
    indices = [] #пустой список
    for index, char in enumerate(word): # енумерате - символ и его место одновременно
        if char.isupper(): # проверяет это ли стоит ЗАГЛАВНАЯ
            indices.append(index) #добавляет индекс в список
    return indices
