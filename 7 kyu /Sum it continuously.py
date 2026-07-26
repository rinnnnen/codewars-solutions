def add(list):
    result = [] # складываем суммы
    total = 0 # текущая накопленная сумма
    for number in list: 
        total += number # добавляем число к сумме
        result.append(total) # сохраняю сумму в результат
    return result
