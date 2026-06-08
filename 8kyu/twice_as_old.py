
def twice_as_old(dad_years_old, son_years_old):
    x =2*son_years_old-dad_years_old # from dad_years_old - x == 2 * (son_years_old - x )
    if x < 0:
        return -x
    return x 
