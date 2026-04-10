def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            date = input("date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            elif "," in date:
                part1, year = date.split(",")
                month_name, day = part1.split()

                if month_name not in months:
                    continue
                
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year.strip())

            else:
                continue

            if month < 1 or month > 12 or day < 1 or day > 31:
                continue

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            continue


main()

   
