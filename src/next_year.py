from is_leap_year import is_leap_year
def next_year(current_month, current_day, first_month, first_day, year):
    if first_month == 2:
        if first_day == 29:
            if is_leap_year(year):
                if current_month == 2:
                    if current_day == 29:
                        return True
            elif not is_leap_year(year):
                if current_month == 2:
                    if current_day == 28:
                        return  True
    if current_month == first_month:
        if current_day == first_day:
            return True
