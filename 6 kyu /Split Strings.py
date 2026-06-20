def solution(s):
    s_len = len(s)
    if s_len % 2 != 0:
        s += "_"
    else:
        pass
    result = [] #empty list for symbols
    for i in range(0, len(s), 2): #from zerost step, two steps
        result.append(s[i:i+2]) # i:i+2 divides by two for each symbol. append for +
    return result
