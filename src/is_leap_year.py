def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 != 0:
            return True

if __name__ == "__main__":
    print(is_leap_year(1600), "=> True")
    print(is_leap_year(2020), "=> True")
    print(is_leap_year(2022), "=> None")
    print(is_leap_year(2024), "=> True")
    print(is_leap_year(2100), "=> None")
