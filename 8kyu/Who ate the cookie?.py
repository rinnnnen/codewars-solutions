def cookie(x):
    if type(x) is str: # str - empty stroke
        return "Who ate the last cookie? It was Zach!"
    elif type(x) in (int, float) and type(x) is not bool:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
