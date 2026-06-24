def calculate_age(year_of_birth, current_year):
    difference =  current_year - year_of_birth
    if difference > 0:
        word = "year" if difference == 1 else "years" #bc 1=year, >=2 = years
        return f"You are {difference} {word} old."
    elif difference < 0:
        years_to_birth = abs(difference)
        word = "year" if years_to_birth == 1 else "years" 
        return f"You will be born in {years_to_birth} {word}."
    else:
        return "You were born this very year!"
