from datetime import date
import sys
import inflect

def main():
    dob_input = input("date of birth (YYYY-MM-DD): ")
    birth_date = get_date(dob_input)
    today = date.today()

    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)

    print(f"{words} minutes")

def get_date(dob_input):
    try:
        return date.fromisoformat(dob_input)
    
    except ValueError:
        sys.exit("invalid date")


def calculate_minutes(birth_date, today):
    if birth_date > today:
        sys.exit("invalid date")

    days = (today - birth_date).days

    return days * 24 * 60


def convert_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    words  = words.replace(",", "")

    return words.capitalize()



if __name__ == "__main__":
    main()