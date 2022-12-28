import datetime
import pytz


def get_days_until_christmas():
    today = datetime.date.today()
    future = datetime.date(2022, 12, 25)
    diff = future - today
    print(f'Pana la Crăciun mai sunt: {diff.days} de zile')


get_days_until_christmas()


def get_days_until_birthday(birth_month, birth_day):
    current_time = datetime.datetime.now(pytz.timezone('Europe/Bucharest'))
    birthday_this_year = datetime.date(current_time.year, birth_month, birth_day)
    birthday_next_year = datetime.date(current_time.year + 1, birth_month, birth_day)
    today = datetime.date(current_time.year, current_time.month, current_time.day)
    if birthday_this_year < today:
        diff = birthday_next_year - today
    else:
        diff = birthday_this_year - today
    print(f'Pana la ziua ta mai sunt: {diff.days} de zile')
    if today == birthday_this_year:
        print('La multi ani, de ziua ta!')

print('Hai sa verificam cat mai e pana la ziua ta, completeaza urmatoarele date.')
user_birth_month = int(input('Luna in care iti serbezi ziua (MM): '))
user_birth_day = int(input('Ziua in care iti serbezi ziua(DD): '))
get_days_until_birthday(user_birth_month, user_birth_day)