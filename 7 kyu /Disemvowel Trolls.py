def disemvowel(string_):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for string in vowels:
        string_ = string_.replace(string, "")
    return string_
