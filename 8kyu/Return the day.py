def whatday(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
    if 1 <= num <= 7:
        return days[num - 1] #bc counting from zero
    else:
        return "Wrong, please enter a number between 1 and 7"
