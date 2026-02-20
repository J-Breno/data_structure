def format_date(day, month, year):
    if int(day) < 10:
        day = "0" + str(day)

    if int(month) < 10:
        month = "0" + str(month)

    print(f"{day}/{month}/{year}")

format_date("21", "7", "2010")