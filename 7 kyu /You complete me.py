def complete(st):
    for i in range(1, len(st) + 1):
        if st[i:] == st[i:][::-1]: # if aba == aba but vice versa ([::-1])
            return st + st[:i][::-1]
    return st
