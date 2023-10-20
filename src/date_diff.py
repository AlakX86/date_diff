from days_between_dates import days_between_dates
from request_user_date import request_final_user_date, request_start_user_date
def date_diff():
    start_year, start_month, start_day = request_start_user_date()
    final_year, final_month, final_day = request_final_user_date()

    day, month, year = days_between_dates(start_year, start_month, start_day, final_year, final_month, final_day)

    print(f"total days:{day} \ntotal months:{month} \ntotal years:{year} \nIn clear terms: {year} years and {month%12} months")

date_diff()
input("Presiona Enter para salir...")
