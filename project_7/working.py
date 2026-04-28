import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.match(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    start = convert_time(h1, m1, p1)
    end = convert_time(h2, m2, p2)

    return f"{start} to {end}"


def convert_time(hours, minute, period):
    hours = int(hours)

    if minute:
        minute = int(minute)
    else:
        minute = 0

    if hours < 1 or hours > 12:
        raise ValueError
    if minute < 0 or minute > 59:
        raise ValueError

    if period == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minute:02}"


if __name__ == "__main__":
    main()