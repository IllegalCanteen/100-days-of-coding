def life_in_weeks(years):
    if isinstance(years, int):
        weeks=(90-years)*52
        print(f"You have {weeks} weeks left until you are 90" )
    else:
        print("Invalid input")
age=int(input("How many years old are you? "))
life_in_weeks(age)


