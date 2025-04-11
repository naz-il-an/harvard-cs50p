from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    counted_mins = convert_date(input('Date of Birth: '))
    print(counted_mins)


def convert_date(birthday):
    try:
        today = date.today()
        year, month, day = birthday.split('-')
        num_birthday = date(int(year), int(month), int(day))
        days_past = (abs(today - num_birthday)).days
        minutes_past = days_past * 24 * 60
        minutes_past = p.number_to_words(minutes_past, andword='').capitalize() + ' ' + p.plural_noun('minute', minutes_past)
        return minutes_past
    except ValueError:
        raise sys.exit('Invalid date')


if __name__ == "__main__":
    main()