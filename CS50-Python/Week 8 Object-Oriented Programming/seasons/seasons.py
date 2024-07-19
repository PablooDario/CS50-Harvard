from datetime import date
import sys
import inflect


def get_birthdate():
    try:
        # Date Format "YYYY-MM-DD"
        birthdate = date.fromisoformat(input("Date of Birth: "))
        return birthdate
    except ValueError:
        sys.exit("Invalid date")

def get_minutes_alive():
    p = inflect.engine()
    birthdate = get_birthdate()
    days_alive = (date.today() - birthdate).days
    minutes_alive = days_alive * 1440
    minutes = p.number_to_words(minutes_alive).capitalize()
    minutes = minutes.replace("and ", '')
    return minutes + " minutes"


def main():
    print(get_minutes_alive())



if __name__ == "__main__":
    main()
