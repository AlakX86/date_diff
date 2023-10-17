from is_leap_year import is_leap_year
def days_in_month(month, year):
    # Lista con la cantidad de días por mes. De enero a Diciembre
    days_per_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12:
        return days_per_month[month - 1]
    else:
        return "El mes debe estar en el rango de 1 a 12"

if __name__ == "__main__":
    print(days_in_month(3,2021), "=> Deberia ser 31")
    print(days_in_month(13,2021), "=> El mes debe estar en el rango de 1 a 12")
    print(days_in_month(-1,2021), "=> El mes debe estar en el rango de 1 a 12")
    