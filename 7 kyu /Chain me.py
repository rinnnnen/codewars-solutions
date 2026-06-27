def chain(init_val, functions):
    value = init_val # make a new variable for save current value
    for func in functions:
        value = func(value) # return function and save this result
    return value
