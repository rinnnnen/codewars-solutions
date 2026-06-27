from typing import Iterable, Callable

def one(xs: Iterable, predicate: Callable[..., bool]) -> bool:
    count = 0
    for item in xs:
        if predicate(item):
            count += 1
        if count > 1:
            return False
    return count == 1 # return True but if cycle doesnt have count > 1 
