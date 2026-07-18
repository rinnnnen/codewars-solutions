def get_count(sentence):
    vowels = "aeiou" # как не странно, так тоже можно, компьютеру срать 
    return sum(sentence.count(y) for y in vowels) # складывает подсчитанные в строке найденные гласные через цикл
