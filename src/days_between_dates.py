from request_user_date import request_final_user_date, request_start_user_date
from next_day import next_day
from next_month import next_month
from next_year import next_year
def days_between_dates():
    start_year, start_month, start_day = request_start_user_date()
    final_year, final_month, final_day = request_final_user_date()

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
        
    return f"total days:{day} \ntotal months:{month} \ntotal years:{year} \nIn clear terms: {year} years and {month%12} months"

print(days_between_dates())
input("Presiona Enter para salir...")
