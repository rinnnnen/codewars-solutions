def bmi(weight, height):
    bmi = weight / (height * height) # bc bmi = weight / height2 => height2 == height * height
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
