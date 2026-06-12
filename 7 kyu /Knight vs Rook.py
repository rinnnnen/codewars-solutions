def knight_vs_rook(knight, rook):
    knight_x, knight_y = knight[0], ord(knight[1]) # its module
    rook_x, rook_y = rook[0], ord(rook[1]) #its module too
    if knight_x == rook_x or knight_y == rook_y:
        return "Rook"
    dx = abs(knight_x - rook_x) # abs do result of the equation in module
    dy = abs(knight_y - rook_y)
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return "Knight"
    return "None"
