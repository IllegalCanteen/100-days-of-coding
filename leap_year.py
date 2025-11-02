def is_leap_year(year):
    if year == "":
        print("Invalid input please type in a year")
        return
    try:
        year = int(year)
    except:
        print("invalid input please type in a number")
        return

    if year % 400 == 0:
        print("It is a leap year")
    elif year % 100 == 0:
        print("It is not a leap year")
    elif year % 4 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")

year = input("What is the current year? ")
is_leap_year(year)