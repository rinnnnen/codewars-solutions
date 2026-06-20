def hydrate(drink_string): 
    total = sum(int(char) for char in drink_string if char.isdigit()) #isdigit get numbers clear from any symbols except numbers
    if total == 1:
        return f"{total} glass of water" #formatted f string
    else:
        return f"{total} glasses of water"
