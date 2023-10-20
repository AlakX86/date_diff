from next_day import next_day
from next_month import next_month
from next_year import next_year
def days_between_dates(start_year, start_month, start_day, final_year, final_month, final_day):

    if [start_year, start_month, start_day] > [final_year, final_month, final_day]:
        raise ValueError("La fecha inicial debe ser anterior o igual a la fecha final")

    day, month, year = 0, 0, 0
    start_year_copy, start_month_copy, start_day_copy = start_year, start_month, start_day

    while [start_year_copy, start_month_copy, start_day_copy] != [final_year, final_month, final_day]:
        start_year_copy, start_month_copy, start_day_copy = next_day(start_year_copy, start_month_copy, start_day_copy)

        if next_year(start_month_copy,start_day_copy):
            year += 1
        
        if next_month(start_day_copy, start_day,start_year_copy,start_month_copy):
            month += 1
        
        day += 1
        
    return day, month, year

if __name__ == "__main__":
    assert days_between_dates(2000, 2, 29, 2023, 3, 1) == (8401, 276, 23)
    assert days_between_dates(1954, 2, 28, 2022, 10, 2) == (25053, 823, 68)
    