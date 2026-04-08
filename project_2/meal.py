def convert(time):
    hour, mins = map(float, time.split(":"))
    return hour + mins / 60


def main():
    time = input("time: ").strip()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

main()