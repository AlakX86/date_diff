from days_in_month import days_in_month
def request_start_user_date():
    print("Please put the starting year")
    start_year = int(input())
    print ("Please put the starting month")
    while True:
        start_month = input()
        if start_month.isdigit():
            start_month = int(start_month)
            if start_month in [1,2,3,4,5,6,7,8,9,10,11,12]:
                break
            else:
                print("Write a number between 1 and 12 please")
        else:
            print("Please enter a valid integer for the month.")
    print("Please put the starting day")
    while True:
        start_day = input()
        if start_day.isdigit():
            start_day = int(start_day)
            if start_day in range(1, days_in_month(start_month, start_year) + 1):
                break
            else:
                print(f"Write a number between 1 and {days_in_month(start_month, start_year)} please")
        else:
            print("Please enter a valid integer for the day.")
    return start_year, start_month, start_day


def request_final_user_date():
    print("Please put the final year")
    final_year = int(input())
    print ("Please put the final month")
    while True:
        final_month = input()
        if final_month.isdigit():
            final_month = int(final_month)
            if final_month in [1,2,3,4,5,6,7,8,9,10,11,12]:
                break
            else:
                print("Write a number between 1 and 12 please")
        else:
            print("Please enter a valid integer for the month.")
    print("Please put the final day")
    while True:
        final_day = input()
        if final_day.isdigit():
            final_day = int(final_day)
            if final_day in range(1, days_in_month(final_month, final_year) + 1):
                break
            else:
                print(f"Write a number between 1 and {days_in_month(final_month, final_year)} please")
        else:
            print("Please enter a valid integer for the day.")
    return final_year,final_month,final_day
