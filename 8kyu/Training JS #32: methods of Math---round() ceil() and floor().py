import math

def round_it(n):
    left, right = str(n).split(".") # separates characters from "."
    if len(left) > len(right):
        return math.floor(n)
    elif len(left) < len(right):
        return math.ceil(n)
    else:
        return round(n)
