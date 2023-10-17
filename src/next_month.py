def next_month(month,day):
    if month == 2:
        return day == 28
    elif day == 29:
        return day
