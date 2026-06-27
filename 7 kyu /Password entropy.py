import string
import math

def entropy(password):
    if not password:
        return 0
    pool_size = 0
    up = string.ascii_uppercase
    down = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    if any(char in up for char in password) == True: pool_size += 26
    if any(char in down for char in password) == True: pool_size += 26
    if any(char in digits for char in password) == True: pool_size += 10
    if any(char in punctuation for char in password) == True: pool_size += 32
    return round(len(password)) * math.log2(pool_size)
