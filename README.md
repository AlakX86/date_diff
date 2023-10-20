# date_diff
A script that calculates the total days, months and years between 2 dates
<h2>About the modules</h2>
date_diff is a program that asks for two different dates and calculates the time between them, telling you the total years, total months and total days (e.g. 365 days, 12 months, 1 year). It also offers a simplified version where it tells you how many years and months in relative format (e.g. 9 years and 8 months have passed).
<h2>The main program: date_diff</h2>
The code imports the days_between_dates and request_user_date functions from the corresponding modules and defines a function called date_diff. The function uses the request_start_user_date and request_final_user_date functions to prompt the user to enter a start date and an end date, and uses the days_between_dates function to calculate the number of days, months, and years between the two dates.

The code prints the total number of days, months, and years between the two dates, as well as a simplified version of the number of years and months. It then prompts the user to press Enter to exit.

The code is automatically executed at the end of the file.
<h2>Modules</h2>
This program consists of 7 modules:
<h3>is_leap_year</h3>
The is_leap_year function takes a year argument and returns True if the year is a leap year and False otherwise. A year is a leap year if it is divisible by 4, except if it is divisible by 100 but not by 400.
<h3>next_year</h3>
The next_year function takes two arguments, month and day, and returns True if the month is December and the day is 31. In other words, the function checks if the given date is the last day of the year.
<h3>days_in_month</h3>
The code defines a function called days_in_month that takes two arguments, month and year, and returns the number of days in the given month. The function uses a list called days_per_month that contains the number of days per month, and uses the is_leap_year function to determine whether February has 28 or 29 days, depending on whether the year is a leap year or not.
<h3>next_day</h3>
The code defines a function called next_day that takes three arguments, year, month and day, and returns the date of the next day in tuple format (year, month, day). The function uses the days_in_month function of the days_in_month module to determine the number of days in the given month.
<h3>next_month</h3>
The code defines a function called next_month that takes four arguments, day, first_day, year and month, and returns True if the day is the first day of the next month and False otherwise. The function uses the is_leap_year function of the is_leap_year module to determine if the year is a leap year and adjust the number of days in February accordingly.
<h3>request_user_date</h3>
The code defines two functions, request_start_user_date and request_final_user_date, which request the user to enter a start date and an end date in year, month and day format. The functions use the days_in_month function of the days_in_month module to validate that the day entered is within the valid range for the given month and year.
The functions prompt the user to enter the year, month and day using the input() function, and validate that the values entered are integers and within the valid range. If the user enters an invalid value, the user is prompted to enter a valid value.

The code defines two functions, request_start_user_date and request_final_user_date, which request the user to enter a start date and an end date in year, month and day format. The functions use the days_in_month function of the days_in_month module to validate that the day entered is within the valid range for the given month and year.
<h3>days_between_dates</h3>
The functions prompt the user to enter the year, month and day using the input() function, and validate that the values entered are integers and within the valid range. If the user enters an invalid value, the user is prompted to enter a valid value.
