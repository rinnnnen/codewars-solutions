def split_odd_and_even(n):
    s = str(n)
    result = []
    current_group = s[0]
    for char in s[1:]: # запускает цикл со второй цифры для сравнения 
        if int(char) % 2 == int(current_group[-1]) % 2: # если остаток от :2 = последний символ в текущей группе :2 
            current_group += char # приклеивает символ если  остатки равны 
        else:
            result.append(int(current_group)) #превращаем курент_груп в число и число добавляется в список
            current_group = char # очищается группа и добавляется в список новый список новое число чар
    result.append(int(current_group)) # те числа, которые еще не добавились в список, добавляются туда принудительно
    return result
