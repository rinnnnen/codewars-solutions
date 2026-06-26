def decode(string_):
    if not isinstance(string_, str):
        return "Input is not a string"
    abc = "abcdefghijklmnopqrstuvwxyz"
    rev_abc = abc[::-1]
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    REV_ABC = ABC[::-1]
    result = ""
    for char in string_:
        if char in abc:
            index = abc.index(char)
            result += rev_abc[index]
        elif char in ABC:
            index = ABC.index(char)
            result += REV_ABC[index]
        else:
            result += char
    return result
