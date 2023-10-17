from days_in_month import days_in_month
def next_day(year, month, day):
    day += 1
    days_in_this_month = days_in_month(month, year)
    if day > days_in_this_month:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return year, month, day

if __name__ == "__main__":
    print(next_day(2023,12,31), "=> 2024, 1, 1")
    print(next_day(1999,1,31), "=> 1999, 2, 1")
    print(next_day(2100,3,23), "=> 2100,3 ,24")
