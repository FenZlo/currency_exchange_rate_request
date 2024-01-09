from json import JSONDecodeError
from httpx import request
from loguru import logger
from datetime import date
from calendar import monthrange
from data_base import create_db_and_base, is_course_on_date_exist, create_curse_on_date

YEAR = 2023
MONTH = 11


def get_datime_range(year: int = YEAR, month: int = MONTH) -> list[date]:
    last_day = monthrange(year, month)[1]
    return [date(year, month, day) for day in range(1, last_day + 1)]


def get_curse(date_: date, base_currency: str = 'eur', target_currency: str = 'rub') -> float:  # сигнатура функции
    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date_.strftime("%Y-%m-%d")}/currencies/{base_currency}.json'
    response = request(method='get', url=url)
    json = response.json()
    curse = json[base_currency][target_currency]
    return curse


def get_currency_curse_on_date(base_currency: str = 'eur', target_currency: str = 'rub'):
    range_date = get_datime_range()

    for date_ in range_date:

        if is_course_on_date_exist(date_):
            logger.debug(f'Curse for date: {date_} is already exist')
            continue

        try:
            curse = get_curse(date_, base_currency, target_currency)

        except JSONDecodeError as e:
            logger.warning(f'Error retrieving data for {date_}: {e}')
            continue

        logger.debug(f'Date: {date_} curse: {curse}')

        create_curse_on_date(date_, curse)


if __name__ == '__main__':
    create_db_and_base()
    get_currency_curse_on_date()
