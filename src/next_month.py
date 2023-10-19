from is_leap_year import is_leap_year
def next_month(day, first_day,year,month):
    if day == first_day:
        return True
    if first_day in [29,30,31]:
        if month == 2:
            if is_leap_year(year):
                if day == 29:
                    return True
            if not is_leap_year(year):
                if day == 28:
                    return True
        if month in [1,3,4,5,6,7,8,9,10,11,12]:
            if day == first_day:
                return True
